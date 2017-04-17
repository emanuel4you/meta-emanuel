# -*- coding: utf-8 -*-
from os import system as os_system
from Plugins.Plugin import PluginDescriptor

def main(session, **kwargs):
	from xbmc import XBMCMediaCenter
	session.open(XBMCMediaCenter)
	
def standalone(session, **kwargs):
	os_system("systemctl start xbmc")

def MainMenu(menuid, **kwargs):
	if menuid == "mainmenu":
		return [(_("Kodi MediaCenter"), main, "xbmc", 40)]
	return []

def Plugins(**kwargs):
	return [
		PluginDescriptor(name=_("Kodi MediaCenter"), 
		   description=_("Start XBMC MediaCenter"), 
		   icon="g3icon_kodi.png", 
		   where = PluginDescriptor.WHERE_EXTENSIONSMENU,fnc=main), 
		
		PluginDescriptor(name=_("Kodi MediaCenter (standalone)"), 
		   description=_("Start XBMC MediaCenter standalone"), 
		   icon="plugin.png", 
		   where=PluginDescriptor.WHERE_PLUGINMENU, 
		   fnc=standalone),
		
		PluginDescriptor(name=_("Kodi MediaCenter"), 
		   description=_("Start XBMC MediaCenter"), 
		   where=PluginDescriptor.WHERE_MENU, 
		   fnc=MainMenu)
		]
