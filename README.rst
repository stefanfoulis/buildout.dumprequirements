=========================
buildout.dumprequirements
=========================

A simple buildout extension that dumps a requirements.txt file for pip.


This is more or less a copy of buildout.dumppickedversions. All credit goes to the authors of that project.

.. warning:: ``buildout.dumppickedversions`` (and therefore also ``buildout.dumprequirements``) does some *nasty*
             stuff to get its job done. Namely it monkeypatches ``zc.buildout.easy_install._log_requirement``,
             ``zc.buildout.easy_install.Installer._get_dist`` and ``logging.shutdown``. Because both extensions
             monkeypatch the same methods, it is currently not possible to use ``buildout.dumppickedversions`` and
             ``buildout.dumprequirements`` at the same time.
             I'm not quite sure how to solve this. Probably we'll have to support the functionality of both extensions
             in one package.

Usage
=====

Add ``buildout.dumprequirements`` as an extension to the ``[buildout]`` section::

    [buildout]
    extensions = buildout.dumprequirements
    dump-requirements-file = requirements.txt
    overwrite-requirements-file = true

``dump-requirements-file`` defines the file the requirement list will be written to. If it is undefined the
package list will be printed to the console. Setting ``overwrite-requirements-file`` to ``false`` will prevent
``buildout.dumprequirements`` from overwriting an existing file. The setting defaults to ``true``.
