SRCREV="132e1e1984267f316c587957fdd1315c67527ff3"
BRANCH="release-1.2.15"

PV = "1.2.15+git${SRCPV}"

PR = "r0"

SRC_URI = "git://github.com/opendreambox/SDL-mirror.git;protocol=https;branch=${BRANCH};tag=${SRCREV} \
           file://libsdl-1.2.15-xdata32.patch \
           file://pkgconfig.patch \
"

S = "${WORKDIR}/git"

EXTRA_OECONF += "--enable-video-bcmfb \
"

FILESEXTRAPATHS_prepend := "${THISDIR}/../../../openembedded-core/meta/recipes-graphics/libsdl/libsdl-1.2.15:"
