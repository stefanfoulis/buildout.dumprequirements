# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = "0.1.1"

long_description = (read('README.rst')+read('CONTRIBUTORS.rst'))
entry_point = 'buildout.dumprequirements:install'
entry_points = {"zc.buildout.extension": ["default = %s" % entry_point]}

tests_require=['zc.buildout', 'zope.testing', 'zc.recipe.egg']

setup(name='buildout.dumprequirements',
      version=version,
      description="Dump buildout picked versions as a pip compatible requirements.txt file.",
      long_description=long_description,
      classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
      license='GPL',
      keywords='buildout extension dump picked versions requirements.txt',
      author='Stefan Foulis',
      author_email='stefan.foulis@gmail.com',
      url='https://github.com/stefanfoulis/buildout.dumprequirements',
      packages = find_packages(),
      namespace_packages=['buildout'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'zc.buildout'
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite = 'buildout.dumppickedversions.tests.test_suite',
      entry_points=entry_points,
      )
