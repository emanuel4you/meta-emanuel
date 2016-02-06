DESCRIPTION = "AdvanceMame Arcade emulator"
LICENSE = "GPLv2"
RDEPENDS_${PN} = "libsdl alsa-lib ncurses-terminfo zlib expat"
DEPENDS = "libsdl"
HOMEPAGE = "http://www.advancemame.it"

LIC_FILES_CHKSUM = "file://COPYING;md5=8ca43cbc842c2336e835926c2166c28b"

SRCREV = "fdd33b5f5d803aaae3109b5d18a6a90012f490cd"
BRANCH="master"

PN = "advancemame"
PV = "1.5.0+git${SRCPV}"
PR = "r1"

SRC_URI = "git://github.com/amadvance/advancemame.git;protocol=https;branch=${BRANCH};tag=${SRCREV} \
	file://configurerc.patch \
	  "
S = "${WORKDIR}/git"

inherit autotools

CFLAGS =+ " -I${STAGING_INCDIR}/SDL/ -I${STAGING_INCDIR}/ -DUSE_SMP"
LDFLAGS =+ " -lSDL -lpthread"

do_configure_prepend() {
	${S}/autogen.sh
}

EXTRA_OECONF = " \
                 --enable-pthread \
                 --docdir=${docdir}/advance/ \
               "

do_install() {
	install -d ${D}/${bindir}
	install -m 0755 ${S}/obj/mame/linux/blend/advmame ${D}${bindir}/advmame
	install -m 0755 ${S}/obj/menu/linux/blend/advmenu ${D}${bindir}/advmenu
#	install -m 0755 ${S}/obj/cfg/linux/blend/advcfg ${D}${bindir}/advcfg
#	install -m 0755 ${S}/obj/v/linux/blend/advv ${D}${bindir}/advv
#	install -m 0755 ${S}/obj/s/linux/blend/advs ${D}${bindir}/advs
#	install -m 0755 ${S}/obj/j/linux/blend/advj ${D}${bindir}/advj
#	install -m 0755 ${S}/obj/k/linux/blend/advk ${D}${bindir}/advk
#	install -m 0755 ${S}/obj/m/linux/blend/advm ${D}${bindir}/advm
	
	install -d ${D}/${datadir}/advance/
	install -d ${D}/${datadir}/advance/sample
	install -d ${D}/${datadir}/advance/artwork
	install -d ${D}/${datadir}/advance/image
	install -d ${D}/${datadir}/advance/crc
	install -d ${D}/${datadir}/advance/snap
	install -d ${D}/${datadir}/advance/rom
	
	install -d ${D}/${docdir}/advance
	install -m 0644 ${S}/doc/*.txt ${D}${docdir}/advance
	install -m 0644 ${S}/doc/*.html ${D}${docdir}/advance
}

FILES_${PN} += "${datadir}/advance/* \
                     "
