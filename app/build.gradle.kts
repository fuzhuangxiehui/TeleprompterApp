import java.util.Properties

plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

// Load signing properties if available
val signingPropsFile = rootProject.file("release/signing.properties")
val signingProps = Properties()
if (signingPropsFile.exists()) {
    signingProps.load(signingPropsFile.inputStream())
}

android {
    namespace = "com.teleprompter.app"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.teleprompter.app"
        minSdk = 24
        targetSdk = 34
        versionCode = 1
        versionName = "1.0.0"
    }

    signingConfigs {
        create("release") {
            if (signingPropsFile.exists() && signingProps.containsKey("STORE_PASSWORD")) {
                storeFile = file("../release/${signingProps.getProperty("STORE_FILE")}")
                storePassword = signingProps.getProperty("STORE_PASSWORD") ?: ""
                keyAlias = signingProps.getProperty("KEY_ALIAS") ?: ""
                keyPassword = signingProps.getProperty("KEY_PASSWORD") ?: ""
            }
        }
    }

    buildTypes {
        debug {
            isMinifyEnabled = false
            isShrinkResources = false
        }
        release {
            isMinifyEnabled = true
            isShrinkResources = true
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
            if (signingPropsFile.exists() && signingProps.containsKey("STORE_PASSWORD")) {
                signingConfig = signingConfigs.getByName("release")
            }
        }
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_1_8
        targetCompatibility = JavaVersion.VERSION_1_8
    }

    kotlinOptions {
        jvmTarget = "1.8"
    }
}

dependencies {
    implementation("androidx.core:core-ktx:1.12.0")
    implementation("androidx.appcompat:appcompat:1.6.1")
    implementation("com.google.android.material:material:1.11.0")
    implementation("androidx.constraintlayout:constraintlayout:2.1.4")
}