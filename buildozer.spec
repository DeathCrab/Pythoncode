[app]

# (str) Title of your application
title = UncertaintyApp

# (str) Package name
package.name = uncertaintyapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (list) Application requirements
requirements = python3,kivy,numpy

# (str) Icon of the application
icon.filename = icon.png

# (str) Source code directory (relative to this directory)
source.dir = .

# (str) Main entry point of the application (relative to source directory)
source.include_exts = py,png,jpg,kv,atlas
source.exclude_exts = spec, txt
source.exclude_dirs = tests, .git, __pycache__

# (list) List of service to declare
services = NAME-OF-YOUR-SERVICE
