# -*- coding: utf-8 -*-

from os import path as os_path, system as os_system
from os import mkdir as os_mkdir
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, copyfile
from Plugins.Plugin import PluginDescriptor
from Components.config import config, ConfigSubsection, ConfigDirectory

config.plugins.mame = ConfigSubsection()
config.plugins.mame.romlocation = ConfigDirectory(default='/media/')
config.plugins.mame.romlocation.save()

config.plugins.mess = ConfigSubsection()
config.plugins.mess.romlocation = ConfigDirectory(default='/media/')
config.plugins.mess.romlocation.save()

def init(reason, **kwargs):
	if reason == 0:
		if "session" in kwargs:
			if not os_path.exists("/root/.advance/advmame.rc"):
				print "[advmame]: config  /root/.advance/advmame.rc not found creating it..."
				os_system("/usr/bin/advmame --default")

def mame_main(session, **kwargs):
	def playCallBack(rom=None):
		if rom is not None:
			print "[advmame]",rom
			from mame import Mame
			session.open(Mame, name="MAME", script="/usr/bin/advmame-sdl-start", rom=rom)
		else:
			from Screens.MessageBox import MessageBox
			session.open(MessageBox, _("No rom selected!"), MessageBox.TYPE_ERROR, timeout=4)
		
	from Plugins.Extensions.GameBrowser.browser import GameBrowser
	session.openWithCallback(playCallBack, GameBrowser, filter="^.*\.(zip|ZIP)", name="MAME")
	
def mame_mess(session, **kwargs):
	def playCallBack(rom=None):
		if rom is not None:
			print "[advmess]",rom
			from mame import Mame
			session.open(Mame, name="MESS", script="/usr/bin/advmess-sdl-start", rom=rom)
		else:
			from Screens.MessageBox import MessageBox
			session.open(MessageBox, _("No rom selected!"), MessageBox.TYPE_ERROR, timeout=4)
		
	from Plugins.Extensions.GameBrowser.browser import GameBrowser
	session.openWithCallback(playCallBack, GameBrowser, filter="", name="MESS")
	
def menu(session, **kwargs):
	print "[advmenu]"
	from mame import Mame
	session.open(Mame, name="MENU", script="/usr/bin/advmenu-sdl-start")
	
def Plugins(**kwargs):
	return [
		PluginDescriptor(where=PluginDescriptor.WHERE_SESSIONSTART,fnc=init),
		PluginDescriptor(name=_("AdvanceMAME"),
			description=_("Arcade Emulator for dreambox"),
			icon="g3icon_mame.png",
			where = PluginDescriptor.WHERE_EXTENSIONSMENU,fnc=mame_main),
		PluginDescriptor(name=_("AdvanceMAME"),
			description=_("Arcade Emulator for dreambox"),
			icon="mame.png",
			where=PluginDescriptor.WHERE_PLUGINMENU, fnc=mame_main),
		PluginDescriptor(name=_("AdvanceMESS"),
			description=_("Multiple System Emulator for dreambox"),
			icon="g3icon_mess.png",
			where = PluginDescriptor.WHERE_EXTENSIONSMENU,fnc=mame_mess),
		PluginDescriptor(name=_("AdvanceMESS"),
			description=_("Multiple System Emulator for dreambox"),
			icon="mess.png",
			where=PluginDescriptor.WHERE_PLUGINMENU, fnc=mame_mess),
		PluginDescriptor(name=_("AdvanceMenu"),
			description=_("Arcade Menu for dreambox"),
			icon="g3icon_menu.png",
			where = PluginDescriptor.WHERE_EXTENSIONSMENU,fnc=menu),
		PluginDescriptor(name=_("AdvanceMenu"),
			description=_("Arcade Menu for dreambox"),
			icon="menu.png",
			where=PluginDescriptor.WHERE_PLUGINMENU, fnc=menu)
		]
