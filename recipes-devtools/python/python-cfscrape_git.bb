DESCRIPTION = "A simple Python module to bypass Cloudflare's anti-bot page"
HOMEPAGE = "https://github.com/Anorov/cloudflare-scrape"
SECTION = "devel/python"
LICENSE = "Apache-2.0"
LIC_FILES_CHKSUM = "file://LICENSE;md5=93d4804f061e05530be1a85b24185408"

SRC_URI = "git://github.com/Anorov/cloudflare-scrape.git;protocol=http;branch=master "
SRCREV = "5da4af148f4434fb2d129d58247ce7dac2454b34"

PV = "1.6.6+git${SRCPV}"
PR = "r0"

S = "${WORKDIR}/git"

inherit setuptools

RDEPENDS_${PN} = "python python-requests python-js2py"
