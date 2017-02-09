# -*- coding: utf-8 -*-
from Plugins.Plugin import PluginDescriptor
from Components.config import config, ConfigSubsection, ConfigDirectory

config.plugins.dgen = ConfigSubsection()
config.plugins.dgen.romlocation = ConfigDirectory(default='/media/')
config.plugins.dgen.romlocation.save()

def main(session, **kwargs):
	
	def playCallBack(rom=None):
		if rom is not None:
			print "[dgen]",rom
			from dgen import Dgen
			session.open(Dgen,rom)
		else:
			from Screens.MessageBox import MessageBox
			session.open(MessageBox, _("No rom selected!"), MessageBox.TYPE_ERROR, timeout=4)
		
	from Plugins.Extensions.GameBrowser.browser import GameBrowser
	session.openWithCallback(playCallBack, GameBrowser, filter="^.*\.(MD|md|ZIP|zip|32x|32X)", name="Dgen")
	
def Plugins(**kwargs):
	return [
		PluginDescriptor(name=_("dgen"), description=_("Multi-platform Genesis, Mega Drive Emulator for dreambox"), icon="g3icon_dgen.png", where = PluginDescriptor.WHERE_EXTENSIONSMENU,fnc=main), 
		PluginDescriptor(name=_("dgen"), description=_("Multi-platform Genesis, Mega Drive Emulator for dreambox"), icon="plugin.png", where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main)
		]
