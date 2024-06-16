[app]

# (str) Title of your application
title = UncertaintyApp

# (str) Package name
package.name = uncertaintyapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.uncertaintyapp

# (str) Human readable version of the application
version = 1.0.0

# (int) Numeric version of the application
version.code = 1

# (str) Application icon (used if you are using the launcher)
icon.filename = icon.png

# (list) Application permissions
android.permissions = INTERNET

# (bool) Indicate whether the application should be fullscreen or not
fullscreen = 0

# (str) Presplash of the application
presplash.filename = presplash.png

# (str) Icon of the application
icon.filename = icon.png

# (list) Permissions
android.permissions = INTERNET

# (int) Window size
Window.size = 360, 640

# (str) Orientation (landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
# services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

# (str) The default orientation you'd like for your app: 'landscape' or 'portrait'
orientation = portrait

# (list) List of parse intent filters (for Python 3 only)
# parse.intent_filters = http://example.com/path,https://example.com/path

# (list) Android additionnal libraries to copy into libs/armeabi
android.add_libs_armeabi = libs/armeabi-v7a/libpython3.8.so

# (list) Python for android packages
# Comma-separated list of python packages to be included in the app
# Make sure these packages are compatible with Kivy and Android
# You may need to adjust versions or dependencies based on your app's requirements
# Here we include numpy and kivy, as well as other dependencies like plyer and buildozer itself
# Ensure to install any other dependencies your app requires for proper functionality on Android
# Separate multiple packages with commas
# Example: numpy, kivy, plyer, buildozer
requirements = python3,kivy,numpy,plyer,buildozer

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or sensorPortrait)
orientation = portrait

# (list) List of service to declare
services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY
# (list) List of service to declare
services =

# (list) List of source files and their inclusion in the APK
source.include_exts = py,png,jpg,kv,atlas

# (str) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
# requirements = python3,kivy,numpy,plyer,buildozer

# (list) Python for android packages
# Change comma to the spacebar if want to add only python packages.
# Change comma to the spacebar if want to add only python packages.
numpy, kivy
