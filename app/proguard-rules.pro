# ============================================================
# 提词器 App - ProGuard / R8 混淆规则
# ============================================================

# 基本优化
-optimizationpasses 5
-dontusemixedcaseclassnames
-dontskipnonpubliclibraryclasses
-verbose

# 保持应用主类（Activity/Service等需要在Manifest中注册的类）
-keep public class com.teleprompter.app.MainActivity { *; }
-keep public class com.teleprompter.app.CameraHelper { *; }

# 保持R类和BuildConfig
-keepclassmembers class com.teleprompter.app.R$* { *; }
-keep class com.teleprompter.app.BuildConfig { *; }

# 保持View相关（XML引用的onClick等）
-keepclassmembers class * {
    public void on*Click(android.view.View);
}

# 保持Serializable
-keepclassmembers class * implements java.io.Serializable {
    static final long serialVersionUID;
    private static final java.io.ObjectStreamField[] serialPersistentFields;
    !static !transient <fields>;
    private void writeObject(java.io.ObjectOutputStream);
    private void readObject(java.io.ObjectInputStream);
    java.lang.Object writeReplace();
    java.lang.Object readResolve();
}

# 保持Parcelable
-keepclassmembers class * implements android.os.Parcelable {
    public static final ** CREATOR;
}

# 保持枚举
-keepclassmembers enum * {
    public static **[] values();
    public static ** valueOf(java.lang.String);
}

# Kotlin反射支持
-dontwarn kotlin.**
-keep class kotlin.Metadata { *; }
-keepclassmembers class **$WhenMappings {
    <fields>;
}
-keepclassmembers class kotlin.Metadata {
    public <methods>;
}

# AndroidX / Jetpack
-keep class androidx.** { *; }
-keep interface androidx.** { *; }
-dontwarn androidx.**

# Material Components
-keep class com.google.android.material.** { *; }
-dontwarn com.google.android.material.**

# 移除日志（Release构建不输出Log.d/Log.v）
-assumenosideeffects class android.util.Log {
    public static *** d(...);
    public static *** v(...);
    public static *** i(...);
}

# 防止反编译关键逻辑
-repackageclasses ''
-allowaccessmodification