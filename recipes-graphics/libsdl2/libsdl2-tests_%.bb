SUMMARY = "Simple DirectMedia Layer Test Applications"
DESCRIPTION = "Simple DirectMedia Layer is a cross-platform multimedia \
library designed to provide low level access to audio, keyboard, mouse, \
joystick, 3D hardware via OpenGL, and 2D video framebuffer."
HOMEPAGE = "http://www.libsdl.org"
BUGTRACKER = "http://bugzilla.libsdl.org/"

SECTION = "tests"

LICENSE = "LGPL-2.1"
LIC_FILES_CHKSUM = "file://../COPYING.txt;md5=e4688d3bd5bf02dadaa3e5182fd9eda9"

BRANCH = "master"

SRCREV = "cd236013164794cfe86d86f61c34af3996ea0fb2"

DEPENDS = "libsdl2 \
	libsdl2-ttf\
	"

SRC_URI = " \
        git://github.com/opendreambox/SDL-mirror.git;protocol=https;branch=${BRANCH};tag=${SRCREV} \
        file://001-disable-testshader.patch \
"
PV = "2.0.5"
RECIPE_PR := "${PR}"
PR = "${RECIPE_PR}-dream1"

S = "${WORKDIR}/git/test"

inherit autotools-brokensep

do_configure_prepend() {
	sed -i -e 's:@GLESLIB@":@GLES2LIB@:g' ${S}/Makefile.in
	cd ${S}
	${S}/autogen.sh
}

do_install() {

    SDL_TESTS_APPS="\
	checkkeys \
	loopwave \
	loopwavequeue \
	testatomic \
	testaudioinfo \
	testaudiocapture \
	testautomation \
	testbounds \
	testcustomcursor \
	testdraw2 \
	testdrawchessboard \
	testdropfile \
	testerror \
	testfile \
	testgamecontroller \
	testgesture \
	testgl2 \
	testgles \
	testgles2 \
	testhaptic \
	testhittesting \
	testrumble \
	testhotplug \
	testthread \
	testiconv \
	testime \
	testintersections \
	testrelative \
	testjoystick \
	testkeys \
	testloadso \
	testlock \
	testmultiaudio \
	testaudiohotplug \
	testnative \
	testoverlay2 \
	testplatform \
	testpower \
	testfilesystem \
	testrendertarget \
	testresample \
	testscale \
	testsem \
	testshape \
	testsprite2 \
	testspriteminimal \
	teststreaming \
	testtimer \
	testver \
	testviewport \
	testwm2 \
	torturethread \
	testrendercopyex \
	testmessage \
	testdisplayinfo \
	testqsort \
	controllermap \
	"
    
    SDL_TESTS_APPS_FILES="axis.bmp button.bmp controllermap.bmp icon.bmp moose.dat picture.xbm sample.bmp \
    sample.wav utf8.txt"

    install -d ${D}${libexecdir}
    for f in $SDL_TESTS_APPS; do 
        install -m 0755 $f ${D}${libexecdir}
    done
    for f in $SDL_TESTS_APPS_FILES; do 
        install -m 0644 ${S}/$f ${D}${libexecdir}
    done
    
    SDL_TESTS_APPS_FILES_EMS="emscripten/*"
    install -d ${D}${libexecdir}/emscripten
    
    for f in $SDL_TESTS_APPS_FILES_EMS; do
	install -m 0644 ${S}/$f ${D}${libexecdir}/emscripten
    done

    SDL_TESTS_APPS_FILES_SHA="shapes/*"
    install -d ${D}${libexecdir}/shapes
    
    for f in $SDL_TESTS_APPS_FILES_SHA; do
	install -m 0644 ${S}/$f ${D}${libexecdir}/shapes
    done
    
}
