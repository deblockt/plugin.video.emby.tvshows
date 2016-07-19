# -*- coding: utf-8 -*-

#################################################################################################

import os
import sys
import urlparse

import xbmc
import xbmcaddon

#################################################################################################

_addon = xbmcaddon.Addon(id='plugin.video.emby')
addon_path = _addon.getAddonInfo('path').decode('utf-8')
base_resource = xbmc.translatePath(os.path.join(addon_path, 'resources', 'lib')).decode('utf-8')
sys.path.append(base_resource)

#################################################################################################

import entrypoint

# Parse parameters
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
params = urlparse.parse_qs(sys.argv[2][1:])
xbmc.log("Parameter string: %s" % sys.argv[2])

try:
    mode = params['mode'][0]
    itemid = params['id'][0]
    dbid = params['dbid'][0]

except (KeyError, IndexError):
    pass
        
else:
    if "play" in mode:
        # plugin.video.emby entrypoint
        entrypoint.doPlayback(itemid, dbid)