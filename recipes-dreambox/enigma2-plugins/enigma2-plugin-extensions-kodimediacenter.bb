LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://COPYING;md5=7215ee9c7d9dc229d2921a40e899ec5f"
SUMMARY = "Kodi MediaCenter for enigma2"
	
MAINTAINER = "GeminiTeam"
HOMEPAGE = "http://www.i-have-a-dreambox.com"
SOURCE = "https://github.com/emanuel4you/meta-emanuel"

PV = "0.1"
PR = "r0"
PN = "enigma2-plugin-extensions-kodimediacenter"

DEPENDS += "systemd"

RDEPENDS_${PN} += "kodi \
"

SRC_URI = "file://*"
S = "${WORKDIR}/"

FILES_${PN} += "/usr/lib/enigma2/python/Plugins/Extensions/XBMCMediaCenter"
FILES_${PN} += "${libdir}/enigma2 ${systemd_unitdir}"
FILES_${PN} += "${datadir}/enigma2/menu"

inherit allarch autotools-brokensep systemd

pkg_postrm_${PN}() {
rm -rf /usr/lib/enigma2/python/Plugins/Extensions/XBMCMediaCenter
}

do_install_append () {
	install -d ${D}${systemd_unitdir}/system
	install -c -m 644 ${S}/xbmc.service.in ${D}${systemd_unitdir}/system/xbmc.service
}

