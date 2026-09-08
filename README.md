# 🎬 Short Video Teleprompter

Android front-camera recording + teleprompter all-in-one app. The essential tool for content creators.

📥 **[Download Latest Release](https://github.com/fuzhuangxiehui/TeleprompterApp/releases/latest)** | 🌐 **[Homepage](https://fuzhuangxiehui.github.io/TeleprompterApp/)** | 📋 **[Privacy Policy](https://fuzhuangxiehui.github.io/TeleprompterApp/privacy.html)** | 🇨🇳 [中文说明](#中文说明)

## ✨ Features

- **1080P Front Camera Recording** — Clean video output without any teleprompter text overlay
- **Transparent Teleprompter Overlay** — Semi-transparent text floats near the front camera, so your eyes look natural while reading
- **Wide-Angle Distortion Correction** — Default 1.4x digital zoom reduces barrel distortion; adjustable 1.0x–3.0x
- **Auto-Scrolling** — Adjustable speed with play/pause/restart controls
- **Font Size Adjustment** — 12sp to 40sp
- **Transparency Control** — 20%–100% to suit any lighting condition
- **Paste from Clipboard** — Copy your script from any app and paste it in
- **Recording Timer** — Real-time recording duration display
- **Auto-Hide Controls** — Controls fade out 3 seconds after recording starts; tap anywhere to bring them back
- **🔒 Zero Data Collection** — No data collected, no ads, no tracking

## 📥 Installation

1. Download the APK from [Releases](https://github.com/fuzhuangxiehui/TeleprompterApp/releases/latest)
2. Enable "Install from unknown sources" in your phone settings
3. Tap the APK to install

## 📱 Requirements

- Android 7.0 (API 24) or above
- Front-facing camera
- ~3.5MB storage

## 🔧 Tech Stack

- **Language**: Kotlin
- **Min SDK**: Android 7.0 (API 24)
- **Target SDK**: Android 14 (API 34)
- **Core**: Camera2 API + MediaRecorder
- **Build**: Gradle 8.5 + R8 obfuscation

## 🔄 Changelog

### v1.0.0 (2026-09-07)
- Initial release
- 1080P front camera recording with transparent teleprompter overlay
- Wide-angle distortion correction (1.4x default zoom)
- Privacy policy consent dialog
- ProGuard obfuscation

## 📦 Building from Source

```bash
# 1. Generate signing key (first time only)
keytool -genkeypair -v \
  -keystore release/teleprompter_release.jks \
  -keyalg RSA -keysize 2048 -validity 10000 \
  -alias teleprompter

# 2. Fill in signing config
# Edit release/signing.properties

# 3. Build signed APK
cd app && ../gradlew assembleRelease

# Output: app/build/outputs/apk/release/app-release.apk
```

## 🔒 Privacy

This app does not collect, upload, or share any user data. See [Privacy Policy](release/privacy_policy.html) for details.

## 📄 License

© 2026 Teleprompter App. All rights reserved.

---

<a id="中文说明"></a>
## 中文说明

**短视频提词器** — Android前置摄像头录制+提词器一体化App，自媒体口播神器。

### 功能亮点
- 📹 前置摄像头1080P高清录制（纯净视频，无提词文字叠加）
- 📝 半透明提词文字悬浮在屏幕上方（靠近前摄像头，眼神更自然）
- 🔍 广角畸变校正（默认1.4x数字变焦，可调1.0x-3.0x）
- ⚙️ 字体大小/透明度/滚动速度可调
- ⏱️ 录制计时、控制栏自动隐藏
- 🔒 零数据收集、无广告无追踪

📥 [下载APK](https://github.com/fuzhuangxiehui/TeleprompterApp/releases/latest) | 📋 [隐私政策](https://fuzhuangxiehui.github.io/TeleprompterApp/privacy.html)