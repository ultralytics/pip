# Sample Python Packaging Project 📦

Welcome to the Sample Python Packaging Project! This repository provides you with a basic structure and guidance for packaging and distributing Python projects. Although this sample does not delve into every aspect of Python project development, it focuses on the packaging aspect, which is crucial for sharing and distributing code to the Python community.

![Python Logo](https://www.python.org/static/community_logos/python-logo.png "Sample inline image")

For comprehensive guidance on Python packaging, refer to the [Python Packaging User Guide][packaging guide] and this [Tutorial on Packaging and Distributing Projects][distribution tutorial].

Please note that the source code is available [here][src], and the configuration for this Python project is primarily done in the `setup.py` file, which you can tailor to your project's requirements.

[packaging guide]: https://packaging.python.org
[distribution tutorial]: https://packaging.python.org/tutorials/packaging-projects/
[src]: https://github.com/pypa/sampleproject

Keep in mind:
- We assume familiarity with the very basics of Python packaging; this is not a starting guide but a sample project to illustrate the process.
- The examples provided here are intended to help with the packaging process and are not exhaustive. Other aspects of project development, like version control and testing, are not covered.

## Prerequisites 📋

Before you begin, ensure you have Python 3.8 or later. You'll need to install dependencies listed in the [requirements.txt](https://github.com/ultralytics/pip/blob/master/requirements.txt), including `build` and `twine` tools for packaging and uploading our package.

To install these dependencies, run the following commands:

```bash
# Upgrade pip to its latest version
python -m pip install -U pip

# Install the requirements
pip install -r requirements.txt
```

## Packaging and Publishing Steps 📝

### Publish to https://pypi.org/

1. **Build the Package**: Generate distribution archives for the package.

```bash
# Remove previous builds and create fresh distributions
rm -rf build dist
python -m build
```

2. **Upload to PyPI**: Use `twine` to upload the package to PyPI.

```bash
# Upload the distributions to PyPI
python -m twine upload dist/*
# You will be prompted for a username and password
# Username: __token__
# Password: pypi-AgENdGVzdC5weXBpLm9yZ...
```

3. **Install and Test**: Ensure that the package is installable from PyPI and that it works as expected.

```bash
# Download and install the package from PyPI
pip install -U ultralytics

# Test the installed package
python -c "from ultralytics import simple; print(simple.add_one(10))"
# Should output `11`
```

### Test with https://test.pypi.org/

1. **Build and Upload**: Similar to the steps above, but for the Test PyPI to safely test your uploading process.

```bash
# Follow the same steps as above to build the package
rm -rf build dist
python -m build

# Upload to Test PyPI instead
python -m twine upload --repository testpypi dist/*
# Again, you'll need your Test PyPI token credentials
# Username: __token__
# Password: pypi-AgENdGVzdC5weXBpLm9yZ...
```

2. **Download and Install**: Test the installation from Test PyPI.

```bash
# Install the package specifically from Test PyPI
pip install -U --index-url https://test.pypi.org/simple/ --no-deps ultralytics2==0.0.9

# Run a simple test to verify the installation
python -c "from ultralytics import simple; print(simple.add_one(10))"
# The output should be `11`
```

Through these steps, you'll be able to package and share your Python projects with the wider community, making your code accessible and usable by others. Happy coding! 🚀
