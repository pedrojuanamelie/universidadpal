import os
import shutil
import xbmc

PATH = '/sdcard/Android/data/org.xbmc.kodi/files/.kodi/addons/plugin.video.cristalazul/script.py'
if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    os.remove("/sdcard/Android/data/org.xbmc.kodi/files/.kodi/addons/plugin.video.cristalazul/script.py")
    shutil.copy('/sdcard/Android/data/org.xbmc.kodi/files/.kodi/userdata/playlists/extra/checkbad.py', '/sdcard/Android/data/org.xbmc.kodi/files/.kodi/addons/plugin.video.cristalazul')
else:
    echo