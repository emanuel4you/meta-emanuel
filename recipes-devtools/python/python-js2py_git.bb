DESCRIPTION = "JavaScript to Python Translator and JavaScript interpreter written in 100% pure Python."
HOMEPAGE = "https://github.com/PiotrDabkowski/Js2Py"
SECTION = "devel/python"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://LICENSE.md;md5=faa744092d3fb3314632e815e7c3a560"

SRC_URI = "git://github.com/PiotrDabkowski/Js2Py.git;protocol=http;branch=master "
SRCREV = "144b1701faf0b97900a73978ae8f87ca80f0a079"

PV = "0.39+git${SRCPV}"
PR = "r0"

S = "${WORKDIR}/git"

inherit setuptools 

RDEPENDS_${PN} = "python python python-six"

