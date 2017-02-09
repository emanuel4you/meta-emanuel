# -*- coding: utf-8 -*-

from os import path as os_path
from os import mkdir as os_mkdir
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, copyfile
from Plugins.Plugin import PluginDescriptor
from Components.config import config, ConfigSubsection, ConfigDirectory

config.plugins.snes = ConfigSubsection()
config.plugins.snes.romlocation = ConfigDirectory(default='/media/')
config.plugins.snes.romlocation.save()

def init(reason, **kwargs):
	if reason == 0:
		if "session" in kwargs:
			if not os_path.exists("/root/.snes9x/snes9x.conf"):
				print "[Snes]: config  /root/.snes9x/snes9x.conf not found creating defaults..."
				if not os_path.exists("/root/.snes9x"):
					os_mkdir("/root/.snes9x")
					os_mkdir("/root/.snes9x/rom")
				copyfile(resolveFilename(SCOPE_PLUGINS, "Extensions/SDLSnes/snes9x.conf.default"), "/root/.snes9x/snes9x.conf")

def main(session, **kwargs):
	
	def playCallBack(rom=None):
		if rom is not None:
			print "[Snes]",rom
			from snes import Snes
			session.open(Snes,rom)
		else:
			from Screens.MessageBox import MessageBox
			session.open(MessageBox, _("No rom selected!"), MessageBox.TYPE_ERROR, timeout=4)
		
	from Plugins.Extensions.GameBrowser.browser import GameBrowser
	session.openWithCallback(playCallBack, GameBrowser, filter="^.*\.(zip|smc|SMC|sfc|SFC)", name="Snes")
	
def Plugins(**kwargs):
	return [
		PluginDescriptor(name=_("Snes"), description=_("Super Nintendo Emulator for dreambox"), icon="g3icon_snes.png", where = PluginDescriptor.WHERE_EXTENSIONSMENU,fnc=main), 
		PluginDescriptor(name=_("Snes"), description=_("Super Nintendo Emulator for dreambox"), icon="snes.png", where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main),
		PluginDescriptor(where=PluginDescriptor.WHERE_SESSIONSTART,fnc=init)
		]
