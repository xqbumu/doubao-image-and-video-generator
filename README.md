# Doubao Image and Video Generator

A comprehensive AI-powered media generation plugin for Dify, leveraging Volcengine's Doubao API to create images and videos from text prompts or transform images into dynamic videos.

基于火山引擎豆包 API 的全功能 AI 媒体生成 Dify 插件，支持文本生成图像、文本生成视频以及图像转视频功能。

> Disclaimer: This plugin is created by enthusiasts and is not officially maintained by ByteDance.

> 免责声明：该插件由爱好者所创建，并非由字节跳动官方维护。

## Features

This plugin provides three powerful AI generation tools:

本插件提供三大强大的 AI 生成工具：

### 1. 📝 Text to Image
📝 文本生成图像（文生图）

- **High-quality image generation** from text descriptions
- **Multiple aspect ratios**: Square (1024×1024), Portrait (1024×1792), Landscape (1792×1024)
- **Advanced AI model**: Powered by Doubao Seedream 3.0
- **Customizable parameters** for precise control

-**高质量图像生成**：根据文本描述生成精美图片
-**多种尺寸选择**：正方形（1024×1024）、纵向（1024×1792）、横向（1792×1024）
-**先进 AI 模型**：采用豆包 Seedream 3.0
-**参数可定制**：精确控制生成效果

### 2. 🎬 Text to Video

🎬 文本生成视频（文生视频）

- **Video creation** from text prompts
- **Flexible aspect ratios**: 16:9, 9:16, 4:3, 1:1
- **Duration options**: 5 or 10 seconds
- **Multiple models**: `doubao-seedance-1-0-lite-t2v-250428`
- **Professional video output** for various use cases

-**视频创作**：从文本提示词生成动态视频
-**灵活宽高比**：16:9、9:16、4:3、1:1 多种选择
-**时长可选**：支持 5 秒或 10 秒视频
-**模型支持** `doubao-seedance-1-0-lite-t2v-250428`
-**专业输出**：适用于各种使用场景

### 3. 🖼️ Image to Video
🖼️ 图像生成视频（图生视频）

- **Transform static images** into dynamic videos
- **Smart animation** guided by text prompts
- **Adaptive aspect ratio** support
- **Seamless integration** with existing images
- **Configurable duration** up to 10 seconds

-**静态转动态**：将静态图片转换为动态视频
-**智能动画**：根据文本提示引导动画效果
-**自适应比例**：支持自动适配最佳宽高比
-**无缝集成**：与现有图片完美结合
-**时长可配**：最长支持 10 秒视频

## 🚀 Quick Start

### Prerequisites
- Dify platform access
- Volcengine account with Visual Services enabled

- Dify 平台访问权限
- 火山引擎账户并开通智能视觉服务

### Step 1: Get Your API Key
1. Visit the [Volcengine Console](https://console.volcengine.com/home).

1. 访问 [火山引擎控制台](https://console.volcengine.com/home)

> Test API Key: `719f1aec-26af-4bac-b1df-1fc26a95df73`

> 测试 API Key：`719f1aec-26af-4bac-b1df-1fc26a95df73`

2. Create an account or sign in
3. Navigate to Visual Services and enable the required APIs
4. Generate your API Key from the dashboard

2. 创建账户或登录现有账户
3. 前往智能视觉服务并启用相关 API
4. 在控制台生成您的 API 密钥

### Step 2: Install the Plugin
步骤 2：安装插件

1. Open Dify's Plugin Marketplace
2. Search for "Doubao Image and Video Generator"
3. Click "Install" and wait for the installation to complete

1. 打开 Dify 插件市场
2. 搜索 "豆包图像视频生成器"
3. 点击 "安装" 并等待安装完成

### Step 3: Configure Authorization
配置授权

1. In Dify, navigate to `Tools > Doubao Generator > Authorize`
2. Enter your Volcengine API Key
3. Save the configuration

1. 在 Dify 中，导航至 `工具 > 豆包生成器 > 授权`
2. 输入您的火山引擎 API 密钥
3. 保存配置

![Configuration Example](./_assets/doubao-1.png)

### Step 4: Start Creating
开始创作

The plugin is now ready to use in your Dify applications!

插件现已准备就绪，可在您的 Dify 应用中使用！

![Application Types](./_assets/doubao-2.png)

## 📋 Usage Examples

📋 使用示例

### In Workflow Applications

在工作流应用使用

- **Batch content creation**: Generate multiple images/videos in sequence
- **Content pipeline**: Combine text→image→video transformations
- **Quality control**: Set consistent parameters across generations

-**批量内容创建**：按序列生成多个图像 / 视频
-**内容管道**：组合文本→图像→视频的转换流程
-**质量控制**：在生成过程中设置一致的参数

### In Agent Applications
在 Agent 应用内使用

- **Intelligent decisions**: Agent automatically chooses the right generation tool
- **Context-aware creation**: Adapts generation based on conversation flow
- **Multi-modal responses**: Combines text, images, and videos seamlessly

-**智能决策**：智能体自动选择合适的生成工具
-**上下文感知**：根据对话流程调整生成策略
-**多模态响应**：无缝结合文本、图像和视频

## ⚙️ Technical Specifications
⚙️ 技术规格

### Supported Models
支持的模型

- **Image Generation**: Doubao Seedream 3.0 (`doubao-seedream-3-0-t2i-250415`)
- **Video Generation**: 
  - Doubao Seedance 1.0 Lite (`doubao-seedance-1-0-lite-t2v-250428`)
  - Doubao Seaweed (`doubao-seaweed-241128`)

-**图像生成**：豆包 Seedream 3.0（`doubao-seedream-3-0-t2i-250415`）
-**视频生成**：
  - 豆包 Seedance 1.0 Lite（`doubao-seedance-1-0-lite-t2v-250428`）

### Output Formats

输出格式

- **Images**: High-resolution PNG/JPEG
- **Videos**: MP4 format with configurable duration

-**图像**：高分辨率 PNG/JPEG 格式
-**视频**：MP4 格式

### Performance
性能表现

- **Text to Image**: ~5-15 seconds generation time
- **Text to Video**: ~30-90 seconds generation time  
- **Image to Video**: ~20-60 seconds generation time

-**文生图**：约 5-15 秒生成时间
-**文生视频**：约 30-90 秒生成时间
-**图生视频**：约 20-60 秒生成时间

## 🎯 Best Practices

### Prompt Engineering
提示词工程

- **Be specific**: Include details about style, lighting, composition
- **Use descriptive adjectives**: "vibrant colors", "soft lighting", "cinematic"
- **Specify the mood**: "peaceful", "dramatic", "whimsical"

-**具体描述**：包含风格、光照、构图等细节
-**使用形容词**：如 "鲜艳色彩"、"柔和光线"、"电影感"
-**指定情绪**：如 "宁静"、"戏剧性"、"奇幻"

### Example Prompts
示例提示词

Text to Image: "A majestic snow-covered mountain peak at sunrise, with golden light reflecting on a pristine alpine lake, photorealistic style"

Text to Video: "Gentle ocean waves washing onto a sandy beach at sunset, with seagulls flying overhead, peaceful and serene"

Image to Video: "Add subtle movement to this landscape - swaying trees, flowing water, and drifting clouds"

文生图："雪山之巅的日出美景，金光洒在原始的高山湖泊上，照片级真实风格"

文生视频："夕阳时分，温柔的海浪拍打着沙滩，海鸥在上空飞翔，宁静祥和的氛围"

图生视频："为这个风景添加微妙的动感 - 树叶摇摆、流水潺潺、云朵飘移"

## 🔧 Troubleshooting

🔧 故障排除

### Common Issues

常见问题

- **API Key Invalid**: Verify your Volcengine API key and service permissions
- **Generation Failed**: Check if your prompt complies with content policies
- **Slow Response**: Peak hours may cause delays; consider retrying later
- **Model Not Found**: Ensure you're using the correct model identifiers

-**API 密钥无效**：请验证火山引擎 API 密钥和服务权限
-**生成失败**：检查提示词是否符合内容政策
-**响应缓慢**：高峰期可能出现延迟，请稍后重试
-**模型未找到**：确保使用正确的模型标识符

### Error Codes
错误代码
- `401`: Authentication failed - check your API key
- `429`: Rate limit exceeded - wait before retrying
- `500`: Server error - contact Volcengine support

- `401`：认证失败 - 检查 API 密钥
- `429`：频率限制 - 请等待后重试
- `500`：服务器错误 - 联系火山引擎技术支持

## 📚 Resources

- [Volcengine Documentation](https://www.volcengine.com/docs/85128/1526761)
- [Dify Plugin Development Guide](https://docs.dify.ai/plugins)
- [Doubao API Reference](https://console.volcengine.com/docs)

## 🤝 Contributing

We welcome contributions! Please feel free to:
- Report bugs and issues
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

📄 许可证

This project is licensed under the terms specified in the LICENSE file.

本项目遵循 LICENSE 文件中指定的许可条款。

---

**Transform your ideas into stunning visuals with the power of AI** ✨

*Built with by Mak J AI Limited*

**用 AI 的力量将创意转化为精彩视觉** ✨

* 由 Mak J AI Limited 构建*
