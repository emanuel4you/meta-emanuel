# -*- coding: utf-8 -*-
from Plugins.Plugin import PluginDescriptor

def main(session, **kwargs):
	from quake import Quake
	session.open(Quake)

def Plugins(**kwargs):
	return [
		PluginDescriptor(name=_("Quake"), description=_("Quake Gaming Engine for dreambox"),
		   icon="g3icon_quake.png",
		   where = PluginDescriptor.WHERE_EXTENSIONSMENU,
		   fnc=main),
		PluginDescriptor(name=_("Quake"), description=_("Quake Gaming Engine for dreambox"),
		   icon="plugin.png",
		   where=PluginDescriptor.WHERE_PLUGINMENU,
		   fnc=main)
		]

