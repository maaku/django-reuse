#!/bin/sh

##
# django-reuse: bin/bootstrap.sh
#
# This file is a stand-alone script which sets up a Django development
# environment using the django-reuse toolkit.
##

##
# Copyright (C) 2009, Mark Friedenbach <mark.friedenbach@nasa.gov>
#
#   This program is free software: you can redistribute it and/or modify it
#   under the terms of version 3 of the GNU Affero General Public License as
#   published by the Free Software Foundation.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU General Public License along
#   with this source code; if not, see <http://www.gnu.org/licenses/>,
#   or write to
#
#     Free Software Foundation, Inc.
#     51 Franklin Street, Fifth Floor
#     Boston, MA  02110-1301  USA
##

##
# Print a short usage statement if one of the help arguments is encountered.
function print_usage() {
    echo "Usage: `basename $0` [<dev_dir>]"
    echo "Where (optional) dev_dir is the directory in which"
    echo "the development environment is to be set up."
    exit
}

if [ "-h"     = "$1" ]; then
    print_usage
fi

if [ "--help" = "$1" ]; then
    print_usage
fi

if [ "--usage" = "$1" ]; then
    print_usage
fi

##
# Parse the command line (pretty simple).  Print an error message if there are
# any problems.
function parse_error() {
    echo "`basename $0`: try \``basename $0` --help\` for instructions."
    exit -1
}

if [ $# -gt 1 ]; then
    echo "`basename $0`: error, too many parameters."
    parse_error
fi

if [ $# -eq 1 ]; then
    if [ ! -d $1 ]; then
        if [ ! -e $1 ]; then
            mkdir $1
        else
            echo "`basename $0`: error, \"$1\" does not exist or is not a directory."
            parse_error
        fi
    fi
fi

##
# Switch to the directory specified.  All commands issued from here on out
# will be relative to this working directory.
#
# Added by Mark Friedenbach 29 Jul 2009
# of "2> /dev/null" to prevent output of an error message when no directory is
# specified.
pushd $1 > /dev/null 2> /dev/null

##
# Some sanity checks... the directory django-reuse should not exist, nor
# should the file manage.py.
if [ -e "django-reuse" ]; then
    echo "`basename $0`: error, file/directory django-reuse already exists."
    exit
fi
if [ -e "manage.py" ]; then
    echo "`basename $0`: error, file/directory manage.py already exists."
    exit
fi

##
# The django-reuse package is stored on github.  If git exists on the function
# local workstation, then we can clone the repository which will let the user
# easily update django-reuse later.  Otherwise we'll just download the latest
# tarball.
if [ `which git` ]; then
    echo "git exists :) cloning django-reuse..."
    git clone git://github.com/maaku/django-reuse.git
else
    echo "git not found :( downloading django-reuse tarball..."
    wget http://github.com/maaku/django-reuse/tarball/master
    tar zxvf *-django-reuse-*.tar.gz
    rm -f *-django-reuse-*.tar.gz
    mv *-django-reuse-* django-reuse
fi

##
# Now the repository exists in the directory django-reuse.  We'll create a
# symbolic link to the script django-reuse/bin/manage.py
ln -s django-reuse/bin/manage.py manage.py

##
# FIXME: this should be moved to 'manage.py bootstrap'
wget http://www.djangoproject.com/download/1.1.1/tarball/
tar zxvf Django-1.1.1.tar.gz
mv Django-1.1.1.tar.gz Django-1.1.1-final.tar.gz
mv Django-1.1.1 Django-1.1.1

wget http://www.djangoproject.com/download/1.0.4/tarball/
tar zxvf Django-1.0.4.tar.gz
mv Django-1.0.4.tar.gz Django-1.0.4-final.tar.gz
mv Django-1.0.4 Django-1.0.4-final

if [ `which svn` ]; then
    echo "svn exists ;) checking out Django-trunk..."
    svn co http://code.djangoproject.com/svn/django/trunk Django-trunk
elif [ `which git` ]; then
    echo "no svn, but git exists ;) checking out Django-trunk..."
    git clone git://github.com/django/django.git
    mv django Django-trunk 
else
    echo "neither svn nor git :( cannot checkout Django-trunk..."
fi

if [ `which hg` ]; then
    echo "hg exists ;) checking out django-south..."
    hg clone http://bitbucket.org/andrewgodwin/south/ django-south
elif [ `which git` ]; then
    echo "no hg, but git exists ;) checking out django-south..."
    git clone git://github.com/andrewgodwin/south.git
else
    echo "neither hg nor git exists :( cannot checkout Django-south..."
fi

if [ `which git` ]; then
    echo "git exists ;) checking out django-extensions..."
    git clone git://github.com/django-extensions/django-extensions.git
else
    echo "can't find git :( downloading django-extensions tarball..."
    wget http://github.com/django-extensions/django-extensions/tarball/master
    tar zxvf django-extensions-*.tar.gz
    rm -f django-extensions-*.tar.gz
    mv django-extensions-* django-extensions
fi

if [ `which wget` ]; then
    echo "downloading virtualenv tarball..."
    wget http://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.4.2.tar.gz#md5=7b1a10f0e84dd945c9b006ace1e1bb16
    tar zxvf virtualenv-1.4.2.tar.gz
    rm -f virtualenv-1.4.2.tar.gz
    mv virtualenv-1.4.2 virtualenv
fi

if [ `which hg` ]; then
    echo "hg exists ;) checking out virtualenvwrapper..."
    hg clone http://bitbucket.org/dhellmann/virtualenvwrapper/
else
    echo "can't find hg :( downloading virtualenvwrapper tarball..."
    wget http://www.doughellmann.com/downloads/virtualenvwrapper-1.21.tar.gz
    tar zxvf virtualenvwrapper-1.21.tar.gz
    rm -f virtualenvwrapper-1.21.tar.gz
    mv virtualenvwrapper-1.21 virtualenvwrapper
fi

##
# Any further initialization will be handled by manage.py
python manage.py bootstrap

##
# Restore current working directory.
#
# Added by Mark Friedenbach 29 Jul 2009
# the "2> /dev/null" to prevent output of an error when no directory is
# specified.
popd > /dev/null 2> /dev/null

##
# End of File
##
