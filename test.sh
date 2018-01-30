#!/bin/bash
. "$(dirname "$0")/test/functions.sh"

cd "$BASEDIR/test"

for file in $(ls); do
  test -x "$file" || continue

  echo "[Running test: ${file}]"
  ./"${file}"
done
