#!/bin/sh

##
# django-reuse: bin/pyunlink.sh
#
# Remove a pylinked module from your site packages directory.
#
# Based on code from http://gist.github.com/21649.
##

# Check that an argument has been given. If not, print usage string.
if [ -z $1 ]
then
    echo "Usage: `basename $0` <link_name>"
    exit
fi

# If there is not already a SITE_PACKAGES environment variable, then get it
# from Python.
if [[ -z $SITE_PACKAGES || ! -d $SITE_PACKAGES ]]
then
    SITE_PACKAGES=`python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()"`
fi

# If given name is a symbolic link in $SITE_PACKAGES
if [ -h $SITE_PACKAGES/`basename $1` ]; then
    # Remove it
    rm -Rf $SITE_PACKAGES/`basename $1`
else
    # Signal an error.
    echo "Error: link `basename $1` not found."
    exit 1
fi

##
# End of File
##
