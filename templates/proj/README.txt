::
: $PROJECT_NAME$
::

$PROJECT_NAME$
$PROJECT_NAME_DOUBLE_DASH$

DESCRIPTION
-----------

A sample Django project configuration, designed to enable the easy integration
of reusable applications and per-project django installations.

INSTALL
-------

To start a new Django project, begin by modifying the *.txt documentation
files in the project's root directory to fit your needs.  Then, in the root
directory of the new project add a 'django' symlink to the identically named
'django' subdirectory of whichever version of Django you choose to use for
this project.  And that's it, you're done.

Note that the newly created project is by default created with development
settings.  To enable production settings, create a 'settings_local.py' file in
the 'project' directory with the following two lines:

  DEBUG = False
  MEDIA_SERVE = False

The settings_local.py file will automatically be loaded after settings.py is
evaluated.  It is advised that you keep settings_local.py outside of version
control, and to use different versions of this file in development and
production environments.

USAGE
-----

The sample Django project is configured to add the root directory to the
python path.  Therefore symlinks to python modules in the root directory may
be used directly in python code.  This has the benefit of enabling a simple
per-project versioning system for applications--just make symlinks to the
version which you want to tie this project to.

DO NOT RENAME THE 'project' SUBDIRECTORY.  This name was chosen so that the
'project' namespace could be used to refer to per-project settings and
functionality in reusable code.

DEPLOYMENT
----------

To deploy this project, simply configure a python CGI-enabled web server to
send requests to the 'project' subdirectory.

::
: End of File
::
