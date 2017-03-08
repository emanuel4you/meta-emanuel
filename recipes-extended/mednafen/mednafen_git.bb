SUMMARY = "Command-line-driven multi-system emulator using SDL"
HOMEPAGE = "http://mednafen.sourceforge.net/"
SECTION = "emulators"

LICENSE = "GPLv3" 
LIC_FILES_CHKSUM = "file://COPYING;md5=6e233eda45c807aa29aeaa6d94bc48a2"

SRCREV="ffdafe23387a0d1482699723b4b2d491d799fa73"
BRANCH="master"

PV = "0.9.43+git${SRCPV}"
PR = "r0"
PN = "mednafen"

SRC_URI += "git://github.com/emanuel4you/mednafen-dreambox.git;protocol=https;branch=${BRANCH};tag=${SRCREV} \
"

S = "${WORKDIR}/git"

DEPENDS = "libsdl \
	jack \
	libsndfile1 \
	"

# large file support was generating a cross-compiling issue where sizeof(off_t) was 
# returning 64 instead of 32, so we are disabling it for now
#EXTRA_OECONF += "--disable-largefile"

inherit autotools-brokensep gettext
