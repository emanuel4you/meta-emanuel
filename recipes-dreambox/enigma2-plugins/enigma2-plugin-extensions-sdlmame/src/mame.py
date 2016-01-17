# -*- coding: utf-8 -*-
# code by emanuel@ihad.tv

from os import path as os_path

from enigma import eConsoleAppContainer, fbClass, eRCInput, eDBoxLCD

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
	def __init__(self, session, rom):
		Screen.__init__(self, session)
		ServiceStopScreen.__init__(self)
		self.__rom = rom
		self.skinName = ["Mame"]
		self["title"] = StaticText("MAME")
		self["lcdinfo"] = StaticText(os_path.basename(self.__rom))
		self.__container=eConsoleAppContainer()
		self.__appClosed_conn = self.__container.appClosed.connect(self.__runFinished)
		self.stopService()
		self.__runEmu(self.__initRom())
		
	def __initRom(self):
		path = "/root/.advance/rom/" + os_path.basename(self.__rom)
		if not os_path.exists(path):
			copyfile(self.__rom, path)
		return os_path.basename(self.__rom.replace(".zip",""))
		
	def __runEmu(self,rom):
		print "[Mame] - __runEmu", rom
		eDBoxLCD.getInstance().lock()
		eRCInput.getInstance().lock()
		fbClass.getInstance().lock()
		
		com = "export LANG=" + language.getLanguage() + ".UTF-8;"
		com += "/usr/bin/advmame-start '%s';" %rom
		self.__container.execute(com)

	def __runFinished(self,retval=1):
		print "[Mame] - __runFinished",retval
		eDBoxLCD.getInstance().unlock()
		fbClass.getInstance().unlock()
		eRCInput.getInstance().unlock()
		self.close()
		
	def createSummary(self):
		return MameSummary
	