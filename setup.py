"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

import pathlib

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()  # current path
long_description = (here / 'README.md').read_text(encoding='utf-8')  # Get the long description from the README file
with open(here / 'requirements.txt') as fp:  # read requirements.txt
    install_reqs = [r.rstrip() for r in fp.readlines() if not r.startswith('#')]

setup(
    name='ultralytics',  # Required https://packaging.python.org/specifications/core-metadata/#name
    version='0.0.1',  # Required https://packaging.python.org/en/latest/single_source_version.html
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

    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=install_reqs,  # Optional, additional pip packeges to be installed by this pacakge installation

    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example: $ pip install sampleproject[dev]
    # Similar to `install_requires` above, these must be valid existing projects
    extras_require={'dev': ['check-manifest'],
                    'test': ['coverage'],
                    },  # Optional

    package_data={'ultralytics': ['package_data.dat'],
                  },  # Optional, Data files included in your packages that need to be installed

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
    entry_points={'console_scripts': ['sample_script=ultralytics:main', ],
                  },  # Optional

    project_urls={'Bug Reports': 'https://github.com/ultralytics/yolov5/issues',
                  'Funding': 'https://www.ultralytics.com',
                  'Source': 'https://github.com/ultralytics/yolov5/',
                  },  # Optional https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
)
