#!/bin/sh
if [ "$(uname)" = "Darwin" ]; then
    TMPDIR=$(mktemp -d /tmp/my_build.XXXXXX)
else
    TMPDIR=/dev/shm/my_build
    mkdir -p "$TMPDIR"
fi
ORIG_DIR=$(pwd)

cp -n *.in "$TMPDIR"
cp -n *.expt "$TMPDIR"
cp -n Makefile "$TMPDIR"
cp -n rars1_6.jar "$TMPDIR"
cp program01.asm "$TMPDIR"

cd "$TMPDIR"
rm -f test_results.html
make clean test_results.html
if [ -e "$ORIG_DIR/test_results.html" ] && [ ! -L "$ORIG_DIR/test_results.html" ]; then
    # run old_run previously?
    rm "$ORIG_DIR/test_results.html"
fi
ln -s "$(pwd)/test_results.html" "$ORIG_DIR/test_results.html" 2>/dev/null

if [ ! -e "$ORIG_DIR/test_results.html" ]; then
    cp ./test_results.html "$ORIG_DIR/test_results.html"
fi
