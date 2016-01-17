SUMMARY = "Gameboy Emulator based on SDL"
MAINTAINER = "GeminiTeam"
HOMEPAGE = "http://www.i-have-a-dreambox.com"
PACKAGE_ARCH = "mips32el"
SECTION = "emulators"
PRIORITY = "optional"
DEPENDS = "virtual/libsdl"

LIC_FILES_CHKSUM = "file://COPYING;md5=8ca43cbc842c2336e835926c2166c28b"
LICENSE = "GPL"

SRCREV="32d122935914526db3267903027e9077b0f4594b"
BRANCH="master"

PV = "1.0.4+git${SRCPV}"
PR = "r0"
PN = "gnuboy"


SRC_URI += "git://github.com/rofl0r/gnuboy.git;protocol=https;branch=${BRANCH};tag=${SRCREV}"

S = "${WORKDIR}/git"

inherit autotools

do_configure_prepend() {
 sed -i -e 's:LIBS="$LIBS -L/usr/local/lib -L/usr/X11R6/lib": :g' ${S}/configure.in
}

do_install() {
	install -d ${D}${bindir}
#	install -m 0755 ${S}/fbgnuboy ${D}${bindir}/fbgnuboy
	install -m 0755 ${S}/sdlgnuboy ${D}${bindir}/sdlgnuboy
	install -d ${D}${docdir}/gnuboy
	install -m 0644 ${S}/docs/CONFIG ${D}${docdir}/gnuboy/CONFIG
	install -m 0644 ${S}/docs/FAQ ${D}${docdir}/gnuboy/FAQ
	install -m 0644 ${S}/etc/classic.rc ${D}${docdir}/gnuboy/classic.rc
	install -m 0644 ${S}/etc/sample.rc ${D}${docdir}/gnuboy/sample.rc
	install -m 0644 ${S}/etc/filters.rc ${D}${docdir}/gnuboy/filters.rc
}

