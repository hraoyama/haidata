.. haidata documentation master file, created by
   sphinx-quickstart on Sun Dec  9 18:28:52 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


   
Welcome to *haidata* Documentation!
===================================

Introduction
------------

:mod:`haidata` is a python based data cleaning and processing tool for :mod:`pandas` DataFrames. :mod:`haidata` wraps processing of pandas DataFrames in reusable JSON using :mod:`jsonpickle`, such that processing can be altered and serialized at runtime through the :class:`HaiDataCfg` class.

Requirements
------------

.. _jsonpickle: https://jsonpickle.github.io/
.. _ftfy: https://pypi.org/project/ftfy/

* Python 3.6+
* `jsonpickle`_ package 
* `ftfy`_ package

Quick Start 
-----------

The easiest way to understand what :mod:`haidata` can do for you is to follow an :doc:`easy example </tutorial>`.

Code Reference
--------------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

For a comprehensive view of the code, click :doc:`here </reference>`.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
