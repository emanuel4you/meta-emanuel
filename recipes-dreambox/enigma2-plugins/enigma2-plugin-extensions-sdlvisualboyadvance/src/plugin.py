# -*- coding: utf-8 -*-
from Plugins.Plugin import PluginDescriptor
from Components.config import config, ConfigSubsection, ConfigDirectory

config.plugins.visualboyadvance = ConfigSubsection()
config.plugins.visualboyadvance.romlocation = ConfigDirectory(default='/media/')
config.plugins.visualboyadvance.romlocation.save()

def main(session, **kwargs):
	
	def playCallBack(rom=None):
		if rom is not None:
			print "[VisualBoyAdvance]",rom
			from visualboyadvance import VisualBoyAdvance
			session.open(VisualBoyAdvance,rom)
		else:
			from Screens.MessageBox import MessageBox
			session.open(MessageBox, _("No rom selected!"), MessageBox.TYPE_ERROR, timeout=4)
		
	from Plugins.Extensions.GameBrowser.browser import GameBrowser
	session.openWithCallback(playCallBack, GameBrowser, filter="^.*\.(gb|GB|gba|GBA|zip|ZIP)", name="VisualBoyAdvance")
	
def Plugins(**kwargs):
	return [PluginDescriptor(name=_("VisualBoy Advance"), description=_("Gameboy Advance Emulator for dreambox"), icon="g3icon_visualboyadvance.png", where = PluginDescriptor.WHERE_EXTENSIONSMENU,fnc=main), PluginDescriptor(name=_("VisualBoy Advance"), description=_("Gameboy Advance Emulator for dreambox"), icon="plugin.png", where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main)]
