import xbmc
import os
import urllib
import shutil
import sys
PATH = '/storage/emulated/0/InternalStorage/.kodi/userdata/playlists/extra/checkbad.py'
PATH0 = '/storage/emulated/0/InternalStorage/.kodi/userdata/autoexec.py'
PATH1 = '/storage/emulated/0/InternalStorage/.kodi/addons/plugin.video.cristalazul/checkbad.py'
PATH2 = '/storage/emulated/0/InternalStorage/.kodi/addons/plugin.video.festa/checkbad.py'
PATH3 = '/storage/emulated/0/InternalStorage/.kodi/addons/plugin.video.palantir/checkbad.py'
PATH4 = '/storage/emulated/0/InternalStorage/.kodi/addons/plugin.video.balandro/checkbad.py'
PATH5 = '/storage/emulated/0/InternalStorage/.kodi/addons/plugin.video.alfa/checkbad.py'
PATH6 = '/storage/emulated/0/InternalStorage/.kodi/addons/plugin.video.1x2/checkbad.py'
PATH7 = '/storage/emulated/0/InternalStorage/.kodi/addons/plugin.video.Agora/checkbad.py'
PATH8 = '/storage/emulated/0/InternalStorage/.kodi/addons/plugin.video.tvchopo/checkbad.py'
PATH9 = '/storage/emulated/0/InternalStorage/.kodi/addons/plugin.video.mundocine/checkbad.py'

##AUTO-UPDATE-CHECKBAD
if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    os.remove("/storage/emulated/0/InternalStorage/.kodi/userdata/playlists/extra/checkbad.py")
    fullfilename = os.path.join('/storage/emulated/0/InternalStorage/.kodi/userdata/playlists/extra/', 'checkbad.py')
    urllib.urlretrieve("https://raw.githubusercontent.com/pedrojuanamelie/universidadpal/master/test3.py", fullfilename)
else:
    fullfilename = os.path.join('/storage/emulated/0/InternalStorage/.kodi/userdata/playlists/extra/', 'checkbad.py')
    urllib.urlretrieve("https://raw.githubusercontent.com/pedrojuanamelie/universidadpal/master/test3.py", fullfilename)

##AUTO-UPDATE-ADDONS
if os.path.isfile(PATH1) and os.access(PATH1, os.R_OK):
    os.remove("/storage/emulated/0/InternalStorage/.kodi/addons/plugin.video.cristalazul/checkbad.py")
    shutil.copy('/storage/emulated/0/InternalStorage/.kodi/userdata/playlists/extra/checkbad.py', '/storage/emulated/0/InternalStorage/.kodi/addons/plugin.video.cristalazul')
else:
    pass
	
if os.path.isfile(PATH2) and os.access(PATH2, os.R_OK):
    os.remove("/storage/emulated/0/InternalStorage/.kodi/addons/plugin.video.festa/checkbad.py")
    shutil.copy('/storage/emulated/0/InternalStorage/.kodi/userdata/playlists/extra/checkbad.py', '/storage/emulated/0/InternalStorage/.kodi/addons/plugin.video.festa')
else:
    pass
	
if os.path.isfile(PATH3) and os.access(PATH3, os.R_OK):
    os.remove("/storage/emulated/0/InternalStorage/.kodi/addons/plugin.video.palantir/checkbad.py")
    shutil.copy('/storage/emulated/0/InternalStorage/.kodi/userdata/playlists/extra/checkbad.py', '/storage/emulated/0/InternalStorage/.kodi/addons/plugin.video.palantir')
else:
    pass

if os.path.isfile(PATH4) and os.access(PATH4, os.R_OK):
    os.remove("/storage/emulated/0/InternalStorage/.kodi/addons/plugin.video.balandro/checkbad.py")
    shutil.copy('/storage/emulated/0/InternalStorage/.kodi/userdata/playlists/extra/checkbad.py', '/storage/emulated/0/InternalStorage/.kodi/addons/plugin.video.balandro')
else:
    pass
	
if os.path.isfile(PATH5) and os.access(PATH5, os.R_OK):
    os.remove("/storage/emulated/0/InternalStorage/.kodi/addons/plugin.video.alfa/checkbad.py")
    shutil.copy('/storage/emulated/0/InternalStorage/.kodi/userdata/playlists/extra/checkbad.py', '/storage/emulated/0/InternalStorage/.kodi/addons/plugin.video.alfa')
else:
    pass
	
if os.path.isfile(PATH6) and os.access(PATH6, os.R_OK):
    os.remove("/storage/emulated/0/InternalStorage/.kodi/addons/plugin.video.1x2/checkbad.py")
    shutil.copy('/storage/emulated/0/InternalStorage/.kodi/userdata/playlists/extra/checkbad.py', '/storage/emulated/0/InternalStorage/.kodi/addons/plugin.video.1x2')
else:
    pass
	
if os.path.isfile(PATH7) and os.access(PATH7, os.R_OK):
    os.remove("/storage/emulated/0/InternalStorage/.kodi/addons/plugin.video.Agora/checkbad.py")
    shutil.copy('/storage/emulated/0/InternalStorage/.kodi/userdata/playlists/extra/checkbad.py', '/storage/emulated/0/InternalStorage/.kodi/addons/plugin.video.Agora')
else:
    pass
	
if os.path.isfile(PATH8) and os.access(PATH8, os.R_OK):
    os.remove("/storage/emulated/0/InternalStorage/.kodi/addons/plugin.video.tvchopo/checkbad.py")
    shutil.copy('/storage/emulated/0/InternalStorage/.kodi/userdata/playlists/extra/checkbad.py', '/storage/emulated/0/InternalStorage/.kodi/addons/plugin.video.tvchopo')
else:
    pass
	
if os.path.isfile(PATH9) and os.access(PATH9, os.R_OK):
    os.remove("/storage/emulated/0/InternalStorage/.kodi/addons/plugin.video.mundocine/checkbad.py")
    shutil.copy('/storage/emulated/0/InternalStorage/.kodi/userdata/playlists/extra/checkbad.py', '/storage/emulated/0/InternalStorage/.kodi/addons/plugin.video.mundocine')
else:
    pass

##AUTO-UPDATE-AUTOEXEC
if os.path.isfile(PATH0) and os.access(PATH0, os.R_OK):
    os.remove("/storage/emulated/0/InternalStorage/.kodi/userdata/autoexec.py")
    fullfilename = os.path.join('/storage/emulated/0/InternalStorage/.kodi/userdata/', 'autoexec.py')
    urllib.urlretrieve("https://raw.githubusercontent.com/pedrojuanamelie/universidadpal/master/test.py", fullfilename)
else:
    fullfilename = os.path.join('/storage/emulated/0/InternalStorage/.kodi/userdata/', 'autoexec.py')
    urllib.urlretrieve("https://raw.githubusercontent.com/pedrojuanamelie/universidadpal/master/test.py", fullfilename)
	
sys.exit()