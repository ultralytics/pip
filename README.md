## Sample Pip Project

![Python Logo](https://www.python.org/static/community_logos/python-logo.png "Sample inline image")

A sample project that exists as an aid to the [Python Packaging User Guide][packaging guide]'
s [Tutorial on Packaging and Distributing Projects][distribution tutorial].

This project does not aim to cover best practices for Python project development as a whole. For example, it does not
provide guidance or tool recommendations for version control, documentation, or testing.

[The source for this project is available here][src].

Most of the configuration for a Python project is done in the `setup.py` file, an example of which is included in this
project. You should edit this file accordingly to adapt this sample project to your needs.

[packaging guide]: https://packaging.python.org

[distribution tutorial]: https://packaging.python.org/tutorials/packaging-projects/

[src]: https://github.com/pypa/sampleproject

[rst]: http://docutils.sourceforge.net/rst.html

[md]: https://tools.ietf.org/html/rfc7764#section-3.5 "CommonMark variant"

[md use]: https://packaging.python.org/specifications/core-metadata/#description-content-type-optional

## Requirements

Python 3.8 or later with all [requirements.txt](https://github.com/ultralytics/pip/blob/master/requirements.txt)
dependencies installed, including `build` and `twine`. To install run:

```bash
python -m pip install -U pip
pip install -r requirements.txt
```

## Pip Package Steps

### https://pypi.org/

```bash
# Build and upload https://pypi.org/
rm -rf build dist && python -m build && python -m twine upload dist/*
# username: __token__
# password: pypi-AgENdGVzdC5weXBpLm9yZ...

# Download and install
pip install -U ultralytics

# Import and test
python -c "from ultralytics import simple; print(simple.add_one(10))"
sample_script
```

### https://test.pypi.org/

```bash
# Build and upload https://test.pypi.org/
rm -rf build dist && python -m build && python -m twine upload --repository testpypi dist/*
# username: __token__
# password: pypi-AgENdGVzdC5weXBpLm9yZ...

# Download and install
pip install -U --index-url https://test.pypi.org/simple/ --no-deps ultralytics2==0.0.9

# Import and test
python -c "from ultralytics import simple; print(simple.add_one(10))"
sample_script
```
