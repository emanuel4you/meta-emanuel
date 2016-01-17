#! /bin/sh
MANGLEDIR=`pwd`/mangle.tmp
MODULO=2048

set -e

[ $# -eq 1 ] || { echo specify pristine tar-ball as argument; exit 1; }

[ -r $1 ] || { echo tar-ball $1 is not readable; exit 2; }

rm -fr $MANGLEDIR
mkdir $MANGLEDIR

gzip -d <"$1" | {
  cd $MANGLEDIR
  tar xf -

  cd vice*
  find data/* -type f -exec wc -c '{}' ';' | while read SIZE FILE; do
    if [ $SIZE -eq $(( ( $SIZE / $MODULO ) * $MODULO )) ] || [ "$FILE" = "data/PRINTER/mps803" ] ; then
      echo mangling $FILE $SIZE 1>&2
      echo dummy > $FILE
    fi
  done
  cd ..

  tar cf - * 
} | gzip -c9 >"$1.mangled"

rm -fr $MANGLEDIR

echo Complete with:  mv "$1.mangled" "$1"

exit 0
