# -*- coding: utf-8 -*-
from Plugins.Plugin import PluginDescriptor

def main(session, **kwargs):
	from wolf3d import Wolf3d
	session.open(Wolf3d)

def Plugins(**kwargs):
	return [
		PluginDescriptor(name=_("Wolf3d"), description=_("Wolf3d Gaming Engine for dreambox"),
		   icon="g3icon_wolf3d.png",
		   where = PluginDescriptor.WHERE_EXTENSIONSMENU,
		   fnc=main),
		PluginDescriptor(name=_("Wolf3d"), description=_("Wolf3d Gaming Engine for dreambox"),
		   icon="plugin.png",
		   where=PluginDescriptor.WHERE_PLUGINMENU,
		   fnc=main)
		]

