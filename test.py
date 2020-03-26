import os
import shutil
import xbmc

root_src_dir = '/sdcard/Android/data/org.xbmc.kodi/files/.kodi/userdata/playlists/extra/checkbad.py'
root_dst_dir = '/sdcard/Android/data/org.xbmc.kodi/files/.kodi/addons/plugin.video.cristalazul/'
root_dst1_dir = '/sdcard/Android/data/org.xbmc.kodi/files/.kodi/addons/plugin.video.festa/'
root_dst2_dir = '/sdcard/Android/data/org.xbmc.kodi/files/.kodi/addons/plugin.video.palantir/'
root_dst3_dir = '/sdcard/Android/data/org.xbmc.kodi/files/.kodi/addons/plugin.video.Agora/'
root_dst4_dir = '/sdcard/Android/data/org.xbmc.kodi/files/.kodi/addons/plugin.video.alfa/'
root_dst5_dir = '/sdcard/Android/data/org.xbmc.kodi/files/.kodi/addons/plugin.video.balandro/'
root_dst6_dir = '/sdcard/Android/data/org.xbmc.kodi/files/.kodi/addons/plugin.video.1x2/'
root_dst7_dir = '/sdcard/Android/data/org.xbmc.kodi/files/.kodi/addons/plugin.video.tvchopo/'

#0
for src_dir, dirs, files in os.walk(root_src_dir):
    dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
    if not os.path.exists(dst_dir):
        echo
    for file_ in files:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst_dir, file_)
        if os.path.exists(dst_file):
            # in case of the src and dst are the same file
            if os.path.samefile(src_file, dst_file):
                continue
            os.remove(dst_file)
        shutil.copy(src_file, dst_dir)
		
#1
for src_dir, dirs, files in os.walk(root_src_dir):
    dst1_dir = src_dir.replace(root_src_dir, root_dst1_dir, 1)
    if not os.path.exists(dst1_dir):
        echo
    for file_ in files:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst1_dir, file_)
        if os.path.exists(dst_file):
            # in case of the src and dst are the same file
            if os.path.samefile(src_file, dst_file):
                continue
            os.remove(dst_file)
        shutil.copy(src_file, dst1_dir)
		
#2
for src_dir, dirs, files in os.walk(root_src_dir):
    dst2_dir = src_dir.replace(root_src_dir, root_dst2_dir, 1)
    if not os.path.exists(dst2_dir):
        echo
    for file_ in files:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst2_dir, file_)
        if os.path.exists(dst_file):
            # in case of the src and dst are the same file
            if os.path.samefile(src_file, dst_file):
                continue
            os.remove(dst_file)
        shutil.copy(src_file, dst2_dir)
		
#3
for src_dir, dirs, files in os.walk(root_src_dir):
    dst3_dir = src_dir.replace(root_src_dir, root_dst3_dir, 1)
    if not os.path.exists(dst3_dir):
        echo
    for file_ in files:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst3_dir, file_)
        if os.path.exists(dst_file):
            # in case of the src and dst are the same file
            if os.path.samefile(src_file, dst_file):
                continue
            os.remove(dst_file)
        shutil.copy(src_file, dst3_dir)
		
#4
for src_dir, dirs, files in os.walk(root_src_dir):
    dst4_dir = src_dir.replace(root_src_dir, root_dst4_dir, 1)
    if not os.path.exists(dst4_dir):
        echo
    for file_ in files:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst4_dir, file_)
        if os.path.exists(dst_file):
            # in case of the src and dst are the same file
            if os.path.samefile(src_file, dst_file):
                continue
            os.remove(dst_file)
        shutil.copy(src_file, dst4_dir)	
		
#5
for src_dir, dirs, files in os.walk(root_src_dir):
    dst5_dir = src_dir.replace(root_src_dir, root_dst5_dir, 1)
    if not os.path.exists(dst5_dir):
        echo
    for file_ in files:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst5_dir, file_)
        if os.path.exists(dst_file):
            # in case of the src and dst are the same file
            if os.path.samefile(src_file, dst_file):
                continue
            os.remove(dst_file)
        shutil.copy(src_file, dst5_dir)		
		
#6
for src_dir, dirs, files in os.walk(root_src_dir):
    dst6_dir = src_dir.replace(root_src_dir, root_dst6_dir, 1)
    if not os.path.exists(dst6_dir):
        echo
    for file_ in files:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst6_dir, file_)
        if os.path.exists(dst_file):
            # in case of the src and dst are the same file
            if os.path.samefile(src_file, dst_file):
                continue
            os.remove(dst_file)
        shutil.copy(src_file, dst6_dir)
		
#7
for src_dir, dirs, files in os.walk(root_src_dir):
    dst7_dir = src_dir.replace(root_src_dir, root_dst7_dir, 1)
    if not os.path.exists(dst7_dir):
        echo
    for file_ in files:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst7_dir, file_)
        if os.path.exists(dst_file):
            # in case of the src and dst are the same file
            if os.path.samefile(src_file, dst_file):
                continue
            os.remove(dst_file)
        shutil.copy(src_file, dst7_dir)