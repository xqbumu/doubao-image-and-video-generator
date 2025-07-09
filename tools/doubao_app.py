import os
import requests
import json
from typing import Any, Dict, Optional


class DoubaoApp:
    """
    Doubao API client for text-to-image generation using OpenAI client
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://ark.cn-beijing.volces.com/api/v3",
        api_secret: str = None,  # 不需要使用，但保留参数以保持接口兼容性
        region: str = "cn-north-1",
    ):
        """
        Initialize the Doubao API client.

        Args:
            api_key: Volcengine API key
            api_secret: Not used in OpenAI client mode
            region: Not used in OpenAI client mode
        """
        self.api_key = api_key
        self.base_url = base_url

        if not self.api_key:
            raise ValueError("API key is required")

    def generate_image(
        self,
        prompt: str,
        model: str = "doubao-seedream-3-0-t2i-250415",
        size: str = "1024x1024",
        seed: int = None,
        guidance_scale: float = None,
        watermark: bool = False,
        quality: str = "standard",
        response_format: str = "url",
    ) -> Dict[str, Any]:
        """
        Generate image from text using Doubao API with direct HTTP request.

        Args:
            prompt: Text prompt for image generation
            model: Model name/version to use
            size: Image size in format "widthxheight"
            seed: Random seed for generation
            guidance_scale: How closely to follow the prompt
            watermark: Whether to add a watermark
            quality: Generation quality ("standard" or "hd")
            response_format: Return format ("url" or "b64_json")

        Returns:
            Dictionary containing the generated image URL or base64 data
        """
        try:
            # 使用直接HTTP请求来支持所有火山引擎特有参数
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            }

            # 准备参数
            data = {
                "model": model,
                "prompt": prompt,
                "size": size,
                "response_format": response_format,
                "quality": quality,
                "n": 1,
                "watermark": watermark,
            }

            # 添加可选参数（如果不是None）
            if seed is not None and seed != -1:
                data["seed"] = seed

            if guidance_scale is not None:
                data["guidance_scale"] = guidance_scale

            # 发送请求
            url = f"{self.base_url}/images/generations"
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()

            result = response.json()

            # 处理返回结果
            if "data" in result and len(result["data"]) > 0:
                if response_format == "url":
                    return {"url": result["data"][0]["url"]}
                else:
                    return {"b64_json": result["data"][0]["b64_json"]}
            else:
                return {"error": {"message": "No image data returned"}}

        except requests.exceptions.RequestException as e:
            return {"error": {"message": f"Request failed: {str(e)}"}}
        except Exception as e:
            return {"error": {"message": str(e)}}

    # 保留旧方法以便兼容性
    def text2image(
        self,
        prompt: str,
        width: int = 1024,
        height: int = 1024,
        seed: int = None,
        scale: float = None,
        use_pre_llm: bool = None,
        return_url: bool = True,
        logo_info: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Legacy method for compatibility"""
        size = f"{width}x{height}"
        response_format = "url" if return_url else "b64_json"

        result = self.generate_image(
            prompt=prompt,
            size=size,
            seed=seed,
            guidance_scale=scale,
            response_format=response_format,
        )

        # 转换为旧格式
        if "url" in result:
            return {
                "code": 10000,
                "data": {
                    "image_urls": [result["url"]],
                    "binary_data_base64": [],
                    "algorithm_base_resp": {
                        "status_code": 0,
                        "status_message": "Success",
                    },
                },
                "message": "Success",
            }
        elif "b64_json" in result:
            return {
                "code": 10000,
                "data": {
                    "image_urls": [],
                    "binary_data_base64": [result["b64_json"]],
                    "algorithm_base_resp": {
                        "status_code": 0,
                        "status_message": "Success",
                    },
                },
                "message": "Success",
            }
        else:
            return {
                "code": 50000,
                "message": result.get("error", {}).get("message", "Unknown error"),
                "data": {},
            }
