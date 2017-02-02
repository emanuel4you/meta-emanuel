# -*- coding: utf-8 -*-
from Plugins.Plugin import PluginDescriptor

def main(session, **kwargs):
	
	def playCallBack(val=None):
		if val is not None:
			print "[dgen]",val
			from dgen import Dgen
			session.open(Dgen,val)
		else:
			from Screens.MessageBox import MessageBox
			session.open(MessageBox, _("No rom selected!"), MessageBox.TYPE_ERROR, timeout=4)
		
	from browser import DgenBrowser
	session.openWithCallback(playCallBack, DgenBrowser)
	
def Plugins(**kwargs):
	return [
		PluginDescriptor(name=_("dgen"), description=_("Multi-platform Genesis, Mega Drive Emulator for dreambox"), icon="g3icon_dgen.png", where = PluginDescriptor.WHERE_EXTENSIONSMENU,fnc=main), 
		PluginDescriptor(name=_("dgen"), description=_("Multi-platform Genesis, Mega Drive Emulator for dreambox"), icon="plugin.png", where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main)
		]
