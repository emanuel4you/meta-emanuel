# -*- coding: utf-8 -*-
from Plugins.Plugin import PluginDescriptor
		
def main(session, **kwargs):
	
	def playCallBack(val=None):
		if val is not None:
			print "[Stella]",val
			from stella import Stella
			session.open(Stella,val)
		else:
			from Screens.MessageBox import MessageBox
			session.open(MessageBox, _("No rom selected!"), MessageBox.TYPE_ERROR, timeout=4)
		
	from browser import StellaBrowser
	session.openWithCallback(playCallBack, StellaBrowser)
	
def Plugins(**kwargs):
	return [PluginDescriptor(name=_("Stella"), description=_("Atari Emulator for dreambox"), icon="g3icon_stella.png", where = PluginDescriptor.WHERE_EXTENSIONSMENU,fnc=main), PluginDescriptor(name=_("Stella"), description=_("Atari Emulator for dreambox"), icon="stella.png", where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main)]
