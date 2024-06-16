[app]

# (str) Title of your application
title = UncertaintyApp

# (str) Package name
package.name = uncertaintyapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (comma-separated)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy,numpy,plyer

# (str) Icon of the application
icon.filename = path/to/your/icon.png

# (str) Presplash of the application
presplash.filename = path/to/your/presplash.png

# (str) Application versioning
version = 1.0.0

# (list) Permissions
android.permissions = INTERNET

# (int) Window size
window.size = 360, 640

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or sensorPortrait)
orientation = portrait

# (list) List of service to declare
services =

# (list) Android whitelist (whitelist specific modules from being removed)
android.whitelist = numpy,kivy

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (bool) Indicate whether the application should be fullscreen
fullscreen = 0

# (list) Intent filters
# android.manifest.intent_filters =

# (list) Android additional libraries to copy into libs/armeabi
android.add_libs_armeabi = libs/armeabi-v7a/libpython3.8.so

# (str) Path to Android NDK
# android.ndk_path =

# (str) Path to Android SDK
# android.sdk_path =

# (str) Android NDK version to use
# android.ndk = 21b

# (str) Android SDK version to use
# android.sdk = 28

# (str) Android logcat filters
# android.logcat_filters = *:S python:D

# (str) Android version_code (integer)
# android.version_code = 1

# (str) Android version_code_suffix (string)
# android.version_code_suffix = .1

# (str) Android NDK API (integer)
# android.ndk_api = 21

# (str) Android Min API (integer)
# android.minapi = 19

# (str) Android build tools version
# android.build_tools_version = 28.0.3

# (str) iOS entry point
ios.entry_point = kivy_main.py


[buildozer]

# (bool) Enable logging to a file
log_enable = 1

# (str) Log file name
log_filename = buildozer.log

# (bool) Warn on root
warn_on_root = 1
