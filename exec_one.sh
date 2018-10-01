echo "$1"
(cd $1 && hd_metaexp ) || (echo "$1 errored"; exit 1 ) || exit 1
