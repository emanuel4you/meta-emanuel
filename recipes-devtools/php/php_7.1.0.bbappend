FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"


PACKAGECONFIG_append = "mysql sqlite3 apache2"

CFLAGS_append = " -pthread -lcurl -I${STAGING_INCDIR_NATIVE}/apache2"

DEPENDS += "curl openssl gd freetype readline"

SRC_URI += "file://001-gd-without-xmp.patch"

EXTRA_OECONF += "--with-fpm-group=www-data \
	--with-fpm-user=www-data \
	--with-curl=${STAGING_BINDIR}/.. \
	--with-openssl=${STAGING_BINDIR}/.. \
	--with-gd=${STAGING_LIBDIR}/.. \
	--with-freetype-dir=${STAGING_INCDIR}/freetype2 \
	--with-readline \
	--enable-gd-native-ttf \
"
do_install_prepend_class-native() {
    install -d ${D}${STAGING_ETCDIR_NATIVE}
    printf "\nLoadModule dummy_module modules/mod_dummy.so\n" >  ${D}${STAGING_ETCDIR_NATIVE}/httpd.conf
}


do_install_prepend_class-target() {
echo
}