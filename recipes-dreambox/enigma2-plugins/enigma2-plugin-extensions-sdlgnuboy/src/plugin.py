# -*- coding: utf-8 -*-
from Plugins.Plugin import PluginDescriptor
			
def main(session, **kwargs):
	
	def playCallBack(val=None):
		if val is not None:
			print "[GnuBoy]",val
			from gnuboy import GnuBoy
			session.open(GnuBoy,val)
		else:
			from Screens.MessageBox import MessageBox
			session.open(MessageBox, _("No rom selected!"), MessageBox.TYPE_ERROR, timeout=4)
		
	from browser import GnuBoyBrowser
	session.openWithCallback(playCallBack, GnuBoyBrowser)
	
def Plugins(**kwargs):
	return [PluginDescriptor(name=_("GnuBoy"), description=_("Gameboy Emulator for dreambox"), icon="g3icon_gnuboy.png", where = PluginDescriptor.WHERE_EXTENSIONSMENU,fnc=main), PluginDescriptor(name=_("GnuBoy"), description=_("Gameboy Emulator for dreambox"), icon="plugin.png", where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main)]
