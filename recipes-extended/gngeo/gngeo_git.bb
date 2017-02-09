SUMMARY = "A NeoGeo emulator for dreambox"
SECTION = "emulators"
PRIORITY = "optional"
HOMEPAGE="https://github.com/ymartel06/GnGeo-Pi"
AUTHOR = "GeminiTeam"
LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://COPYING;md5=15969273699440f9449cf74b98e9c05f"

SRC_URI = " \
    git://github.com/mdeguzis/gngeo.git;branch=master \
    file://pkg-sdl.patch \
"

SRCREV = "2eb90cebf2500b21b4365c9b6b3081fcedff44cb"
PV = "0.8+git${SRCPV}"
PR = "r0"

inherit autotools-brokensep pkgconfig

DEPENDS = "libsdl \
	zlib \
	"

S = "${WORKDIR}/git"

FILES_${PN} = "/usr/bin/ /usr/share/gngeo/"

do_configure() {
	sed -i -e 's:sdl-config:pkg-config sdl:g' ${S}/src/generator68k/Makefile.am
	sed -i -e 's:sdl-config:pkg-config sdl:g' ${S}/src/generator68k/Makefile.in
	autoreconf -Wcross --verbose --install --force --exclude=autopoint
	chmod 0755 configure
	oe_runconf
}

PARALLEL_MAKE_dm7080 = ""
