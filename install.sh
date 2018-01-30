#!/bin/sh

set -ex

DESTDIR=${DESTDIR:=""}
PREFIX=${PREFIX:="/usr"}
INSTALL_PATH=${INSTALL_PATH:="${PREFIX}/share/icinga2/include"}
OWNER=${OWNER:="root"}
GROUP=${GROUP:="root"}

if [ `id -u` -eq 0 ]; then
  INSTALL_OWNER="--owner=$OWNER --group=$GROUP"
else
  INSTALL_OWNER=
fi
{ set +x; } 2>/dev/null

install_file() {
  set -x
  install -vC $INSTALL_OWNER --mode='0644' "$@"
  { set +x; } 2>/dev/null
}

install_dir() {
  set -x
  install -vd $INSTALL_OWNER --mode='0755' "$@"
  { set +x; } 2>/dev/null
}

install_recursive() {
  local path target
  path="$1"
  target="$2"

  install_dir "${target}"

  for file in $(cd "$path" && ls); do
    if [ -d "${path}/${file}" ]; then
      install_recursive "${path}/${file}" "${target}/${file}"
    else
      install_file "${path}/${file}" "${target}/${file}"
    fi
  done
}

if ! which install >/dev/null; then
  echo "The tool 'install' could not be found in path!" >&2
  exit 1
fi

install_recursive itl "${DESTDIR}${INSTALL_PATH}"

# vi: ts=2 sw=2 expandtab
