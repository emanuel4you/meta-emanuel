# # -*- coding: utf-8 -*-
# code by emanuel@ihad.tv

from Screens.Screen import Screen
from Components.ActionMap import ActionMap
from Components.FileList import FileList
from Components.ConfigList import ConfigListScreen
from Components.config import config, ConfigSubsection, ConfigDirectory
from Components.Label import Label
from Components.Sources.StaticText import StaticText
from Tools.Directories import pathExists, createDir, SCOPE_HDD, SCOPE_PLUGINS, resolveFilename

config.plugins.vice = ConfigSubsection()
config.plugins.vice.romlocation = ConfigDirectory(default="/media/hdd")

from skin import loadSkin
loadSkin(resolveFilename(SCOPE_PLUGINS, "Extensions/SDLVice/skin.xml"))

#-----------------------------------------------------------------------------------

class ViceBrowserSummary(Screen):
	def __init__(self, session, parent):
		Screen.__init__(self, session, parent = parent)
		self.skinName = ["ViceBrowserSummary"]

#-----------------------------------------------------------------------------------

class ViceBrowser(Screen):
	def __init__(self, session, filemode=True):
		Screen.__init__(self, session)
		self.skinName = ["ViceBrowser"]
		self.filemode = filemode
		self["title"] = StaticText("Vice Browser")
		self["lcdinfo"] = StaticText()
		if self.filemode:
			self.filelist = FileList(config.plugins.vice.romlocation.value, matchingPattern = "^.*\.(d64|D64|t64|T64|crt|CRT|P00|p00|g64|G64|p64|P64|d67|D67|d71|D71|d81|D81|d80|D80|d82|D82|d1m|D1M|d2m|D2M|d4,|D4M)", showDirectories = True)
		else:
			self.filelist = FileList(config.plugins.vice.romlocation.value, showDirectories = True, showFiles = False)
			
		self["filelist"] = self.filelist
		self["buttonred"] = Label(_("Cancel"))
		self["buttongreen"] = Label(_("Select"))
		self["info"] = Label("")
		self["actions"] = ActionMap(["OkCancelActions", "ColorActions", "ShortcutActions", "DirectionActions"],
		{
			"ok": self.KeyOk,
			"cancel": self.KeyCancel,
			"green": self.KeyGreen,
			"red" : self.KeyRed,
			"up": self.KeyUp,
			"upRepeated": self.KeyUp,
			"downRepeated": self.KeyDown,
			"down": self.KeyDown,
			"left": self.KeyLeft,
			"right": self.KeyRight
		}, -1)
		
		self.onShown.append(self.__setInfo)
		self.onShown.append(self.__setTitle)

	def __setTitle(self):
		if self.filemode:
			self.setTitle(_("Select a rom for Vice"))
		else:
			self.setTitle(_("Select a directory for roms"))
		
	def __setInfo(self):
		self["info"].setText(self["filelist"].getCurrentDirectory())
		self["lcdinfo"].setText(self["filelist"].getCurrent()[1][7])
		
	def createSummary(self):
		return ViceBrowserSummary

	def KeyUp(self):
		self["filelist"].up()
		self.__setInfo()

	def KeyDown(self):
		self["filelist"].down()
		self.__setInfo()

	def KeyRight(self):
		self["filelist"].pageDown()
		self.__setInfo()

	def KeyLeft(self):
		self["filelist"].pageUp()
		self.__setInfo()

	def KeyGreen(self):
		if self.filemode:
			self.KeyOk()
		elif self["filelist"].getSelection()[0] <> "/autofs/" and self["filelist"].canDescent(): # isDir
			config.plugins.vice.romlocation.value = self["filelist"].getCurrentDirectory()
			config.plugins.vice.romlocation.save()
			if self["filelist"].getCurrentDirectory().endswith("/"):
				dir = self["filelist"].getCurrentDirectory()
			else:
				dir = self["filelist"].getCurrentDirectory() + "/"
			self.close(dir)

	def KeyOk(self):
		if self["filelist"].getSelection()[0] <> "/autofs/":
			if self["filelist"].canDescent(): # isDir
				self["filelist"].descent()
				self.__setInfo()
				
			elif self.filemode and self["filelist"].getFilename():
				config.plugins.vice.romlocation.value = self["filelist"].getCurrentDirectory()
				config.plugins.vice.romlocation.save()
				if self["filelist"].getCurrentDirectory().endswith("/"):
					file = self["filelist"].getCurrentDirectory() + self["filelist"].getFilename()
				else:
					file = self["filelist"].getCurrentDirectory() + "/" + self["filelist"].getFilename()
				self.close(file)

	def KeyRed(self):
		self.KeyCancel()

	def KeyCancel(self):
		self.close(None)
 
