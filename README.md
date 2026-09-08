# 🎬 短视频提词器

Android前置摄像头录制+提词器一体化App，自媒体口播神器。

📥 **[下载最新版本](https://github.com/fuzhuangxiehui/TeleprompterApp/releases/latest)** | 🌐 **[官网](https://fuzhuangxiehui.github.io/TeleprompterApp/)** | 📋 **[隐私政策](https://fuzhuangxiehui.github.io/TeleprompterApp/privacy.html)**

## ✨ 功能

- **前置摄像头高清录制** — 1080P录制，录制视频纯净无提词文字
- **透明提词器悬浮** — 文字半透明悬浮在屏幕上方，靠近前摄像头，看词时眼神更自然
- **广角畸变校正** — 默认1.4x变焦减小前置广角畸变，可调1.0x-3.0x
- **自动滚动** — 可调速度，播放/暂停/回到顶部
- **字体大小调节** — 12sp ~ 40sp
- **透明度调节** — 20%-100%，适应不同场景
- **文字粘贴** — 支持从其他App复制粘贴提词内容
- **录制计时** — 实时显示录制时长
- **自动隐藏控制栏** — 录制开始3秒后自动隐藏，轻触屏幕重新显示
- **🔒 零数据收集** — 不收集任何个人数据，无广告无追踪

## 🔄 版本历史

### v1.0.0 (2026-09-07)
- 首次发布
- 前置摄像头1080P录制 + 半透明提词悬浮
- 广角畸变校正（1.4x默认变焦）
- 隐私政策合规弹窗
- ProGuard混淆保护

## 🔧 技术栈

- **语言**：Kotlin
- **最低SDK**：Android 7.0 (API 24)
- **目标SDK**：Android 14 (API 34)
- **架构**：Camera2 API + MediaRecorder
- **构建**：Gradle 8.5 + R8混淆

## 📦 构建发布版

```bash
# 1. 生成签名密钥（首次）
keytool -genkeypair -v \
  -keystore release/teleprompter_release.jks \
  -keyalg RSA -keysize 2048 -validity 10000 \
  -alias teleprompter

# 2. 填写签名密码
# 编辑 release/signing.properties

# 3. 构建签名APK
cd app && ../gradlew assembleRelease

# 输出: app/build/outputs/apk/release/app-release.apk
```

## 📋 发布准备

详见 `release/RELEASE_CHECKLIST.md`

包含：
- ProGuard混淆配置 ✅
- 隐私政策页面 ✅
- 权限合规弹窗 ✅
- 签名密钥配置 ✅
- 软著源代码提取工具 ✅
- 应用素材清单（图标/截图/描述）
- 各渠道上架要求对比

## 🔒 隐私

本应用不收集、不上传、不分享任何用户数据。详见 `release/privacy_policy.html`

## 📄 许可

© 2026 提词器 App. 保留所有权利。