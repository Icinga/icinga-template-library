#!/bin/bash
# Note: with packages this test must be run with sudo
. "$(dirname "$0")/functions.sh"
set -x

icinga2 daemon -C -DRunAsUser=$USER -DRunAsGroup=$GROUP -DIncludeConfDir="$BASEDIR"/itl
