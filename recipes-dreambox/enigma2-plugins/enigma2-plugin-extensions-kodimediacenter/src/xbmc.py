# -*- coding: utf-8 -*-
# code by emanuel@ihad.tv

from enigma import eConsoleAppContainer, fbClass, eRCInput

from Components.Language import language
from Components.Sources.StaticText import StaticText

from Screens.Screen import Screen
from Screens.ServiceStopScreen import ServiceStopScreen

from Tools.Directories import resolveFilename, SCOPE_PLUGINS

from skin import loadSkin

loadSkin(resolveFilename(SCOPE_PLUGINS, "Extensions/XBMCMediaCenter/skin.xml"))

#-----------------------------------------------------------------------------------

class XBMCMediaCenterSummary(Screen):
	def __init__(self, session, parent):
		Screen.__init__(self, session, parent = parent)
		self.skinName = ["XBMCMediaCenterSummary"]

#-----------------------------------------------------------------------------------

class XBMCMediaCenter(Screen, ServiceStopScreen):
	def __init__(self, session):
		Screen.__init__(self, session)
		ServiceStopScreen.__init__(self)
		self.skinName = ["XBMCMediaCenter"]
		self["title"] = StaticText("Kodi")
		self["lcdinfo"] = StaticText()
		self.__container=eConsoleAppContainer()
		self.__appClosed_conn = self.__container.appClosed.connect(self.__runFinished)
		self.stopService()
		self.__runXBMCMediaCenter()
		
	def __runXBMCMediaCenter(self):
		print "[XBMCMediaCenter] - __runXBMCMediaCenter"
		eRCInput.getInstance().lock()
		fbClass.getInstance().lock()
		com = "export LANG=" + language.getLanguage() + ".UTF-8;"
		com += "/usr/bin/xbmc-start;"
		self.__container.execute(com)

	def __runFinished(self,retval):
		print "[XBMCMediaCenter] - __runFinished"
		fbClass.getInstance().unlock()
		eRCInput.getInstance().unlock()
		self.close()
		
	def createSummary(self):
		return XBMCMediaCenterSummary
