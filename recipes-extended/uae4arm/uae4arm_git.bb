SUMMARY = "A fast and optimized Amiga Emulator"
HOMEPAGE = "https://github.com/lubomyr/uae4all2" 
SECTION = "emulators"

LICENSE = "GPLv2" 
LIC_FILES_CHKSUM = "file://COPYING;md5=7215ee9c7d9dc229d2921a40e899ec5f"

SRCREV="3141bf576ebb8068bd5e229f40ad4593aca64366"
BRANCH="master"

PV = "0.1+git${SRCPV}"
PR = "r0"

SRC_URI = "git://github.com/opendreambox/uae4arm-dream.git;protocol=https;branch=${BRANCH};tag=${SRCREV} \
	file://* \
	"


S = "${WORKDIR}/git"

DEPENDS = "libsdl \
	libsdl-ttf \
	libsdl-image \
	libsdl-gfx \
	libpng \
	guichan \
	mpg123 \
	flac \
	libxml2 \
	zlib \
	"

inherit autotools

do_compile() {
	cd ${S}
	oe_runmake -f Makefile.dream
}

do_install() {
	install -d ${D}${bindir}
	install -m 0755 ${S}/uae4arm ${D}${bindir}/uae4arm
}