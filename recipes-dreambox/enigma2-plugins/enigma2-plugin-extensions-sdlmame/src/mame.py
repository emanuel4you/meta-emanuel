# -*- coding: utf-8 -*-
# code by emanuel@ihad.tv

from os import path as os_path
from time import sleep

from enigma import eConsoleAppContainer, fbClass, eRCInput

from Components.Language import language
from Components.Sources.StaticText import StaticText

from Screens.Screen import Screen
from Screens.ServiceStopScreen import ServiceStopScreen
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, copyfile

from skin import loadSkin

loadSkin(resolveFilename(SCOPE_PLUGINS, "Extensions/SDLMame/skin.xml"))

#-----------------------------------------------------------------------------------

class MameSummary(Screen):
	def __init__(self, session, parent):
		Screen.__init__(self, session, parent = parent)
		self.skinName = ["MameSummary"]

#-----------------------------------------------------------------------------------

class Mame(Screen, ServiceStopScreen):
	def __init__(self, session, rom=None):
		Screen.__init__(self, session)
		ServiceStopScreen.__init__(self)
		self.__rom = rom
		self.skinName = ["Mame"]
		if self.__rom is not None:
			self["title"] = StaticText("MAME")
			self["lcdinfo"] = StaticText(os_path.basename(self.__rom))
		else:
			self["title"] = StaticText("MENU")
			self["lcdinfo"] = StaticText("")
		self.__container=eConsoleAppContainer()
		self.__appClosed_conn = self.__container.appClosed.connect(self.__runFinished)
		self.stopService()
		self.__runEmu(self.__initRom())
		
	def __initRom(self):
		if self.__rom is None:
			return None
		path = "/root/.advance/rom/" + os_path.basename(self.__rom)
		if not os_path.exists(path):
			copyfile(self.__rom, path)
			sleep(1)
		return os_path.basename(self.__rom.replace(".zip",""))
		
	def __runEmu(self,rom):
		print "[Mame] - __runEmu", rom
		eRCInput.getInstance().lock()
		fbClass.getInstance().lock()
		
		com = "export LANG=" + language.getLanguage() + ".UTF-8;"
		if rom is not None:
			com += "/usr/bin/advmame-start '%s';" %rom
		else:
			com += "/usr/bin/advmenu-start"
		self.__container.execute(com)

	def __runFinished(self,retval=1):
		print "[Mame] - __runFinished",retval
		fbClass.getInstance().unlock()
		eRCInput.getInstance().unlock()
		self.close()
		
	def createSummary(self):
		return MameSummary
