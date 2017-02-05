SUMMARY = "Dos Emulator based on SDL"
SECTION = "emulators"
PRIORITY = "optional"
DEPENDS = "virtual/libsdl \
	libsdl-net \
	zlib \
	libpng \
"
LICENSE = "GPLv2"
HOMEPAGE = "http://www.dosbox.com/"

inherit autotools-brokensep

SRC_URI[md5sum] = "b9b240fa87104421962d14eee71351e8"
SRC_URI[sha256sum] = "13f74916e2d4002bad1978e55727f302ff6df3d9be2f9b0e271501bd0a938e05"

LIC_FILES_CHKSUM = "file://COPYING;md5=94d55d512a9ba36caa9b7df079bae19f"


SRC_URI = "${SOURCEFORGE_MIRROR}/dosbox/dosbox-0.74.tar.gz \
	file://000-update-to-74-2.patch \
	file://pkg-sdl.patch \
"

S = "${WORKDIR}/dosbox-0.74"

PR = "r5"
