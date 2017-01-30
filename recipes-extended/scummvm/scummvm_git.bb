require scummvm.inc

LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://COPYING;md5=441c28d2cf86e15a37fa47e15a72fbac"

#SRCREV = "366e164705a920ccd5de9dc606399f9c5b54913c"
#SRCREV = "d750c85fc8da4128f1f7e8ddbb9ffbf9e86cf16f"
SRCREV = "b7469085b596e3d2fc330fe23ec60c76116c2ed7"
BRANCH="master"

PN = "scummvm"
PV = "1.9.0+git${SRCPV}"

DEPENDS = "virtual/libsdl \
	libsdl-net \
	libvorbis \
	libogg \
	zlib \
	curl \
	libmad \
	mpeg2dec \
	flac \
	libjpeg-turbo \
	faad2 \
	libpng \
	libtheora \
"

SRC_URI = "git://github.com/scummvm/scummvm.git;protocol=https;branch=${BRANCH};tag=${SRCREV} \
"

SRC_URI[md5sum] = "ed9098a78022d07fa1482f14325e3ab8"
SRC_URI[sha256sum] = "9cc865c5690bfc1df4970d35984455031467381180a71d84b08dcc9f51e39d4a"

S = "${WORKDIR}/git"


# Make this a plugin enabled build. Bigger binary, less memory usage. Makes more games run on lower end platforms.
# These plugins are not normal Linux shared libs so will fall foul of the sanity checker.
INSANE_SKIP_${PN} = "1"
EXTRA_OECONF += " --enable-plugins --default-dynamic "

# Workaround, because some env variables aren't recognised correctly
do_configure_append() {
	sed -i "s/AS := as/AS := ${AS}/" ${S}/config.mk
	sed -i "s/AR := ar cru/AR := ${AR} cru/" ${S}/config.mk
	sed -i "s/STRIP := strip/STRIP := ${STRIP}/" ${S}/config.mk
	sed -i "s/RANLIB := ranlib/RANLIB := ${RANLIB}/" ${S}/config.mk
}

