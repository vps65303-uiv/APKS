[app]

# (str) Title of your application
title = Shellndrod

# (str) Package name
package.name = shellndrod

# (str) Package domain (needed for android packaging)
package.domain = org.shellndrod

# (str) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to include (let it empty to include all files)
source.dir = .

# (str) Application versioning
version = 1.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,requests

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Indicate whether the application should be fullscreen or not
fullscreen = 0

# (string) python-for-android branch to use
p4a.branch = master

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if run as root (0 = False, 1 = True)
warn_on_root = 1
