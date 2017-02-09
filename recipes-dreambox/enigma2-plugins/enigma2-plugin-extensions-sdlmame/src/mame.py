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

from Plugins.Extensions.GameBrowser.browser import GameSummary

from skin import loadSkin

loadSkin(resolveFilename(SCOPE_PLUGINS, "Extensions/GameBrowser/skin.xml"))

#-----------------------------------------------------------------------------------

class Mame(Screen, ServiceStopScreen):
	def __init__(self, session, name="MAME", script="/usr/bin/advmame-start", rom=None):
		self.name = name
		Screen.__init__(self, session)
		ServiceStopScreen.__init__(self)
		self.__script = script
		self.__rom = rom
		
		self.skinName = ["Game"]
		self["title"] = StaticText(self.name)
		if self.__rom is not None:
			self["lcdinfo"] = StaticText(os_path.basename(self.__rom))
		else:
			self["lcdinfo"] = StaticText("no rom selected")
			
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
		print "[%s] - __runEmu"%self.name, rom
		eRCInput.getInstance().lock()
		fbClass.getInstance().lock()
		
		com = "export LANG=" + language.getLanguage() + ".UTF-8;"
		if rom is not None:
			com += "%s '%s';" %(self.__script, rom)
		else:
			com += self.__script
		self.__container.execute(com)

	def __runFinished(self,retval=1):
		print "[%s] - __runFinished"%self.name, retval
		fbClass.getInstance().unlock()
		eRCInput.getInstance().unlock()
		self.close()
		
	def createSummary(self):
		return GameSummary
