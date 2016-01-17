# -*- coding: utf-8 -*-
# code by emanuel@ihad.tv

from enigma import eConsoleAppContainer, fbClass, eRCInput

from Components.Language import language
from Components.Sources.StaticText import StaticText

from Screens.Screen import Screen
from Screens.ServiceStopScreen import ServiceStopScreen

from Tools.Directories import resolveFilename, SCOPE_PLUGINS

from skin import loadSkin

loadSkin(resolveFilename(SCOPE_PLUGINS, "Extensions/SDLDosBox/skin.xml"))

#-----------------------------------------------------------------------------------

class DosBoxSummary(Screen):
	def __init__(self, session, parent):
		Screen.__init__(self, session, parent = parent)
		self.skinName = ["DosBoxSummary"]

#-----------------------------------------------------------------------------------

class DosBox(Screen, ServiceStopScreen):
	def __init__(self, session):
		Screen.__init__(self, session)
		ServiceStopScreen.__init__(self)
		self.skinName = ["DosBox"]
		self["title"] = StaticText("DosBox")
		self.__container=eConsoleAppContainer()
		self.__appClosed_conn = self.__container.appClosed.connect(self.__runFinished)
		self.stopService()
		self.__runEmu()
		
	def __runEmu(self):
		print "[DosBox] - __runEmu"
		eRCInput.getInstance().lock()
		fbClass.getInstance().lock()
		com = "export LANG=" + language.getLanguage() + ".UTF-8;"
		com += "/usr/bin/dosbox-start;"
		self.__container.execute(com)

	def __runFinished(self,retval):
		print "[DosBox] - __runFinished"
		fbClass.getInstance().unlock()
		eRCInput.getInstance().unlock()
		self.close()
		
	def createSummary(self):
		return DosBoxSummary
