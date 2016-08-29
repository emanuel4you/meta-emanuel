DESCRIPTION = "Requests allows you to send organic, grass-fed HTTP1.1 requests, without the need for manual labor."
HOMEPAGE = "https://github.com/kennethreitz/requests"
SECTION = "devel/python"
LICENSE = "Apache-2.0"
LIC_FILES_CHKSUM = "file://LICENSE;md5=d9bb3515869c0f426cb8441c899ae7f5"

SRC_URI = "git://github.com/kennethreitz/requests.git;protocol=http;branch=master "
SRCREV = "58d855e1939cb798bc94f8a21e404f17213e9e92"


PV = "2.11.1+git${SRCPV}"
PR = "r0"

S = "${WORKDIR}/git"

inherit setuptools 

RDEPENDS_${PN} = "python"
