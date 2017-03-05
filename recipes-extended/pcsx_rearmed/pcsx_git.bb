SUMMARY = "Sony Playstation Emulator"
SECTION = "emulators"
PRIORITY = "optional"
HOMEPAGE="https://github.com/notaz/pcsx_rearmed"
AUTHOR = "GeminiTeam"
LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://COPYING;md5=5dd99a4a14d516c44d0779c1e819f963"

SRC_URI = " \
    git://github.com/notaz/pcsx_rearmed.git;branch=master \
    file://001-move-dir-to-home.patch \
    file://pkg-config_sdl.patch \
"

SRCREV = "25e52b2c51afd3609aa2a0e218036d27520af510"
PV = "1.9+git${SRCPV}"
PR = "r1"

inherit autotools-brokensep pkgconfig

DEPENDS = "libsdl \
	zlib \
	libpng \
	"

S = "${WORKDIR}/git"

FILES_${PN} += "/usr/games/ /usr/games/plugins/"

do_configure() {
	git submodule init && git submodule update
	CFLAGS="${TUNE_CCARGS}"
	./configure
	sed -i -e 's:/.picodrive/:/.pcsx/.picodrive/:' ${S}/frontend/libpicofe/linux/plat.c
}

do_install() {
	install -d ${D}/usr/games
	install -m 0755 ${S}/pcsx ${D}/usr/games/pcsx
	install -d ${D}/usr/games/plugins 
	install -m 0755 ${S}/plugins/gpu_peops.so ${D}/usr/games/plugins/gpu_peops.so
	install -m 0755 ${S}/plugins/gpu_unai.so ${D}/usr/games/plugins/gpu_unai.so
	install -m 0755 ${S}/plugins/spunull.so ${D}/usr/games/plugins/spunull.so
}