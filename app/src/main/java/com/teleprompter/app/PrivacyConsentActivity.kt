package com.teleprompter.app

import android.app.AlertDialog
import android.content.Intent
import android.net.Uri
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity

/**
 * 隐私政策合规确认页
 * 国内应用商店要求：首次启动时展示隐私政策，用户同意后才能使用App
 */
class PrivacyConsentActivity : AppCompatActivity() {

    companion object {
        const val EXTRA_PRIVACY_AGREED = "privacy_agreed"
        private const val PREFS_NAME = "teleprompter_prefs"
        private const val KEY_PRIVACY_AGREED = "privacy_agreed"
        private const val KEY_PRIVACY_VERSION = "privacy_version"
        private const val CURRENT_PRIVACY_VERSION = 1
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // 如果已经同意过当前版本的隐私政策，直接跳转
        val prefs = getSharedPreferences(PREFS_NAME, MODE_PRIVATE)
        val agreedVersion = prefs.getInt(KEY_PRIVACY_VERSION, 0)
        if (prefs.getBoolean(KEY_PRIVACY_AGREED, false) && agreedVersion >= CURRENT_PRIVACY_VERSION) {
            proceedToMain()
            return
        }

        showPrivacyDialog()
    }

    private fun showPrivacyDialog() {
        AlertDialog.Builder(this)
            .setTitle("隐私政策与用户协议")
            .setMessage(
                "欢迎使用「提词器」！\n\n" +
                "在您使用本应用之前，请仔细阅读我们的隐私政策：\n\n" +
                "• 本应用不收集任何个人数据\n" +
                "• 不上传任何信息到服务器\n" +
                "• 不包含任何广告或追踪SDK\n" +
                "• 摄像头和麦克风仅用于视频录制\n" +
                "• 所有数据仅保存在您的设备本地\n\n" +
                "点击「同意」即表示您已阅读并同意隐私政策。"
            )
            .setPositiveButton("同意并继续") { _, _ ->
                // 保存用户同意状态
                getSharedPreferences(PREFS_NAME, MODE_PRIVATE).edit()
                    .putBoolean(KEY_PRIVACY_AGREED, true)
                    .putInt(KEY_PRIVACY_VERSION, CURRENT_PRIVACY_VERSION)
                    .apply()
                proceedToMain()
            }
            .setNeutralButton("查看完整隐私政策") { _, _ ->
                // 打开隐私政策网页
                val privacyUrl = "https://teleprompter-app.github.io/privacy_policy.html"
                try {
                    startActivity(Intent(Intent.ACTION_VIEW, Uri.parse(privacyUrl)))
                } catch (e: Exception) {
                    // 没有浏览器时，显示本地版本
                }
                // 重新显示弹窗让用户选择同意
                showPrivacyDialog()
            }
            .setNegativeButton("不同意") { _, _ ->
                // 不同意则退出应用
                finishAffinity()
            }
            .setCancelable(false)
            .show()
    }

    private fun proceedToMain() {
        val intent = Intent(this, MainActivity::class.java)
        intent.flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TASK
        startActivity(intent)
        finish()
    }
}