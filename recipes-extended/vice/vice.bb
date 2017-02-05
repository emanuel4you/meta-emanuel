SUMMARY = "VICE (SDL), the multi-platform C64, C128, VIC20, PET, PLUS4 and CBM-II emulator"
 
MAINTAINER = "Andreas Boose <viceteam@t-online.de> \
Dag Lem <resid@nimrod.no> \
Tibor Biczo <crown@mail.matav.hu> \
Andreas Dehmel <zarquon@t-online.de> \
Thomas Bretz <tbretz@ph.tum.de> \
Andreas Matthies <andreas.matthies@gmx.net> \
Martin Pottendorfer <pottendo@gmx.net> \
Markus Brenner <markus@brenner.de> \
Spiro Trikaliotis <Spiro.Trikaliotis@gmx.de> \
David Hansel <david@hansels.net> \
Daniel Sladic <sladic@eecg.toronto.edu> \
Ettore Perazzoli <ettore@comm2000.it> \
Andre Fachat <fachat@physik.tu-chemnitz.de> \
Teemu Rantanen <tvr@cs.hut.fi> \
Marco van den Heuvel <blackystardust68@yahoo.com> \
Christian Vogelgsang <chris@vogelgsang.org> \
Fabrizio Gennari <fabrizio.ge@tiscali.it> \
M.Kiesel <mayne@users.sourceforge.net> \
Hannu Nuotio <hannu.nuotio@tut.fi> \
Daniel Kahlin <daniel@kahlin.net> \
Antti S. Lankila <alankila@bel.fi> \
Groepaz <groepaz@gmx.net> \
Ingo Korb <ikorb@users.sourceforge.net> \
Errol Smith <strobe@kludgesoft.com> \
Olaf Seibert <rhialto@falu.nl> \
Marcus Sutton <loggedoubt@gmail.com> \
Ulrich Schulz <peiselulli@t-online.de> \
Stefan Haubenthal <polluks@LONESTAR.ORG> \
Thomas Giesel <skoe@directbox.com> \
Kajtar Zsolt <soci@c64.rulez.org> \
Benjamin 'BeRo' Rosseaux <benjamin@rosseaux.com> \
Gemini Team <info@ihad.tv>"

HOMEPAGE = "http://vice-emu.sourceforge.net/"
SECTION = "emulators"
PRIORITY = "optional"

LICENSE = "GPLv2+"
LIC_FILES_CHKSUM = "file://COPYING;md5=c93c0550bd3173f4504b2cbd8991e50b"

DEPENDS = "virtual/libsdl \
	libjpeg-turbo \
	zlib \
	giflib \
	libpng \
"

PV = "2.4.20"
PR = "r1"
PN = "vice"

SRC_URI = "${SOURCEFORGE_MIRROR}/vice-emu/${PN}-${PV}.tar.gz \
	file://pkg-sdl.patch \
"

SRC_URI[md5sum] = "91e083f83b491753923c44a69f0b1839"
SRC_URI[sha256sum] = "e5d3d125940f0fafe409aabeec9de4e3ae8d9c19a731aa7ec6a57f6d2b897c5f"

inherit autotools-brokensep

S = "${WORKDIR}/${PN}-${PV}"

do_configure() {
./configure  --build=x86_64-linux \
		--host=mipsel-oe-linux \
		--target=mipsel-oe-linux \
		--prefix=/usr \
		--exec_prefix=/usr \
		--bindir=/usr/bin \
		--sbindir=/usr/sbin \
		--libexecdir=/usr/lib/vice \
		--datadir=/usr/share \
		--sysconfdir=/etc \
		--sharedstatedir=/com \
		--localstatedir=/var \
		--libdir=/usr/lib \
		--includedir=/usr/include \
		--oldincludedir=/usr/include \
		--infodir=/usr/share/info \
		--mandir=/usr/share/man \
		--enable-sdlui \
		--without-pulse \
		--with-sdlsound \
		--with-uithreads \
		--enable-arch=sdl \
		--disable-lame
}
