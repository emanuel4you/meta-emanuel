PR = "r4"

SRC_URI += "file://bcmfb.patch \
          "

EXTRA_OECONF = "--disable-static --enable-cdrom --enable-threads --enable-timers --enable-endian \
                --enable-file --disable-oss --disable-esd --disable-arts \
                --disable-diskaudio --disable-nas --disable-esd-shared --disable-esdtest \
                --disable-mintaudio --disable-nasm --disable-video-dga \
                --enable-video-bcmfb --disable-video-ps2gs --disable-video-ps3 \
                --disable-video-xbios --disable-video-gem --disable-video-dummy \
                --enable-input-events --disable-input-tslib --enable-pthreads \
                --disable-video-fbcon \
                --disable-video-directfb \
                --disable-video-opengl \
                --disable-video-x11 \
                --disable-video-svga \
                --disable-video-picogui --disable-video-qtopia --enable-dlopen \
                --disable-rpath \
                --disable-pulseaudio \
"

FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"
