SUMMARY = "The shellinaboxd daemon implements a webserver that listens on the specified port. \
The web server publishes one or more services that will be displayed in a VT100 emulator implemented as an AJAX web application."
MAINTAINER = "GeminiTeam"
HOMEPAGE = "https://github.com/shellinabox/shellinabox/wiki"
PACKAGE_ARCH = "mips32el"
SECTION = "terminal"
PRIORITY = "optional"

RDEPENDS_${PN} += "openssl"

LIC_FILES_CHKSUM = "file://COPYING;md5=a193d25fdef283ddce530f6d67852fa5"
LICENSE = "GPLv2"

#SRCREV="2c93404bd0b2b3dac244b3664741603f9a619664"
SRCREV="0c8c295c1af04f357eb60ab263822c45df5b1031"
BRANCH="master"

PV = "2.20+git${SRCPV}"
PR = "r0"
PN = "shellinabox"

EXTRA_OECONF = " \
                  --disable-runtime-loading --disable-pam \
               "

SRC_URI += "git://github.com/shellinabox/shellinabox;protocol=https;branch=${BRANCH};tag=${SRCREV} \
	file://* \
	"

S = "${WORKDIR}/git"

inherit autotools systemd

SYSTEMD_SERVICE_${PN} = "shellinabox.service"

do_install_append() {
	install -d ${D}${systemd_unitdir}/system
	install -c -m 644 ${S}/shellinabox.service.in ${D}${systemd_unitdir}/system/shellinabox.service
	
	install -d ${D}${sysconfdir}/default
	install -c -m 644 ${S}/shellinaboxd.default ${D}${sysconfdir}/default/shellinaboxd
}

pkg_preinst_${PN} () {
	CERT="/etc/${PN}/certificate.pem"
	BOX=`cat /proc/stb/info/model`
	
	if [ ! -d "/etc/${PN}" ]
	then
		mkdir -p "/etc/${PN}"
		chmod 0755 "/etc/${PN}"
	fi

	if [ -f "${CERT}" ]
	then
		rm "${CERT}"
	fi
	
	openssl req -new -x509 -keyout "${CERT}" -out "${CERT}" -days 5500 -nodes -subj "/C=DE/ST=Home/L=Home/O=Dreambox/OU=STB/CN=${BOX}" && chmod 644 "${CERT}"
}

pkg_postrm_${PN} () {
	rm -rf "/etc/${PN}"
}

