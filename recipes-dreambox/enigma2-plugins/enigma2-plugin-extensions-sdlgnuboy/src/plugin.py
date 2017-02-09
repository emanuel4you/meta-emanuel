# -*- coding: utf-8 -*-
from Plugins.Plugin import PluginDescriptor
from Components.config import config, ConfigSubsection, ConfigDirectory

config.plugins.gnuboy = ConfigSubsection()
config.plugins.gnuboy.romlocation = ConfigDirectory(default='/media/')
config.plugins.gnuboy.romlocation.save()

def main(session, **kwargs):
	
	def playCallBack(rom=None):
		if rom is not None:
			print "[GnuBoy]",rom
			from gnuboy import GnuBoy
			session.open(GnuBoy,rom)
		else:
			from Screens.MessageBox import MessageBox
			session.open(MessageBox, _("No rom selected!"), MessageBox.TYPE_ERROR, timeout=4)
		
	from Plugins.Extensions.GameBrowser.browser import GameBrowser
	session.openWithCallback(playCallBack, GameBrowser, filter="^.*\.(gb|GB)", name="GnuBoy")
	
def Plugins(**kwargs):
	return [PluginDescriptor(name=_("GnuBoy"), description=_("Gameboy Emulator for dreambox"), icon="g3icon_gnuboy.png", where = PluginDescriptor.WHERE_EXTENSIONSMENU,fnc=main), PluginDescriptor(name=_("GnuBoy"), description=_("Gameboy Emulator for dreambox"), icon="plugin.png", where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main)]
