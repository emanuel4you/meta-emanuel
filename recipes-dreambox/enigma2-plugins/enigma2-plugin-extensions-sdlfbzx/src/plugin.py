# -*- coding: utf-8 -*-
from Plugins.Plugin import PluginDescriptor

def load(session, **kwargs):
	
	def playCallBack(val=None):
		if val is not None:
			print "[Fbzx]",val
			from fbzx import Fbzx
			session.open(Fbzx,val)
		else:
			from Screens.MessageBox import MessageBox
			session.open(MessageBox, _("No rom selected!"), MessageBox.TYPE_ERROR, timeout=4)
		
	from browser import FbzxBrowser
	session.openWithCallback(playCallBack, FbzxBrowser)
	
def main(session, **kwargs):
	from fbzx import Fbzx
	session.open(Fbzx)
	
def Plugins(**kwargs):
	return [
		PluginDescriptor(name=_("Fbzx"), description=_("ZX Sinclair Emulator for dreambox"), icon="g3icon_fbzx.png", where = PluginDescriptor.WHERE_EXTENSIONSMENU,fnc=main), 
		PluginDescriptor(name=_("Fbzx"), description=_("ZX Sinclair Emulator for dreambox"), icon="plugin.png", where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main), 
		PluginDescriptor(name=_("Fbzx"), description=_("ZX Sinclair load ROM"), icon="plugin.png", where=PluginDescriptor.WHERE_PLUGINMENU, fnc=load)
		]
