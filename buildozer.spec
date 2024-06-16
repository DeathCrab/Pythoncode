[app]

# (str) Title of your application
title = UncertaintyApp

# (str) Package name
package.name = uncertaintyapp

# (str) Package domain (needed for Android/IOS packaging)
package.domain = org.kivy

# (str) Source code where the main.py file is located
source.dir = .

# (list) Source files to include (and their patterns) that are not in the .py file. This supports wildcards
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = assets/*,images/*.png

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,numpy

# (str) Custom source folders for requirements
# (advanced) Separated by a comma
# e.g. source.include_dirs =

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate whether the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE

# (str) Application versioning (method 1)
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py

# (str) Application versioning (method 2)
#version = 1.2.0

# (list) Application meta-data (key=value format)
#android.meta_data =

# (str) Service to launch (like wakelock)
#android.service =

# (str) Primary python-for-android git repository to use
#p4a.url =

# (str) Secondary python-for-android fork to use
#p4a.fork =

# (str) The URL for the main Python source code
#web2py.url =

# (str) The URL for the secondary fork source code
#web2py.fork =

# (list) Application specific (local) custom android permissions
#android.permissions =

# (bool) If False, the application won't be able to run on x86 Android devices
#android.arch = armeabi-v7a

# (str) launch modes for Android. Options are: standard, singleTop, singleTask, singleInstance
#android.launchMode = standard

# (bool) Indicate whether the screen should stay on
#android.keepScreenOn = True

# (str) Android API to use
#android.api = 27

# (int) Minimum API required
#android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 27

# (str) Android NDK version to use
#android.ndk = 21.1.6352462

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (bool) Android antialiasing
#android.antialias = False

# (bool) Enable Logcat logging
#android.logcat = False

# (bool) Uses old expandtab that converts tabs to spaces
#android.old_expandtab = False

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.renpy.android.PythonActivity

# (str) Android app theme, default is ok for Kivy-based app
#android.apptheme = @android:style/Theme.NoTitleBar

# (bool) Enable Android M permissions request
#android.permissions_ensure = False

# (str) iOS project bundle identifier
#ios.bundleid = org.test

# (str) iOS project title
#ios.title = UncertaintyApp

# (str) iOS project description
#ios.description = Uncertainty Calculation App

# (list) iOS frameworks to link against (this is addition to the default ones)
#ios.frameworks =

# (int) Icon width (in pixels)
#icon.width = 57

# (int) Icon height (in pixels)
#icon.height = 57

# (str) iOS supported orientations
#ios.orientations = Portrait

# (str) iOS deployment target
#ios.ios_deployment_target =

# (str) Android gradle dependencies exclusions
#android.gradle_dependencies_exclusions = com.google.android.material:material

# (bool) Log compilation comands
#log_commands = False

# (str) macOS application bundle id
#macos.bundleid = org.test

# (str) macOS application title
#macos.title = UncertaintyApp

# (str) macOS developer id
#macos.developerid =

# (str) macOS minimum system version to deploy
#macos.min_os_version = 10.13

# (bool) Use the --private option with buildozer
#private =

# (str) macOS resources path
#macos.resources =

# (bool) Enable use of --use_color option
#use_color = True

# (str) macOS icon filename
#macos.icon =

# (str) macOS icon file type
#macos.icon_type =

# (str) Kivy version to use
#kivy_version = 2.1.0

