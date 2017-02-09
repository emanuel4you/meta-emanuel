# -*- coding: utf-8 -*-
from Plugins.Plugin import PluginDescriptor
from Components.config import config, ConfigSubsection, ConfigDirectory

config.plugins.fbzx = ConfigSubsection()
config.plugins.fbzx.romlocation = ConfigDirectory(default='/media/')
config.plugins.fbzx.romlocation.save()

def load(session, **kwargs):
	
	def playCallBack(val=None):
		if val is not None:
			print "[Fbzx]",val
			from fbzx import Fbzx
			session.open(Fbzx,val)
		else:
			from Screens.MessageBox import MessageBox
			session.open(MessageBox, _("No rom selected!"), MessageBox.TYPE_ERROR, timeout=4)
		
	from Plugins.Extensions.GameBrowser.browser import GameBrowser
	session.openWithCallback(playCallBack, GameBrowser, filter="^.*\.(z80|Z80|SNA|sna|TAP|tap|TZX|tzx)", name="Fbzx")
	
def main(session, **kwargs):
	from fbzx import Fbzx
	session.open(Fbzx)
	
def Plugins(**kwargs):
	return [
		PluginDescriptor(name=_("Fbzx"), description=_("ZX Sinclair Emulator for dreambox"), icon="g3icon_fbzx.png", where = PluginDescriptor.WHERE_EXTENSIONSMENU,fnc=main), 
		PluginDescriptor(name=_("Fbzx"), description=_("ZX Sinclair Emulator for dreambox"), icon="plugin.png", where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main), 
		PluginDescriptor(name=_("Fbzx"), description=_("ZX Sinclair load ROM"), icon="plugin.png", where=PluginDescriptor.WHERE_PLUGINMENU, fnc=load)
		]
