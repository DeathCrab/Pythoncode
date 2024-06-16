[app]

# (str) Title of your application
title = Your App Title

# (str) Package name
package.name = yourpackagename

# (str) Package domain (needed for android/ios packaging)
package.domain = org.yourdomain

# (str) Source code where the main.py live
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy,numpy,plyer,buildozer

# (str) Icon of the application
icon.filename = path/to/your/icon.png

# (str) Application versioning
version = 1.0.0

# (list) Python for android packages
android.p4a_whitelist = numpy, kivy

# (list) Android additional parameters
android.permissions = INTERNET

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (str) iOS entry point
ios.entry_point = kivy_main.py

# (bool) Indicate whether the application should be fullscreen
fullscreen = 0

# (list) List of service to declare
services =


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
