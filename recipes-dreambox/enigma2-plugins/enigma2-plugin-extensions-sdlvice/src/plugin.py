# -*- coding: utf-8 -*-
from Plugins.Plugin import PluginDescriptor

def x64(session, **kwargs):
	from vice import Vice
	session.open(Vice)
	
def sel(session, **kwargs):
	def emuCallBack(val=None):
		if val is not None:
			print "[vice]",val[0]
			from vice import Vice
			session.open(Vice, emu=val[1])
		else:
			from Screens.MessageBox import MessageBox
			session.open(MessageBox, _("No Emu selected!"), MessageBox.TYPE_ERROR, timeout=4)
			
	from Screens.ChoiceBox import ChoiceBox
	mnu=((("VC20"),("xvic"),None),
			(("C64"),("x64"),None),
			(("C64DTV"),("x64dtv"),None),
			(("x128"),("x128"),None),
			(("PET"),("xpet"),None),
			(("C264"),("xplus4"),None),
			(("CBM-II"),("xcbm5x0"),None),
			)
	session.openWithCallback(emuCallBack, ChoiceBox, title=_("select a Commodore Emulation"), list=mnu)
	
def x64_load(session, **kwargs):
	def playCallBack(val=None):
		if val is not None:
			print "[x64]",val
			from vice import Vice
			session.open(Vice, emu="x64", rom=val)
		else:
			from Screens.MessageBox import MessageBox
			session.open(MessageBox, _("No rom selected!"), MessageBox.TYPE_ERROR, timeout=4)
			
	from browser import ViceBrowser
	session.openWithCallback(playCallBack, ViceBrowser)

def Plugins(**kwargs):
	emu_list = [PluginDescriptor(name=_("C64"), description=_("C64 Emulator for dreambox"), icon="g3icon_vice.png", where = PluginDescriptor.WHERE_EXTENSIONSMENU,fnc=x64), PluginDescriptor(name=_("C64"), description=_("C64 Emulator for dreambox"), icon="c64.png", where=PluginDescriptor.WHERE_PLUGINMENU, fnc=x64), PluginDescriptor(name=_("C64 LOAD"), description=_("load C64 rom, image"), icon="c64.png", where=PluginDescriptor.WHERE_PLUGINMENU, fnc=x64_load), PluginDescriptor(name=_("C64 LOAD"), description=_("load C64 rom, image"), icon="g3icon_vice.png", where = PluginDescriptor.WHERE_EXTENSIONSMENU,fnc=x64_load), PluginDescriptor(name=_("Commodore Emulation"), description=_("VC20, C64, C128, PET, ..."), icon="c64.png", where=PluginDescriptor.WHERE_PLUGINMENU, fnc=sel), PluginDescriptor(name=_("Commodore Emulation"), description=_("VC20, C64, C128, PET, ..."), icon="g3icon_vice.png", where=PluginDescriptor.WHERE_EXTENSIONSMENU, fnc=sel)]
	
	return emu_list
