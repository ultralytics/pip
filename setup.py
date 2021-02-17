"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

import pathlib

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

with open(here / 'requirements.txt') as fp:
    install_reqs = [r.rstrip() for r in fp.readlines() if not r.startswith('#')]

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='ultralytics',  # Required https://packaging.python.org/specifications/core-metadata/#name
    version='0.0.0',  # Required https://packaging.python.org/en/latest/single_source_version.html
    description='YOLOv5 by Ultralytics',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional
    url='https://github.com/ultralytics/pip',  # Optional, project's main homepage
    author='Glenn Jocher',  # Optional, name or the name of the organization which owns the project
    author_email='glenn.jocher@ultralytics.com',  # Optional
    classifiers=['Development Status :: 5 - Production/Stable',  # 3 - Alpha, 4 - Beta, 5 - Production/Stable
                 'Intended Audience :: Developers',  # Indicate who your project is intended for
                 'Operating System :: OS Independent',  # Operation system
                 'Topic :: Education',  # Topics
                 'Topic :: Scientific/Engineering',
                 'Topic :: Scientific/Engineering :: Artificial Intelligence',
                 'Topic :: Scientific/Engineering :: Image Recognition',
                 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',  # Pick your license as you wish
                 'Programming Language :: Python :: 3.7',  # Python version support
                 'Programming Language :: Python :: 3.8',
                 'Programming Language :: Python :: 3.9',
                 ],  # Classifiers help users find your project by categorizing it https://pypi.org/classifiers/
    keywords='machine-learning, deep-learning, ml, pytorch, YOLO, object-detection, YOLOv3, YOLOv4, YOLOv5',  # Optional
    package_dir={'': 'src'},  # Optional, use if source code is in a subdirectory under the project root, i.e. `src/`
    packages=find_packages(where='src'),  # Required
    python_requires='>=3.7, <4',

    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=install_reqs,  # Optional

    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.
    package_data={  # Optional
        'ultralytics': ['package_data.dat'],
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/distutils/setupscript.html#installing-additional-files
    #
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[('my_data', ['data/data_file'])],  # Optional

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `ultralytics` which
    # executes the function `main` from this package when invoked:
    entry_points={'console_scripts': ['sample_script=ultralytics:main',
                                      ],
                  },  # Optional

    # List additional URLs that are relevant to your project as a dict.
    #
    # This field corresponds to the "Project-URL" metadata fields:
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    #
    # Examples listed include a pattern for specifying where the package tracks
    # issues, where the source is hosted, where to say thanks to the package
    # maintainers, and where to support the project financially. The key is
    # what's used to render the link text on PyPI.
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/ultralytics/yolov5/issues',
        'Funding': 'https://www.ultralytics.com',
        'Source': 'https://github.com/ultralytics/yolov5/',
    },
)
