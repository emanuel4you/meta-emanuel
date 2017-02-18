SUMMARY = "Gameboy Emulator based on SDL"
MAINTAINER = "GeminiTeam"
HOMEPAGE = "http://www.i-have-a-dreambox.com"
PACKAGE_ARCH = "${DEFAULTTUNE}"
SECTION = "emulators"
PRIORITY = "optional"
DEPENDS = "virtual/libsdl"

RDEPENDS_${PN} += "zlib"

LIC_FILES_CHKSUM = "file://COPYING;md5=8ca43cbc842c2336e835926c2166c28b"
LICENSE = "GPLv2"

SRCREV="9d7e1f4c964ba5b902d10a62422b140a6eb3da7d"
BRANCH="master"

PV = "1.0.5+git${SRCPV}"
PR = "r0"
PN = "gnuboy"

SRC_URI += "git://github.com/emanuel4you/gnuboy-dreambox.git;protocol=https;branch=${BRANCH};tag=${SRCREV} \
"

S = "${WORKDIR}/git"

inherit autotools-brokensep pkgconfig

EXTRA_OECONF = " \
	--with-sdl \
"
do_compile() {
	oe_runmake sdlgnuboy
}


do_install() {
	install -d ${D}${bindir}
	install -m 0755 ${S}/sdlgnuboy ${D}${bindir}/sdlgnuboy
	install -d ${D}${docdir}/gnuboy
	install -m 0644 ${S}/docs/CONFIG ${D}${docdir}/gnuboy/CONFIG
	install -m 0644 ${S}/docs/FAQ ${D}${docdir}/gnuboy/FAQ
	install -m 0644 ${S}/etc/classic.rc ${D}${docdir}/gnuboy/classic.rc
	install -m 0644 ${S}/etc/sample.rc ${D}${docdir}/gnuboy/sample.rc
	install -m 0644 ${S}/etc/filters.rc ${D}${docdir}/gnuboy/filters.rc
}
