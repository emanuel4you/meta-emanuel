# -*- coding: utf-8 -*-
from Plugins.Plugin import PluginDescriptor

def main(session, **kwargs):
	from d1x import D1X
	session.open(D1X)

def Plugins(**kwargs):
	return [PluginDescriptor(name=_("D1X"), description=_("D1X-Rebirth is a Source Port of the Descent Game for dreambox"), icon="g3icon_d1x.png", where = PluginDescriptor.WHERE_EXTENSIONSMENU,fnc=main), PluginDescriptor(name=_("D1X"), description=_("D1X-Rebirth is a Source Port of the Descent Game for dreambox"), icon="plugin.png", where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main)]
