SUMMARY = "Multi-platform Super Nintendo emulator (SDL version)"
HOMEPAGE = "http://www.snes9x.com/"
SECTION = "emulators"
PRIORITY = "optional"

PROVIDES += "virtual/snes9x"

LICENSE = "GPLv2 & LGPLv2.1" 
LIC_FILES_CHKSUM = "file://../docs/snes9x-license.txt;md5=2990ee23aa20730e9a67366f467e0991 \
	file://../docs/gpl-2.0.txt;md5=751419260aa954499f7abaabaa882bbe \
	file://../docs/lgpl-2.1.txt;md5=243b725d71bb5df4a1e5920b344b86ad \
	" 

SRCREV = "e5bbaa3a0ce3d79b9c76fa5b744a70c97ebe7661"
BRANCH="master"

PV = "1.53+git${SRCPV}"

SRC_URI = "git://github.com/emanuel4you/snes9x-sdl.git;protocol=https;branch=${BRANCH};tag=${SRCREV} \
	file://cross_compile.patch;striplevel=2 \
	file://001-enable-SDL-joystick.patch;striplevel=2 \
	file://002-enable-debug_key.patch;striplevel=2 \
	file://003-addkey.patch;striplevel=2 \
"

S = "${WORKDIR}/git/sdl"

DEPENDS = "virtual/libsdl libpng"

inherit autotools-brokensep

#EXTRA_OECONF += "--enable-debug --enable-debugger"

do_install() {
	install -d ${D}${bindir}
	install -m 0755 snes9x-sdl ${D}${bindir}
	install -d ${D}${docdir}/snes9x-sdl
	install -m 0644 ${S}/docs/control-inputs.txt ${D}${docdir}/snes9x-sdl/control-inputs.txt
	install -m 0644 ${S}/docs/readme_unix.html ${D}${docdir}/snes9x-sdl/readme_unix.html
	install -m 0644 ${S}/docs/snes9x-sdl.conf ${D}${docdir}/snes9x-sdl/snes9x-sdl.conf
}
