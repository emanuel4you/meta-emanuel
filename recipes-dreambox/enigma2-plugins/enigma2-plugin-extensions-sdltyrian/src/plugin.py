# -*- coding: utf-8 -*-
from Plugins.Plugin import PluginDescriptor

def main(session, **kwargs):
	from tyrian import Tyrian
	session.open(Tyrian)

def Plugins(**kwargs):
	return [PluginDescriptor(name=_("Open Tyrian"), description=_("OpenTyrian is a port of the DOS shoot-em-up Tyrian for dreambox"), icon="g3icon_tyrian.png", where = PluginDescriptor.WHERE_EXTENSIONSMENU,fnc=main), PluginDescriptor(name=_("Open Tyrian"), description=_("OpenTyrian is a port of the DOS shoot-em-up Tyrian for dreambox"), icon="plugin.png", where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main)]
