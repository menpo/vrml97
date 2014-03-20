#!/usr/bin/env python
"""Installs vrml scenegraph modelling engine using setuptools (eggs)
"""
from setuptools import setup, find_packages
import sys, os
sys.path.insert(0, '.' )

def find_version( ):
    for line in open( os.path.join(
        'vrml','__init__.py',
    )):
        if line.strip().startswith( '__version__' ):
            return eval(line.strip().split('=')[1].strip())
    raise RuntimeError( """No __version__ = 'string' in __init__.py""" )
version = find_version()

if __name__ == "__main__":
    extraArguments = {
        'classifiers': [
            """License :: OSI Approved :: BSD License""",
            """Programming Language :: Python""",
            """Programming Language :: C""",
            """Topic :: Software Development :: Libraries :: Python Modules""",
            """Topic :: Multimedia :: Graphics :: 3D Rendering""",
            """Intended Audience :: Developers""",
        ],
        #'download_url': "https://sourceforge.net/projects/pyvrml97/files/PyVRML97/",
        'keywords': 'VRML,VRML97,scenegraph',
        'long_description' : """VRML97 Scenegraph modelling objects for Python 

This project provides a core semantic model for VRML97 objects which
is close to (but not identical to) that specified in the VRML97 spec.
It is primarily used for the OpenGLContext project's VRML97 rendering
engine, but can also be used for generating, parsing or processing VRML97 
scenegraphs.

We have forked this to provide a correct setup.py. No other changes have been made.

Originally from http://pyopengl.sourceforge.net/context/
""",
        'platforms': ['Win32','Linux','OS-X','Posix'],
    }
    ### Now the actual set up call

    setup (
        name = "menpo-PyVRML97",
        version = version,
        description = "VRML97 Scenegraph model for Python",
        author = "Mike C. Fletcher",
        author_email = "mcfletch@vrplumber.com",
        options = {
            'sdist': {
                'formats':['gztar','zip'],
            },
        },
        url = "https://github.com/menpo/vrml97",
        license = "BSD",
        packages = find_packages(),
        install_requires=['numpy>=1.7', 'PyDispatcher>=2.0.3', 'SimpleParse>=2.1.1'],
        zip_safe = False,
        **extraArguments
    )
