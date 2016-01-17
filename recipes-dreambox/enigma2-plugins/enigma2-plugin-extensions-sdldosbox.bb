LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://COPYING;md5=7215ee9c7d9dc229d2921a40e899ec5f"
SUMMARY = "Dos Emulator for enigma2"
	
MAINTAINER = "GeminiTeam"
HOMEPAGE = "http://www.i-have-a-dreambox.com"
PACKAGE_ARCH = "mips32el"
SOURCE = "ftp://www.unknown.com"

PV = "0.1"
PR = "r1"
PN = "enigma2-plugin-extensions-sdldosbox"

RDEPENDS_${PN} += "dosbox \
 fbset-modes (>= 0.1.0-r6.2) \
"

SRC_URI = "file://${PN}/*"
S = "${WORKDIR}/"

FILES_${PN} += "${datadir}"
FILES_${PN} += "${libdir}"

inherit autotools pkgconfig

bindir = "/usr/bin"
sbindir = "/usr/sbin"
libdir = "/usr/lib"
datadir = "/usr/share"

#do_install_append_${PN}() {
#}

#pkg_postinst_${PN}() {
#if [ -f /usr/bin/ginstall.py ]; then
#	ginstall.py add '("Games", "1", "DosBox", "", "Plugins.Extensions.SDLDosBox.dosbox", "DosBox", "", "/usr/lib/enigma2/python/Plugins/Extensions/SDLDosBox/icon_dosbox.png", "", "")' path=/etc/enigma2/gemini_desktop.xml
#fi
#}

pkg_postrm_${PN}() {
rm -rf /usr/lib/enigma2/python/Plugins/Extensions/SDLDosBox
#if [ -f /usr/bin/ginstall.py ]; then
#	ginstall.py remove '("Games", "", "DosBox", "", "", "", "", "", "", "")' path=/etc/enigma2/gemini_desktop.xml
#fi
}