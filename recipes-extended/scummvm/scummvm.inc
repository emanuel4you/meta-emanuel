DESCRIPTION = "Virtual Machine for several classic graphical point-and-click adventure games"
HOMEPAGE = "http://www.scummvm.org"
SECTION = "emulators"
PRIORITY = "optional"
LICENSE = "GPL"

SRC_URI = "${SOURCEFORGE_MIRROR}/scummvm/scummvm-${PV}.tar.bz2"

inherit autotools-brokensep pkgconfig

EXTRA_OECONF = "--host=${HOST_SYS} \
		--backend=sdl \
		--disable-alsa \
		--prefix=${prefix} \
		--with-ogg-prefix=${STAGING_LIBDIR}/.. \
		--with-vorbis-prefix=${STAGING_LIBDIR}/.. \
		${@base_conditional('ENTERPRISE_DISTRO', '1', '--disable-mpeg2', '--with-mpeg2-prefix=${STAGING_LIBDIR}/..', d)} \
		${@base_conditional('ENTERPRISE_DISTRO', '1', '--disable-mad', '--with-mad-prefix=${STAGING_LIBDIR}/..', d)} \
		"

EXTRA_OEMAKE = "MANDIR=${mandir}"

do_configure() {
	./configure ${EXTRA_OECONF}
}
