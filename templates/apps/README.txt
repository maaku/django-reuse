::
: $PROJECT_NAME$
::

$PROJECT_NAME$
$PROJECT_NAME_DOUBLE_DASH$

DESCRIPTION
-----------

A sample Django reusable application, designed to enable easy integration with
other reusable applications and to provide a consistent interface and set of
conventions for doing so.

INSTALL
-------

To start a new reusable Django application, begin by modifying the *.txt
distribution files in the application's root directory to fit your needs.
Then create a symbolic link somewhere in the python path (typically in a
subdirectory of your project that has been added to that project's python
path) to the python module that has been created in this directory.  Add the
name of that module to your project's INSTALLED_APPS setting, and you're done.

USAGE
-----

There is no guarantee that a project will keep your choice of an application
name when deployed.  Do not rely on that choice.  For example, if you choose
"foo" as the name of your application, and "bar" is a module within your
application, do not try to "import foo.bar".  This will keep your app usable
even when and if another developer chooses the same name as you for their
reusable application.

DEPLOYMENT
----------

To deploy this application, simply create a symbolic link within the python
path of your project to this application's python module.

::
: End of File
::
