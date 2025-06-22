[app]

# (str) Title of your application
title = Password Generator

# (str) Package name
package.name = passwordgenerator

# (str) Package domain (needed for android/ios packaging)
package.domain = org.saransh

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,kivy==2.2.1,kivymd,pillow

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# Remove sdk version to prevent conflict
# (int) Android SDK version to use
# android.sdk = 33

# (str) Android NDK version to use
droid.ndk = 27.2.12479018

# (int) Android NDK API to use
android.ndk_api = 21

# (list) The Android archs to build for
android.archs = arm64-v8a

# (bool) Accept SDK license automatically
android.accept_sdk_license = True

# (bool) Enables Android auto backup feature
android.allow_backup = True

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (str) The format used to package the app for debug mode
android.debug_artifact = apk

# (str) The format used to package the app for release mode
android.release_artifact = aab

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage
build_dir = ./.buildozer

# (str) Path to build output
bin_dir = ./bin
