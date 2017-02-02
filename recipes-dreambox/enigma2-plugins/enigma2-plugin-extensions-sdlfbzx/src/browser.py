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

from skin import loadSkin

loadSkin(resolveFilename(SCOPE_PLUGINS, "Extensions/SDLFbzx/skin.xml"))

config.plugins.fbzx = ConfigSubsection()
config.plugins.fbzx.romlocation = ConfigDirectory(default="/root")

#-----------------------------------------------------------------------------------

class FbzxBrowserSummary(Screen):
	def __init__(self, session, parent):
		Screen.__init__(self, session, parent = parent)
		self.skinName = ["FbzxBrowserSummary"]

#-----------------------------------------------------------------------------------

class FbzxBrowser(Screen):
	def __init__(self, session, filemode=True):
		Screen.__init__(self, session)
		self.skinName = ["FbzxBrowser"]
		self.__filemode = filemode
		self["title"] = StaticText("Fbzx Browser")
		self["lcdinfo"] = StaticText()
		if self.__filemode:
			self.filelist = FileList(config.plugins.fbzx.romlocation.value, matchingPattern = "^.*\.(z80|Z80|SNA|sna|TAP|tap|TZX|tzx)", showDirectories = True)
		else:
			self.filelist = FileList(config.plugins.fbzx.romlocation.value, showDirectories = True, showFiles = False)
			
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
		if self.__filemode:
			self.setTitle(_("Select a rom for Fbzx"))
		else:
			self.setTitle(_("Select a directory for roms"))
		
	def __setInfo(self):
		self["info"].setText(self["filelist"].getCurrentDirectory())
		self["lcdinfo"].setText(self["filelist"].getCurrent()[1][7])
		
	def createSummary(self):
		return FbzxBrowserSummary

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
		if self.__filemode:
			self.KeyOk()
		elif self["filelist"].getSelection()[0] <> "/autofs/" and self["filelist"].canDescent(): # isDir
			config.plugins.fbzx.romlocation.value = self["filelist"].getCurrentDirectory()
			config.plugins.fbzx.romlocation.save()
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
				
			elif self.__filemode and self["filelist"].getFilename():
				config.plugins.fbzx.romlocation.value = self["filelist"].getCurrentDirectory()
				config.plugins.fbzx.romlocation.save()
				if self["filelist"].getCurrentDirectory().endswith("/"):
					file = self["filelist"].getCurrentDirectory() + self["filelist"].getFilename()
				else:
					file = self["filelist"].getCurrentDirectory() + "/" + self["filelist"].getFilename()
				self.close(file)

	def KeyRed(self):
		self.KeyCancel()

	def KeyCancel(self):
		self.close(None)