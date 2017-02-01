LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://COPYING;md5=7215ee9c7d9dc229d2921a40e899ec5f"
SUMMARY = "ZX Sinclare Emulator for dreambox"
	
MAINTAINER = "GeminiTeam"
HOMEPAGE = "http://www.i-have-a-dreambox.com"
PACKAGE_ARCH = "${DEFAULTTUNE}"
SOURCE = "https://github.com/emanuel4you/meta-emanuel"

PV = "0.1"
PR = "r1"
PN = "enigma2-plugin-extensions-sdlfbzx"

RDEPENDS_${PN} += "fbzx \
"

SRC_URI = "file://*"
S = "${WORKDIR}/"

FILES_${PN} += "/usr/lib/enigma2/python/Plugins/Extensions/SDLFbzx"

inherit autotools-brokensep

pkg_postrm_${PN}() {
rm -rf /usr/lib/enigma2/python/Plugins/Extensions/SDLFbzx
}