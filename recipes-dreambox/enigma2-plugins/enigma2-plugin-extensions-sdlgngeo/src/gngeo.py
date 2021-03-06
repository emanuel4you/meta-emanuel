# -*- coding: utf-8 -*-
# code by emanuel@ihad.tv

from os import path as os_path

from enigma import eConsoleAppContainer, fbClass, eRCInput, eDBoxLCD

from Components.Language import language
from Components.Sources.StaticText import StaticText

from Screens.Screen import Screen
from Screens.ServiceStopScreen import ServiceStopScreen
from Tools.Directories import resolveFilename, SCOPE_PLUGINS

from Plugins.Extensions.GameBrowser.browser import GameSummary

from skin import loadSkin

loadSkin(resolveFilename(SCOPE_PLUGINS, "Extensions/GameBrowser/skin.xml"))

#-----------------------------------------------------------------------------------

class GnGeo(Screen, ServiceStopScreen):
	def __init__(self, session, rom=""):
		Screen.__init__(self, session)
		ServiceStopScreen.__init__(self)
		self.__rom = rom
		self.skinName = ["Game"]
		self["title"] = StaticText("GnGeo")
		self["lcdinfo"] = StaticText(os_path.basename(self.__rom))
		self.__container=eConsoleAppContainer()
		self.__appClosed_conn = self.__container.appClosed.connect(self.__runFinished)
		self.stopService()
		self.__runEmu(self.__rom)
		
	def __runEmu(self,rom):
		print "[GnGeo] - __runEmu", rom
		eDBoxLCD.getInstance().lock()
		eRCInput.getInstance().lock()
		fbClass.getInstance().lock()
		com = "export LANG=" + language.getLanguage() + ".UTF-8;"
		com += "/usr/bin/gngeo-sdl-start '%s';" %os_path.basename(rom.replace(".zip",""))
		self.__container.execute(com)

	def __runFinished(self,retval=1):
		print "[GnGeo] - __runFinished",retval
		eDBoxLCD.getInstance().unlock()
		fbClass.getInstance().unlock()
		eRCInput.getInstance().unlock()
		self.close()
		
	def createSummary(self):
		return GameSummary
	