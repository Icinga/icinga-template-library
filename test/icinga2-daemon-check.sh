#!/bin/bash
. "$(dirname "$0")/functions.sh"
set -x

icinga2 daemon -C -DRunAsUser=$USER -DRunAsGroup=$GROUP -DIncludeConfDir="$BASEDIR"/itl
