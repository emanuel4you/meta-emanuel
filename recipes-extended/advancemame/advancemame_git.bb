DESCRIPTION = "AdvanceMame Arcade emulator"
LICENSE = "GPLv2"
RDEPENDS_${PN} = "libsdl alsa-lib ncurses-terminfo zlib expat"
DEPENDS = "libsdl \
	freetype \
"
HOMEPAGE = "http://www.advancemame.it"

LIC_FILES_CHKSUM = "file://COPYING;md5=8ca43cbc842c2336e835926c2166c28b"

#SRCREV = "fdd33b5f5d803aaae3109b5d18a6a90012f490cd"
#SRCREV = "7c2653bded5fd296f1d2a1618769f90d9283d058"
#SRCREV = "e047d2c1d339817baccec8a49fb40508756ba27b"
#SRCREV = "efb73a9ceb9118176ec7c6833a92cf1dd9ffd138"
SRCREV = "7f7abff1dd300921107084c905896d88b2f4f8e1"

BRANCH="master"

PN = "advancemame"
PV = "3.2+git${SRCPV}"
PR = "r1"

SRC_URI = "git://github.com/amadvance/advancemame.git;protocol=https;branch=${BRANCH};tag=${SRCREV} \
	file://configure.patch \
	"

S = "${WORKDIR}/git"

inherit autotools-brokensep pkgconfig

CFLAGS =+ " -I${STAGING_INCDIR}/SDL/ -I${STAGING_INCDIR}/ -DUSE_SMP"
LDFLAGS =+ " -lSDL -lpthread"

do_configure_prepend() {
	${S}/autogen.sh
}

EXTRA_OECONF = " \
                 --enable-pthread \
                 --docdir=${docdir}/advance/ \
                 --enable-sdl \
                 --enable-mevent \
               "
               

do_install() {
	install -d ${D}${bindir}
	install -m 0755 ${S}/advmame ${D}${bindir}/advmame
	install -m 0755 ${S}/advmenu ${D}${bindir}/advmenu
	install -m 0755 ${S}/advmess ${D}${bindir}/advmess
#	install -m 0755 ${S}/advcfg ${D}${bindir}/advcfg
#	install -m 0755 ${S}/advv ${D}${bindir}/advv
#	install -m 0755 ${S}/advs ${D}${bindir}/advs
#	install -m 0755 ${S}/advj ${D}${bindir}/advj
#	install -m 0755 ${S}/advk ${D}${bindir}/advk
#	install -m 0755 ${S}/advm ${D}${bindir}/advm
	
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

FILES_${PN} += "${datadir}/advance/* /usr/bin/* \
                     "
pkg_postinst_${PN} () {
#! /bin/sh
set -e

if [ x"$D" = "x" ]; then
	# On target
	if [ -f /root/.advance/advmame.rc ]; then
		DATE=`date +"%Y%m%d%H%M"`
		cp -a /root/.advance/advmame.rc /root/.advance/advmame.rc.$DATE
	fi
	/usr/bin/advmame --default
	
	if [ -f /root/.advance/advmenu.rc ]; then
		DATE=`date +"%Y%m%d%H%M"`
		cp -a /root/.advance/advmenu.rc /root/.advance/advmenu.rc.$DATE
	fi
	/usr/bin/advmenu --default
	
	if [ -f /root/.advance/advmess.rc ]; then
		DATE=`date +"%Y%m%d%H%M"`
		cp -a /root/.advance/advmess.rc /root/.advance/advmess.rc.$DATE
	fi
	/usr/bin/advmess --default
else
    exit 0
fi

}

                     