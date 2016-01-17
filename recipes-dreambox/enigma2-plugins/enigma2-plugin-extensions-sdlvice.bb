LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://COPYING;md5=7215ee9c7d9dc229d2921a40e899ec5f"
SUMMARY = "Vice Emulator for enigma2"
	
MAINTAINER = "GeminiTeam"
HOMEPAGE = "http://www.i-have-a-dreambox.com"
PACKAGE_ARCH = "mips32el"
SOURCE = "https://github.com/emanuel4you/meta-emanuel"

PV = "0.1"
PR = "r1"
PN = "enigma2-plugin-extensions-sdlvice"

RDEPENDS_${PN} += "vice \
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
#	ginstall.py add '("Games", "1", "C64", "", "Plugins.Extensions.SDLVice.vice", "Vice", "", "/usr/lib/enigma2/python/Plugins/Extensions/SDLVice/icon_x64.png", "", "")' path=/etc/enigma2/gemini_desktop.xml
#fi
#}

pkg_postrm_${PN}() {
rm -rf /usr/lib/enigma2/python/Plugins/Extensions/SDLVice
#if [ -f /usr/bin/ginstall.py ]; then
#	ginstall.py remove '("Games", "", "C64", "", "", "", "", "", "", "")' path=/etc/enigma2/gemini_desktop.xml
#fi
}