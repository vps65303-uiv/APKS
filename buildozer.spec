# (str) Application requirements
# (comma separated)
requirements = python3,requests
[app]
title = Shellndrod
package.name = shellndrod
package.domain = org.shellndrod
source.include_exts = py,png,jpg,kv,atlas
source.dir = .
version = 1.0
requirements = python3,requests
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.ndk_api = 21
