# -*- coding: utf-8 -*-
# code by emanuel@ihad.tv

from enigma import eConsoleAppContainer, fbClass, eRCInput

from Components.Language import language
from Components.Sources.StaticText import StaticText

from Screens.Screen import Screen
from Screens.ServiceStopScreen import ServiceStopScreen

from Tools.Directories import resolveFilename, SCOPE_PLUGINS

from skin import loadSkin

loadSkin(resolveFilename(SCOPE_PLUGINS, "Extensions/SDLVice/skin.xml"))

#-----------------------------------------------------------------------------------

class ViceSummary(Screen):
	def __init__(self, session, parent):
		Screen.__init__(self, session, parent = parent)
		self.skinName = ["ViceSummary"]

#-----------------------------------------------------------------------------------

class Vice(Screen, ServiceStopScreen):
	def __init__(self, session, emu="x64", rom=""):
        	self.__emu=emu
        	self.__rom=rom
		Screen.__init__(self, session)
		ServiceStopScreen.__init__(self)
		self.skinName = ["Vice"]
		self["lcdinfo"] = StaticText(self.__rom)
		self["title"] = StaticText(emu)
		self.__container=eConsoleAppContainer()
		self.__appClosed_conn = self.__container.appClosed.connect(self.__runFinished)
		self.stopService()
		self.__runEmu()
		
	def __runEmu(self):
		print "[Vice] - __runEmu", self.__emu
		eRCInput.getInstance().lock()
		fbClass.getInstance().lock()
		com = "export LANG=" + language.getLanguage() + ".UTF-8;"
		com += "/usr/bin/vice-start '%s'" %self.__emu
		if self.__rom != "":
			com += " '%s'" %self.__rom
		self.__container.execute(com)

	def __runFinished(self,retval):
		print "[Vice] - runFinished"
		fbClass.getInstance().unlock()
		eRCInput.getInstance().unlock()
		self.close()
		
	def createSummary(self):
		return ViceSummary
