SUMMARY = "VisualBoyAdvance Emulator for dreambox"
MAINTAINER = "GeminiTeam"
HOMEPAGE = "http://ngemu.com/forums/visualboy-advance-discussion.31/"
LICENSE = "GPLv2"
PACKAGE_ARCH = "${DEFAULTTUNE}"
SECTION = "base"
PRIORITY = "optional"
DEPENDS = "virtual/libsdl \
	zlib \
	libpng \
	readline \
"

SRCREV = "1f88bcf77f5b060e3ca8d1b5958046703835b8c1"
BRANCH="master"

PN = "visualboyadvance"
PV = "1.8.0+git${SRCPV}"
PR = "r0"

SRC_URI = "git://github.com/emanuel4you/VisualBoyAdvance-dreambox.git;protocol=https;branch=${BRANCH};tag=${SRCREV} \
	"

EXTRA_OECONF += "--disable-sdltest \
		--enable-sdl \
		--disable-nls \
"

LIC_FILES_CHKSUM = "file://COPYING;md5=393a5ca445f6965873eca0259a17f833"

S = "${WORKDIR}/git"

inherit autotools gettext
