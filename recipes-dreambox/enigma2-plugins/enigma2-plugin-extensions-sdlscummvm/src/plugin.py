# -*- coding: utf-8 -*-
from Plugins.Plugin import PluginDescriptor

def main(session, **kwargs):
	from scummvm import Scummvm
	session.open(Scummvm)

def Plugins(**kwargs):
	return [PluginDescriptor(name=_("Scummvm"), description=_("Scummvm game VM for dreambox"), icon="g3icon_scummvm.png", where = PluginDescriptor.WHERE_EXTENSIONSMENU,fnc=main), PluginDescriptor(name=_("Scummvm"), description=_("Scummvm game VM for dreambox"), icon="plugin.png", where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main)]

