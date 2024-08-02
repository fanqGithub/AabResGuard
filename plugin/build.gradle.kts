plugins {
    id("java-library")
    id("java-gradle-plugin")
    alias(libs.plugins.jetbrainsKotlinJvm)
    id("maven-publish")
}

java {
    sourceCompatibility = JavaVersion.VERSION_11
    targetCompatibility = JavaVersion.VERSION_11
}

gradlePlugin {
    plugins {
        create("AabResGuard-Plugin") {
            group = "com.fan.plugin"
            version = "1.1.0"
            id = "aab-res-guard" //插件的唯一标识，使用插件的时候就是这个id
            implementationClass = "com.znh.plugin.page.PageAnalysisPlugin" //PageAnalysisPlugin的全类名 取代resources声明
        }
    }
}

publishing {
    repositories {
        maven {
            url = uri("../localRepo") //本地maven地址
        }
    }
}

dependencies {
    implementation("com.android.tools.build:gradle:8.1.2")
}

