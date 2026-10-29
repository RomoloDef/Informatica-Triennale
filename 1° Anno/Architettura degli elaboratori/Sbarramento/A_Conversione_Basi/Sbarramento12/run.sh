#!/bin/bash
#set -x  # Print commands as they run
trap 'echo "Error on line $LINENO"' ERR
if [ "$(uname)" = "Darwin" ]; then
    TMPDIR=$(mktemp -d /tmp/my_build.XXXXXX)
else
    export DISPLAY=:0
    TMPDIR=/dev/shm/my_build
    mkdir -p "$TMPDIR"
    LOCKFILE="/dev/shm/my_build/running.lock"
    exec 9>"$LOCKFILE"
    flock -n 9 || {
        echo "Another compilation in progress. Waiting..."
        flock 9
    }
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
#if [ -e "$ORIG_DIR/test_results.html" ] && [ ! -L "$ORIG_DIR/test_results.html" ]; then
#    # run old_run previously?
#    rm "$ORIG_DIR/test_results.html"
#fi
if [ "$(uname)" = "Darwin" ]; then
    echo "We are on Mac, remember to test on Debian"
    cp ./test_results.html "$ORIG_DIR/test_results.html"
    exit
fi
( exec 9>&-; nohup firefox "$TMPDIR/test_results.html" >/dev/null 2>&1 & )

#ln -s "$(pwd)/test_results.html" "$ORIG_DIR/test_results.html" 2>/dev/null || true

#if [ ! -e "$ORIG_DIR/test_results.html" ]; then
cp ./test_results.html "$ORIG_DIR/test_results.html"
exec 9>&-
#fi