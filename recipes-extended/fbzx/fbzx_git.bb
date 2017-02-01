SUMMARY = "A Sinclair Spectrum emulator, designed to work at full screen using the FrameBuffer"
SECTION = "emulators"
PRIORITY = "optional"
HOMEPAGE="https://github.com/rastersoft/fbzx"
AUTHOR = "GeminiTeam"
LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://COPYING;md5=d32239bcb673463ab874e80d47fae504"

SRC_URI = " \
    git://github.com/rastersoft/fbzx.git;branch=master \
    file://fix-Makefiles.patch \
"

SRCREV= "981d48272e1cd04ce258e1060fd9574dd6bb4a60"
PV = "3.1.0+git${SRCPV}"
PR = "r0"

inherit pkgconfig autotools-brokensep

DEPENDS = "libsdl \
	alsa-lib \
	"

S = "${WORKDIR}/git"

EXTRA_OEMAKE = ""

FILES_${PN} += "/usr/bin /usr/share/spectrum-roms/"

do_compile() {
	oe_runmake -f Makefile
}