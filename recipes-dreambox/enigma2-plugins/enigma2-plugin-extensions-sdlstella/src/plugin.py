# -*- coding: utf-8 -*-
from Plugins.Plugin import PluginDescriptor
from Components.config import config, ConfigSubsection, ConfigDirectory

config.plugins.stella = ConfigSubsection()
config.plugins.stella.romlocation = ConfigDirectory(default='/media/')
config.plugins.stella.romlocation.save()

def main(session, **kwargs):
	
	def playCallBack(rom=None):
		if rom is not None:
			print "[Stella]",rom
			from stella import Stella
			session.open(Stella,rom)
		else:
			from Screens.MessageBox import MessageBox
			session.open(MessageBox, _("No rom selected!"), MessageBox.TYPE_ERROR, timeout=4)
		
	from Plugins.Extensions.GameBrowser.browser import GameBrowser
	session.openWithCallback(playCallBack, GameBrowser, filter="^.*\.(bin|BIN)", name="Stella")
	
def Plugins(**kwargs):
	return [PluginDescriptor(name=_("Stella"), description=_("Atari Emulator for dreambox"), icon="g3icon_stella.png", where = PluginDescriptor.WHERE_EXTENSIONSMENU,fnc=main), PluginDescriptor(name=_("Stella"), description=_("Atari Emulator for dreambox"), icon="stella.png", where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main)]
