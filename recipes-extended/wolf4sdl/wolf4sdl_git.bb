PRIORITY = "optional"
DEPENDS = "virtual/libsdl \
	libsdl-mixer \
	"

LIC_FILES_CHKSUM = "file://license-id.txt;md5=6372b65e755633128ef61f364d5dcce5"
SECTION = "base"
LICENSE = "Proprietary"


SRCREV = "5387b99d32fc5bac39c87defcb0abbf1018d8083"
BRANCH="master"

PV = "1.7+git${SRCPV}"
PR = "r0"

SRC_URI = "git://github.com/mozzwald/wolf4sdl.git;protocol=https;branch=${BRANCH};tag=${SRCREV} \
	file://dreambox.patch \
	   " 	

FILES_${PN} += "/usr/bin /usr/share"

inherit autotools

S = "${WORKDIR}/git"

do_compile() {
	cd ${S}
	oe_runmake -f Makefile
}

do_install() {
	install -d ${D}${bindir}
	install -m 0755 ${S}/wolf3d ${D}${bindir}/wolf3d
	install -d ${D}${datadir}/games/wolf3d
}

SRC_URI[md5sum] = "cde6afcfc85ef46ee6f385e5e92db1ee"
SRC_URI[sha256sum] = "37eae610a19452745f0d0da769fb71a276293859d0a757df8a8bc3f799880cce"
