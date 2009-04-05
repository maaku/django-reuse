::
: django-reuse: README.txt
::

Reusable applications are the primary strength of Django.  With careful
design, a reusable app can be made such that it need only be added to a
project's INSTALLED_APPS setting and instantly add functionality to a site
without any need for manual configuration.  However the key words here are
*careful design*.  The vision of reusable applications that are easy to drop
into a project and painless to use is only realizable only if certain design
constraints and conventions are decided upon and rigorously adhered to.

However, Django by default is not very amenable to reusability.  This has been
summarized fairly well by Brantley Harris (AKA, deadwisdom):

“The default django project layout leaves much to be desired.  It mixes
 applications in folders with project settings, assumes a global django folder
 (in site-packages for instance), assumes you will be serving static media
 though apache or something, cares nothing of per-environment settings, and
 requires tricks to create truly modular apps.”
<http://evernote.com/pub/deadwisdom/blog#144a765d-68b4-48b8-92f5-b834d94ba6a0>

This project, django-reuse, provides a suite of scripts and utility functions
that make it easy to build and maintain reusable Django applications.  It also
provides utilities for managing a development environment that makes it easy
manage applications and keep them up to date.  In short, it provides those
“tricks” required to build reusable, modular Django apps.

::
: End of File
::
