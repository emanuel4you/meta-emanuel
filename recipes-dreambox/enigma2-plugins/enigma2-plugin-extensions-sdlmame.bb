LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://COPYING;md5=7215ee9c7d9dc229d2921a40e899ec5f"
SUMMARY = "Arcade Emulator for enigma2"
	
MAINTAINER = "GeminiTeam"
HOMEPAGE = "http://www.i-have-a-dreambox.com"
PACKAGE_ARCH = "${DEFAULTTUNE}"
SOURCE = "https://github.com/emanuel4you/meta-emanuel"

PV = "0.2"
PR = "r0"
PN = "enigma2-plugin-extensions-sdlmame"

RDEPENDS_${PN} += "advancemame (>= 3.2) \
"

SRC_URI = "file://*"
S = "${WORKDIR}/"

FILES_${PN} += "/usr/lib/enigma2/python/Plugins/Extensions/SDLMame"

inherit autotools-brokensep

#pkg_preinst_${PN}() {
#
#if [ -f /root/.advance/advmame.rc ];
#then
#	mv /root/.advance/advmame.rc /root/.advance/advmame.rc.old
#fi
#
#}

#pkg_postinst_${PN} () {
#
#if [ ! -d /root/.advance ];
#then
#	mkdir -p /root/.advance
#fi
#
#cp /usr/lib/enigma2/python/Plugins/Extensions/SDLMame/advmame.rc.default /root/.advance/advmame.rc
#
#}

pkg_postrm_${PN}() {

rm -rf /usr/lib/enigma2/python/Plugins/Extensions/SDLMame

}