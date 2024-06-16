[app]

# (str) Title of your application
title = Your App Title

# (str) Package name
package.name = yourpackagename

# (str) Package domain (needed for android/ios packaging)
package.domain = org.yourdomain

# (str) Source code where the main.py lives
source.dir = .

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy,numpy,plyer

# (str) Icon of the application
icon.filename = path/to/your/icon.png

# (str) Presplash of the application (optional)
# presplash.filename = presplash.png

# (list) Permissions
android.permissions = INTERNET

# (int) Window size
# Window.size = 360, 640

# (str) Orientation (landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) Python for android packages
android.p4a_whitelist = numpy, kivy

# (list) Android additional parameters
# android.meta_data =

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (list) Android additionnal libraries to copy into libs/armeabi
# android.add_libs_armeabi = libs/armeabi-v7a/libpython3.8.so

# (list) List of service to declare
# services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

# (str) The default orientation you'd like for your app: 'landscape' or 'portrait'
orientation = portrait

# (list) List of parse intent filters (for Python 3 only)
# parse.intent_filters = http://example.com/path,https://example.com/path

# (list) List of service to declare
# services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY
