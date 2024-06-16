[app]

# (str) Title of your application
title = UncertaintyApp

# (str) Package name
package.name = uncertaintyapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py lives
source.dir = .

# (list) Application requirements
requirements = python3,kivy,numpy,plyer,pytest-runner

# (str) Icon of the application
icon.filename = path/to/your/icon.png

# (str) Application versioning
version = 1.0.0

# (list) Python for android packages
android.p4a_whitelist = numpy, kivy

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (bool) Indicate whether the application should be fullscreen
fullscreen = 0

# (int) Window size
Window.size = 360, 640

# (str) Orientation (landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
services =

# (list) List of source files and their inclusion in the APK
source.include_exts = py,png,jpg,kv,atlas
