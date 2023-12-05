# Sample Pip Project 📦

![Python Logo](https://www.python.org/static/community_logos/python-logo.png "Sample inline image")

Welcome to the Sample Pip Project! This repository serves as a practical reference for the [Python Packaging User Guide][packaging guide]'s [Tutorial on Packaging and Distributing Projects][distribution tutorial]. Our goals are to provide clear examples and to help you master the art of packaging and distributing Python projects.

Please note that this project is not a comprehensive guide to all best practices in software development. Areas such as version control, comprehensive documentation, or extensive testing strategies are beyond the scope of this tutorial.

The source code for this project is available [here][src], and your contributions and feedback are welcome.

[packaging guide]: https://packaging.python.org

[distribution tutorial]: https://packaging.python.org/tutorials/packaging-projects/

[src]: https://github.com/pypa/sampleproject

The main configurations for setting up a Python project are contained within the `setup.py` file. We have included a sample `setup.py` in this project for your reference. Be sure to tailor it to the specific needs of your project.

## Prerequisites

Before diving into the packaging process, you'll need:

- Python 3.8 or later installed on your machine.
- All the necessary dependencies listed in [requirements.txt](https://github.com/ultralytics/pip/blob/master/requirements.txt), which include packages like `build` and `twine`.

To install these requirements, run the following commands:

```bash
# Upgrade pip to the latest version
python -m pip install -U pip

# Install the required packages
pip install -r requirements.txt
```

## Pip Package Management Steps

Here, we walk you through the process of building and distributing your package to both the official Python Package Index (PyPI) and the Test PyPI site.

### Official PyPI Site: https://pypi.org/

```bash
# Clean previous builds and upload new distribution archives to PyPI
rm -rf build dist
python -m build
python -m twine upload dist/*

# Enter your credentials here:
# username: __token__
# password: pypi-AgENdGVzdC5weXBpLm9yZ...

# Download and install your package using pip
pip install -U ultralytics

# Import your module and test its functionality with a simple example
python -c "from ultralytics import simple; print(simple.add_one(10))"
```

### Test PyPI Site: https://test.pypi.org/

If you want to test the upload and installation process before going live on the official index, you can use the Test PyPI site.

```bash
# Build your package and upload it to Test PyPI
rm -rf build dist
python -m build
python -m twine upload --repository testpypi dist/*

# Authenticate using your Test PyPI credentials
# username: __token__
# password: pypi-AgENdGVzdC5weXBpLm9yZ...

# To install your package from Test PyPI, ensure that you specify the index URL and the package name with its version
pip install -U --index-url https://test.pypi.org/simple/ --no-deps ultralytics2==0.0.9

# Run a quick test to confirm everything works as expected
python -c "from ultralytics import simple; print(simple.add_one(10))"
```

Please note that in a real-world scenario, you'd replace the placeholder package name (`ultralytics` or `ultralytics2`) with the actual name of your package, as well as the placeholder version number (`0.0.9`) with the version you are releasing.

Remember to always upload your package to the Test PyPI first to ensure everything works perfectly before pushing it to the official PyPI site. With this careful approach, you can ensure a smooth release process for your package.
