# -*- coding: utf-8 -*-
from Plugins.Plugin import PluginDescriptor
from Components.config import config, ConfigSubsection, ConfigDirectory

config.plugins.pcsx = ConfigSubsection()
config.plugins.pcsx.romlocation = ConfigDirectory(default='/media/')
config.plugins.pcsx.romlocation.save()

def main(session, **kwargs):
	
	def playCallBack(rom=None):
		if rom is not None:
			print "[pcsx]",rom
			from pcsx import Pcsx
			session.open(Pcsx,rom)
		else:
			from Screens.MessageBox import MessageBox
			session.open(MessageBox, _("No rom selected!"), MessageBox.TYPE_ERROR, timeout=4)
		
	from Plugins.Extensions.GameBrowser.browser import GameBrowser
	session.openWithCallback(playCallBack, GameBrowser, filter="^.*\.(bin|img|mdf|iso|cue|z|bz|znx|pbp|cbn|exe)", name="Pcsx")
	
def Plugins(**kwargs):
	return [
		PluginDescriptor(name=_("Pcsx"), description=_("Playstation Emulator for dreambox"), icon="g3icon_pcsx.png", where = PluginDescriptor.WHERE_EXTENSIONSMENU,fnc=main), 
		PluginDescriptor(name=_("Pcsx"), description=_("Playstation Emulator for dreambox"), icon="plugin.png", where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main)
		]
