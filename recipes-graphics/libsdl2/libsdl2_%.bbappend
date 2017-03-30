LIC_FILES_CHKSUM = "file://COPYING.txt;md5=e4688d3bd5bf02dadaa3e5182fd9eda9"

BRANCH = "master"

SRC_URI = " \
        git://github.com/opendreambox/SDL-mirror.git;protocol=https;branch=${BRANCH} \
        file://linkage.patch \
"

SRCREV = "${@opendreambox_srcrev('8a60553165db549208dbeb04a14d40f2e36bd401', d)}"


inherit opendreambox-srcrev git-project

PV = "2.0.5"
RECIPE_PR := "${PR}"
PR = "${RECIPE_PR}-dream1"

EXTRA_OECONF += "--enable-video-dreambox \
"
LDFLAGS += "-lEGL -lGLESv2"

FILESEXTRAPATHS_prepend := "${THISDIR}/libsdl2:"
