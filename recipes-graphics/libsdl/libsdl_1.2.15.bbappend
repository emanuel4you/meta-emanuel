PR = "r7"

SRC_URI += "\
    file://bcmfb.patch \
"

EXTRA_OECONF = "--disable-static --enable-cdrom --enable-threads --enable-timers \
                --enable-file --disable-oss --disable-esd --disable-arts \
                --disable-diskaudio --disable-nas --disable-esd-shared --disable-esdtest \
                --disable-mintaudio --disable-nasm --disable-video-dga \
                --enable-video-bcmfb --disable-video-ps2gs --disable-video-ps3 \
                --disable-video-dummy \
                --enable-input-events --disable-input-tslib --enable-pthreads \
                --disable-video-fbcon \
                --disable-video-directfb \
                --disable-video-opengl \
                --disable-video-x11 \
                --disable-video-svga \
                --disable-video-picogui --disable-video-qtopia \
                --disable-rpath \
                --disable-pulseaudio \
"

FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

