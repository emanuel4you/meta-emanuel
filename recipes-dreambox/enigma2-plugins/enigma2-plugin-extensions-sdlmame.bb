LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://COPYING;md5=7215ee9c7d9dc229d2921a40e899ec5f"
SUMMARY = "Arcade Emulator for enigma2"
	
MAINTAINER = "GeminiTeam"
HOMEPAGE = "http://www.i-have-a-dreambox.com"
PACKAGE_ARCH = "mips32el"
SOURCE = "https://github.com/emanuel4you/meta-emanuel"

PV = "0.1"
PR = "r5"
PN = "enigma2-plugin-extensions-sdlmame"

RDEPENDS_${PN} += "advancemame \
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

pkg_preinst_${PN} () {

if [ -f /root/.advance/advmame.rc ];
then
	mv /root/.advance/advmame.rc /root/.advance/advmame.rc.old
fi

}

pkg_postinst_${PN} () {

if [ ! -d /root/.advance ];
then
	mkdir -p /root/.advance
fi

cp /usr/lib/enigma2/python/Plugins/Extensions/SDLMame/advmame.rc.default /root/.advance/advmame.rc

}

pkg_postrm_${PN}() {

rm -rf /usr/lib/enigma2/python/Plugins/Extensions/SDLMame

}