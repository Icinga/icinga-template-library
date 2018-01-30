Icinga Template Library
=======================

Future home of the Icinga Template Library, or short ITL.

Please do not use this as of now. The README will be updated once we really migrate.

## Import from icinga2

    git clone https://github.com/Icinga/icinga2.git icinga2/

    cd icinga2/
    git checkout -b itl-split

    # if necessary restart
    git reset --hard origin/master

    ../git-itl-filter.sh

    git remote add itl git@github.com:Icinga/icinga-template-library.git
    git push -fu itl itl-split:icinga2-export

    # Merge into local repository
    cd ../
    git fetch origin
    git merge --allow-unrelated-histories origin/icinga2-export

## License

    Copyright (C) 2012-2017 Icinga Development Team <info@icinga.com>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
