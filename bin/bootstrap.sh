#!/bin/sh

##
# django-reuse: bin/bootstrap.sh
#
# Setup a django development environment using the django-reuse tools.
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
}

if [ $# -gt 1 ]; then
    echo "`basename $0`: error, too many parameters."
    parse_error
fi

if [ $# -eq 1 ]; then
    if [ ! -d $1 ]; then
        echo "`basename $0`: error, \"$1\" does not exist or is not a directory."
        parse_error
    fi

    ##
    # Switch to the directory specified.  All commands issued from here on out
    # will be relative to this working directory.
    cd $1
fi

##
# Some sanity checks... the directory django-reuse should not exist, nor
# should the file django-reuse.py.
if [ -e "django-reuse" ]; then
    echo "`basename $0`: error, file/directory django-reuse already exists."
    exit
fi
if [ -e "django-reuse.py" ]; then
    echo "`basename $0`: error, file/directory django-reuse.py already exists."
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
# symbolic link to the script django-reuse/bin/reuse.py
ln -s django-reuse/bin/reuse.py django-reuse.py

##
# Any further initialization will be handled by django-reuse.py
python django-reuse.py init

##
# End of File
##
