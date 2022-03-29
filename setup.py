# -*- coding: utf-8 -*-

from setuptools import setup

setup(

    # Vitals
    name='usb_protocol',
    license='BSD',
    url='https://github.com/usb-tool/luna',
    author='Katherine J. Temkin',
    author_email='ktemkin@greatscottgadgets.com',
    description='python library providing utilities, data structures, constants, parsers, and tools for working with USB data',
    use_scm_version= {
        "root": '..',
        "relative_to": __file__,
        "version_scheme": "guess-next-dev",
        "local_scheme": lambda version : version.format_choice("+{node}", "+{node}.dirty"),
        "fallback_version": "0.0"
    },

    # Imports / exports / requirements.
    platforms='any',
    packages=[
        'usb_protocol',
        'usb_protocol.emitters',
        'usb_protocol.types',
    ],
    package_dir={'usb_protocol': 'usb_protocol',
                 'usb_protocol.emitters': 'usb_protocol/emitters',
                 'usb_protocol.types': 'usb_protocol/types',
                 },
    include_package_data=True,
    python_requires="~=3.7",
    install_requires=['construct'],

    # Metadata
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Environment :: Console',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering',
        'Topic :: Security',
        ],
)
