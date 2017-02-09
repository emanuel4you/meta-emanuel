# -*- coding: utf-8 -*-

from os import path as os_path, mkdir as os_mkdir
from Plugins.Plugin import PluginDescriptor
from Components.config import config, ConfigSubsection, ConfigDirectory
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, copyfile

config.plugins.gngeo = ConfigSubsection()
config.plugins.gngeo.romlocation = ConfigDirectory(default='/media/')
config.plugins.gngeo.romlocation.save()

def init(reason, **kwargs):
	if reason == 0:
		if "session" in kwargs:
			if not os_path.exists("/root/.gngeo/gngeorc"):
				print "[gngeo]: config  /root/.gngeo/gngeorc not found creating defaults..."
				if not os_path.exists("/root/.gngeo"):
					os_mkdir("/root/.gngeo")
				if not os_path.exists("/root/.gngeo/roms"):
					os_mkdir("/root/.gngeo/roms")
				if not os_path.exists("/root/.gngeo/bios"):
					os_mkdir("/root/.gngeo/bios")
				copyfile(resolveFilename(SCOPE_PLUGINS, "Extensions/SDLGnGeo/gngeorc.default"), "/root/.gngeo/gngeorc")

def main(session, **kwargs):
	
	def playCallBack(rom=None):
		if rom is not None:
			print "[gngeo]",rom
			from gngeo import GnGeo
			session.open(GnGeo,rom)
		else:
			from Screens.MessageBox import MessageBox
			session.open(MessageBox, _("No rom selected!"), MessageBox.TYPE_ERROR, timeout=4)
		
	from Plugins.Extensions.GameBrowser.browser import GameBrowser
	session.openWithCallback(playCallBack, GameBrowser, filter="^.*\.(zip|ZIP)", name="GnGeo")
	
def Plugins(**kwargs):
	return [
		PluginDescriptor(name=_("GnGeo"), description=_("NeoGeo Emulator for dreambox"), icon="g3icon_gngeo.png", where = PluginDescriptor.WHERE_EXTENSIONSMENU,fnc=main), 
		PluginDescriptor(name=_("GnGeo"), description=_("NeoGeo Emulator for dreambox"), icon="plugin.png", where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main),
		PluginDescriptor(where=PluginDescriptor.WHERE_SESSIONSTART,fnc=init)
		]
