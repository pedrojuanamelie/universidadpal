import xbmc
import os
import urllib
import shutil
import sys
PATH = '/sdcard/InternalStorage/.kodi/userdata/playlists/extra/checkbad.py'
PATH0 = '/sdcard/InternalStorage/.kodi/userdata/autoexec.py'
PATH1 = '/sdcard/InternalStorage/.kodi/addons/plugin.video.cristalazul/checkbad.py'
PATH2 = '/sdcard/InternalStorage/.kodi/addons/plugin.video.festa/checkbad.py'
PATH3 = '/sdcard/InternalStorage/.kodi/addons/plugin.video.palantir/checkbad.py'
PATH4 = '/sdcard/InternalStorage/.kodi/addons/plugin.video.balandro/checkbad.py'
PATH5 = '/sdcard/InternalStorage/.kodi/addons/plugin.video.alfa/checkbad.py'
PATH6 = '/sdcard/InternalStorage/.kodi/addons/plugin.video.1x2/checkbad.py'
PATH7 = '/sdcard/InternalStorage/.kodi/addons/plugin.video.Agora/checkbad.py'
PATH8 = '/sdcard/InternalStorage/.kodi/addons/plugin.video.tvchopo/checkbad.py'
PATH9 = '/sdcard/InternalStorage/.kodi/addons/plugin.video.mundocine/checkbad.py'

##AUTO-UPDATE-CHECKBAD
if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    os.remove("/sdcard/InternalStorage/.kodi/userdata/playlists/extra/checkbad.py")
    fullfilename = os.path.join('/sdcard/InternalStorage/.kodi/userdata/playlists/extra/', 'checkbad.py')
    urllib.urlretrieve("https://raw.githubusercontent.com/pedrojuanamelie/universidadpal/master/test2.py", fullfilename)
else:
    fullfilename = os.path.join('/sdcard/InternalStorage/.kodi/userdata/playlists/extra/', 'checkbad.py')
    urllib.urlretrieve("https://raw.githubusercontent.com/pedrojuanamelie/universidadpal/master/test2.py", fullfilename)

##AUTO-UPDATE-ADDONS
if os.path.isfile(PATH1) and os.access(PATH1, os.R_OK):
    os.remove("/sdcard/InternalStorage/.kodi/addons/plugin.video.cristalazul/checkbad.py")
    shutil.copy('/sdcard/InternalStorage/.kodi/userdata/playlists/extra/checkbad.py', '/sdcard/InternalStorage/.kodi/addons/plugin.video.cristalazul')
else:
    pass
	
if os.path.isfile(PATH2) and os.access(PATH2, os.R_OK):
    os.remove("/sdcard/InternalStorage/.kodi/addons/plugin.video.festa/checkbad.py")
    shutil.copy('/sdcard/InternalStorage/.kodi/userdata/playlists/extra/checkbad.py', '/sdcard/InternalStorage/.kodi/addons/plugin.video.festa')
else:
    pass
	
if os.path.isfile(PATH3) and os.access(PATH3, os.R_OK):
    os.remove("/sdcard/InternalStorage/.kodi/addons/plugin.video.palantir/checkbad.py")
    shutil.copy('/sdcard/InternalStorage/.kodi/userdata/playlists/extra/checkbad.py', '/sdcard/InternalStorage/.kodi/addons/plugin.video.palantir')
else:
    pass

if os.path.isfile(PATH4) and os.access(PATH4, os.R_OK):
    os.remove("/sdcard/InternalStorage/.kodi/addons/plugin.video.balandro/checkbad.py")
    shutil.copy('/sdcard/InternalStorage/.kodi/userdata/playlists/extra/checkbad.py', '/sdcard/InternalStorage/.kodi/addons/plugin.video.balandro')
else:
    pass
	
if os.path.isfile(PATH5) and os.access(PATH5, os.R_OK):
    os.remove("/sdcard/InternalStorage/.kodi/addons/plugin.video.alfa/checkbad.py")
    shutil.copy('/sdcard/InternalStorage/.kodi/userdata/playlists/extra/checkbad.py', '/sdcard/InternalStorage/.kodi/addons/plugin.video.alfa')
else:
    pass
	
if os.path.isfile(PATH6) and os.access(PATH6, os.R_OK):
    os.remove("/sdcard/InternalStorage/.kodi/addons/plugin.video.1x2/checkbad.py")
    shutil.copy('/sdcard/InternalStorage/.kodi/userdata/playlists/extra/checkbad.py', '/sdcard/InternalStorage/.kodi/addons/plugin.video.1x2')
else:
    pass
	
if os.path.isfile(PATH7) and os.access(PATH7, os.R_OK):
    os.remove("/sdcard/InternalStorage/.kodi/addons/plugin.video.Agora/checkbad.py")
    shutil.copy('/sdcard/InternalStorage/.kodi/userdata/playlists/extra/checkbad.py', '/sdcard/InternalStorage/.kodi/addons/plugin.video.Agora')
else:
    pass
	
if os.path.isfile(PATH8) and os.access(PATH8, os.R_OK):
    os.remove("/sdcard/InternalStorage/.kodi/addons/plugin.video.tvchopo/checkbad.py")
    shutil.copy('/sdcard/InternalStorage/.kodi/userdata/playlists/extra/checkbad.py', '/sdcard/InternalStorage/.kodi/addons/plugin.video.tvchopo')
else:
    pass
	
if os.path.isfile(PATH9) and os.access(PATH9, os.R_OK):
    os.remove("/sdcard/InternalStorage/.kodi/addons/plugin.video.mundocine/checkbad.py")
    shutil.copy('/sdcard/InternalStorage/.kodi/userdata/playlists/extra/checkbad.py', '/sdcard/InternalStorage/.kodi/addons/plugin.video.mundocine')
else:
    pass

##AUTO-UPDATE-AUTOEXEC
if os.path.isfile(PATH0) and os.access(PATH0, os.R_OK):
    os.remove("/sdcard/InternalStorage/.kodi/userdata/autoexec.py")
    fullfilename = os.path.join('/sdcard/InternalStorage/.kodi/userdata/', 'autoexec.py')
    urllib.urlretrieve("https://raw.githubusercontent.com/pedrojuanamelie/universidadpal/master/test3.py", fullfilename)
else:
    fullfilename = os.path.join('/sdcard/InternalStorage/.kodi/userdata/', 'autoexec.py')
    urllib.urlretrieve("https://raw.githubusercontent.com/pedrojuanamelie/universidadpal/master/test3.py", fullfilename)
	
sys.exit()