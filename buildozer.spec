[app]

# (str) Title of your application
title = Password Generator

# (str) Package name
package.name = passwordgenerator

# (str) Package domain
package.domain = org.saransh

# (str) Source code directory
source.dir = .

# (list) Source file extensions to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 1.0

# (list) Application requirements
requirements = python3,kivymd,kivy,pillow

# (list) Supported orientations
orientation = portrait

# (bool) Application fullscreen
fullscreen = 0

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version
android.sdk = 33

# (str) Android NDK version
android.ndk = 25b

# (int) Android NDK API level
android.ndk_api = 21

# (bool) Automatically accept SDK license agreements
android.accept_sdk_license = True

# (list) Architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable backup
android.allow_backup = True

# (str) Debug build artifact format
android.debug_artifact = apk

# (str) Release build artifact format
android.release_artifact = aab

# (bool) Copy libs instead of making libpymodules.so
android.copy_libs = 1

# (str) Logcat filter
android.logcat_filters = *:S python:D

[buildozer]

# (int) Log level (0=error only, 1=info, 2=debug)
log_level = 2

# (int) Warn if run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Build artifact storage directory
build_dir = ./.buildozer

# (str) Output APK/AAB storage directory
bin_dir = ./bin
