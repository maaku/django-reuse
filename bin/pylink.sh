#!/bin/sh

##
# django-reuse: bin/pylink.sh
#
# Link a Python module to your site packages directory.
#
# Based on code from http://gist.github.com/21649.
##

# Check that an argument has been given. If not, print usage string.
if [ -z $1 ]
then
    echo "Usage: `basename $0` <path_to_module> [<link_name>]"
    exit
fi

# If there is not already a SITE_PACKAGES environment variable, then get it
# from Python.
if [[ -z $SITE_PACKAGES || ! -d $SITE_PACKAGES ]]
then
    SITE_PACKAGES=`python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()"`
fi

# Parse the first argument
BASE=`basename $1`
DIR=`dirname $1`

# Go into the directory of the first argument
pushd $DIR > /dev/null

if [ $2 ]; then
    # If an additional name for the module has been provided, use that as the
    # link's basename.
    ln -sfnv `pwd`/$BASE $SITE_PACKAGES/`basename $2`
else
    # Otherwise, use the basename of the given location.
    ln -sfnv `pwd`/$BASE $SITE_PACKAGES/$BASE
fi

# Return to where we were before
popd > /dev/null

##
# End of File
##
