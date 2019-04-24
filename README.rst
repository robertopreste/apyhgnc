=======
apyhgnc
=======


.. image:: https://img.shields.io/pypi/v/apyhgnc.svg
        :target: https://pypi.python.org/pypi/apyhgnc

.. image:: https://www.repostatus.org/badges/latest/wip.svg
    :alt: Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.
    :target: https://www.repostatus.org/#wip

.. image:: https://travis-ci.com/robertopreste/apyhgnc.svg?branch=master
    :target: https://travis-ci.com/robertopreste/apyhgnc

.. image:: https://circleci.com/gh/robertopreste/apyhgnc.svg?style=svg
        :target: https://circleci.com/gh/robertopreste/apyhgnc

.. image:: https://app.codeship.com/projects/c832f1e0-44fe-0137-a826-5a0258e749b3/status?branch=master
        :target: https://app.codeship.com/projects/337097
        :alt: Codeship Status for robertopreste/apyhgnc

.. image:: https://codecov.io/gh/robertopreste/apyhgnc/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/robertopreste/apyhgnc

.. image:: https://readthedocs.org/projects/apyhgnc/badge/?version=latest
        :target: https://apyhgnc.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/robertopreste/apyhgnc/shield.svg
     :target: https://pyup.io/repos/github/robertopreste/apyhgnc/
     :alt: Updates

.. image:: https://pyup.io/repos/github/robertopreste/apyhgnc/python-3-shield.svg
     :target: https://pyup.io/repos/github/robertopreste/apyhgnc/
     :alt: Python 3



.. image:: https://pepy.tech/badge/apyhgnc
    :target: https://pepy.tech/project/apyhgnc
    :alt: Downloads


Async pythonic interface to HGNC.


* Free software: MIT license
* Documentation: https://apyhgnc.readthedocs.io
* GitHub repo: https://github.com/robertopreste/apyhgnc


Features
--------

This Python package allows to retrieve entries from HGNC_ using synchronous or asynchronous calls.

* Return searchable fields and stored fields separately using the ``info()`` function (or the lower-level ``Info`` class).
* Return all entries of interest limiting results only to hgnc_id, symbol and score fields using the ``search()`` function for synchronous calls or the ``asearch()`` function for asynchronous calls (or the lower-level ``Search`` class).
* Return entries according to the given searchable fields, returning all the available stored fields using the ``fetch()`` function for synchronous calls or the ``afetch()`` function for asynchronous calls (or the lower-level ``Fetch`` class).

Please refer to the Usage_ section of the documentation for further information.

Installation
------------

**apyhgnc only supports Python 3**, and can be installed using pip::

    pip install apyhgnc

Please refer to the Installation_ section of the documentation for further information.

Credits
-------

This package was created with Cookiecutter_ and the `cc-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cc-pypackage`: https://github.com/robertopreste/cc-pypackage
.. _HGNC: https://www.genenames.org
.. _Usage: https://apyhgnc.readthedocs.io/en/latest/usage.html
.. _Installation: https://apyhgnc.readthedocs.io/en/latest/installation.html
