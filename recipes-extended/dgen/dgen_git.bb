SUMMARY = "A Sega - Genesis, Sega CD, 32X Emulator"
SECTION = "emulators"
PRIORITY = "optional"
HOMEPAGE="https://sourceforge.net/projects/dgen/"
AUTHOR = "GeminiTeam"
LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://COPYING;md5=43021d83808b3cc4e00b77ab1c558847"

SRC_URI = " \
    git://git.code.sf.net/p/dgen/dgen.git;branch=master \
    file://pkg-sdl.patch \
    file://bcmfb-sdl.patch \
"

SRCREV = "a6f61a594b996840110a6c4bc0347a9d8e4f81e7"
PV = "1.33+git${SRCPV}"
PR = "r0"

inherit autotools-brokensep pkgconfig

DEPENDS = "libsdl \
	libarchive \
	"

S = "${WORKDIR}/git"

FILES_${PN} += "/usr/bin"

do_configure() {
	${S}/autogen.sh
	oe_runconf --enable-threads --disable-asm
}