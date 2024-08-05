plugins {
    id("java-library")
    id("java-gradle-plugin")
    alias(libs.plugins.jetbrainsKotlinJvm)
    id("maven-publish")
}

java {
    sourceCompatibility = JavaVersion.VERSION_17
    targetCompatibility = JavaVersion.VERSION_17
}

object RepoConfig {
    const val group = "com.fan.plugin"
    const val version = "1.1.0"
    const val artifactId = "guard"
}

gradlePlugin {
    plugins {
        create("AabResGuard-Plugin") {
            id = "aab-res-guard" //插件的唯一标识，使用插件的时候就是这个id
            implementationClass = "com.bytedance.android.plugin.AabResGuardPlugin"
        }
    }
}

publishing {
    publications {
        create<MavenPublication>("maven") {
            from(components["java"])
            artifactId = RepoConfig.artifactId
            groupId = RepoConfig.group
            version = RepoConfig.version
        }
    }
    repositories {
        maven {
            url = uri("../localRepo") //本地maven地址
        }
    }
}

dependencies {
    implementation("com.android.tools.build:gradle:8.1.2")
    api(project(":core"))
}

