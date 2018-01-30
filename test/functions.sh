set -e

BASEDIR="$(dirname "$(readlink -f "$(dirname "$BASH_SOURCE")")")"
USER="$(id -u -n)"
GROUP="$(id -g -n)"
