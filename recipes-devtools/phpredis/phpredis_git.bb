DESCRIPTION = "A PHP extension for Redis"
HOMEPAGE = "https://github.com/phpredis"
SECTION = "utils"
LICENSE = "Proprietary"
LIC_FILES_CHKSUM = "file://COPYING;md5=cb564efdf78cce8ea6e4b5a4f7c05d97"

PACKAGE_ARCH = "${DEFAULTTUNE}"

SRCREV="8a0ecbc162f7ffbd5251a05022947d5d0d8a3efb"
BRANCH="php7"

PV = "3.1.1-2+git${SRCPV}"
PR = "r0"
PN = "phpredis"

DEPENDS = "php"

SRC_URI = "git://github.com/phpredis/phpredis.git;protocol=https;branch=${BRANCH};tag=${SRCREV} \
"

SRC_URI[md5sum] = "e30f1a0e45b440443c044148fb62ad6e"
SRC_URI[sha256sum] = "ac8c0a6b6aaf0702411e71dd3626c655287c903233b659389fc07113114c9de3"

inherit autotools-brokensep pkgconfig

S = "${WORKDIR}/git"


do_configure_prepend () {
	mkdir -p ${S}/aclocal-copy
	mkdir -p ${S}/build/aclocal-copy
	mkdir -p ${WORKDIR}/build/aclocal-copy
	cd ${S}
	phpize
}

do_compile() {
	cd ${S}
	oe_runmake || die "make failed"
}

do_install() {
install -d ${D}${sysconfdir}
echo "extension=redis.so" > ${D}${sysconfdir}/redis.ini
install -d "${D}${libdir}/php5"
install -m 0755 "${S}/.libs/redis.so" "${D}${libdir}/php5/redis.so"

}

FILES_${PN} += "/etc /usr/lib"

SSTATE_SCAN_FILES += "phpize"