# -*- coding: utf-8 -*-

from os import path as os_path
from os import mkdir as os_mkdir
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, copyfile
from Plugins.Plugin import PluginDescriptor

def init(reason, **kwargs):
	if reason == 0:
		if "session" in kwargs:
			if not os_path.exists("/root/.advance/advmame.rc"):
				print "[Mame]: config  /root/.advance/advmame.rc not found creating defaults..."
				if not os_path.exists("/root/.advance"):
					os_mkdir("/root/.advance")
					os_mkdir("/root/.advance/rom")
				copyfile(resolveFilename(SCOPE_PLUGINS, "Extensions/SDLMame/advmame.rc.default"), "/root/.advance/advmame.rc")

def main(session, **kwargs):
	def playCallBack(val=None):
		if val is not None:
			print "[Mame]",val
			from mame import Mame
			session.open(Mame,val)
		else:
			from Screens.MessageBox import MessageBox
			session.open(MessageBox, _("No rom selected!"), MessageBox.TYPE_ERROR, timeout=4)
		
	from browser import MameBrowser
	session.openWithCallback(playCallBack, MameBrowser)
	
def Plugins(**kwargs):
	return [PluginDescriptor(where=PluginDescriptor.WHERE_SESSIONSTART,fnc=init),PluginDescriptor(name=_("Advance Mame"), description=_("Arcade Emulator for dreambox"), icon="g3icon_mame.png", where = PluginDescriptor.WHERE_EXTENSIONSMENU,fnc=main), PluginDescriptor(name=_("Advance Mame"), description=_("Arcade Emulator for dreambox"), icon="mame.png", where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main)]
