plugins {
    id("java-library")
    id("kotlin-kapt")
    alias(libs.plugins.jetbrainsKotlinJvm)
}

java {
    sourceCompatibility = JavaVersion.VERSION_17
    targetCompatibility = JavaVersion.VERSION_17
}

dependencies{
    compileOnly(gradleApi())
    implementation("com.android.tools.build:bundletool:0.13.3")
    implementation("com.google.guava:guava:30.0-jre")
    implementation("commons-io:commons-io:2.7")
    implementation("commons-codec:commons-codec:1.5")
    kapt("com.google.auto.value:auto-value:1.5.2")
    implementation("com.google.auto.value:auto-value:1.5.2")
    compileOnly("com.android.tools.build:aapt2-proto:0.4.0")
    implementation("com.android.support:support-annotations:24.2.0")
    implementation("org.dom4j:dom4j:2.1.1")
}