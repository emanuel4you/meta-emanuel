# -*- coding: utf-8 -*-
from Plugins.Plugin import PluginDescriptor

def main(session, **kwargs):
	from dosbox import DosBox
	session.open(DosBox)

def Plugins(**kwargs):
	return [PluginDescriptor(name=_("DosBox"), description=_("Dos Emulator for dreambox"), icon="g3icon_dosbox.png", where = PluginDescriptor.WHERE_EXTENSIONSMENU,fnc=main), PluginDescriptor(name=_("DosBox"), description=_("Dos Emulator for dreambox"), icon="plugin.png", where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main)]
