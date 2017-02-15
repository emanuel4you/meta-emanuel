PRIORITY = "optional"
DEPENDS = "virtual/libsdl \
	libsdl-mixer \
	"

LIC_FILES_CHKSUM = "file://README;md5=3c699e0b4861a65253becfa6f37bbb29"
SECTION = "base"
LICENSE = "GPLv2"

SRCREV = "3dfaba19ea51fb2938cd5e6ce93c70f4ad5ba8be"
BRANCH="master"

PV = "1.30+git${SRCPV}"
PR = "r0"

SRC_URI = "git://github.com/emanuel4you/sdlquake-dreambox.git;protocol=https;branch=${BRANCH};tag=${SRCREV} \
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
	install -m 0755 ${S}/sdlquake ${D}${bindir}/sdlquake
	install -d ${D}${datadir}/games/quake
}
