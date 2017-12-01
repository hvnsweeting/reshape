=======
reshape
=======


.. image:: https://img.shields.io/pypi/v/reshape.svg
        :target: https://pypi.python.org/pypi/reshape

.. image:: https://img.shields.io/travis/hvnsweeting/reshape.svg
        :target: https://travis-ci.org/hvnsweeting/reshape

.. image:: https://readthedocs.org/projects/reshape/badge/?version=latest
        :target: https://reshape.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/hvnsweeting/reshape/shield.svg
     :target: https://pyup.io/repos/github/hvnsweeting/reshape/
     :alt: Updates


The missing Numpy's reshape for Python.



* Free software: MIT license
* Documentation: https://reshape.readthedocs.io.


Features
--------


::


  >>> import reshape
  >>> for row in reshape.reshape(range(20), 3):
  ...     print(row)
  ...
  (0, 7, 14)
  (1, 8, 15)
  (2, 9, 16)
  (3, 10, 17)
  (4, 11, 18)
  (5, 12, 19)
  (6, 13, None)
  >>>
  >>> for row in reshape.reshape("HVNfromPymiVN"):
  ...     print(row)
  ...
  ('H', 'o', 'i')
  ('V', 'm', 'V')
  ('N', 'P', 'N')
  ('f', 'y', None)
  ('r', 'm', None)

TODO
----

- Support py2
- Use mypy

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

