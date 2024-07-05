<br>
<a href="https://ultralytics.com" target="_blank"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

# Sample Pip Project 📦

Welcome to the Sample Pip Project! This repository serves as a practical reference for the [Python Packaging User Guide][packaging guide]'s [Tutorial on Packaging and Distributing Projects][distribution tutorial]. Our goals are to provide clear examples and to help you master the art of packaging and distributing Python projects.

[![Ultralytics Actions](https://github.com/ultralytics/pip/actions/workflows/format.yml/badge.svg)](https://github.com/ultralytics/pip/actions/workflows/format.yml) <a href="https://ultralytics.com/discord"><img alt="Discord" src="https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue"></a>

Please note that this project is not a comprehensive guide to all best practices in software development. Areas such as version control, comprehensive documentation, or extensive testing strategies are beyond the scope of this tutorial.

The source code for this project is available [here][src], and your contributions and feedback are welcome.

The main configurations for setting up a Python project are contained within the `setup.py` file. We have included a sample `setup.py` in this project for your reference. Be sure to tailor it to the specific needs of your project.

## Prerequisites

Before diving into the packaging process, you'll need:

- Python 3.8 or later installed on your machine.
- All the necessary dependencies listed in [requirements.txt](https://github.com/ultralytics/pip/blob/main/requirements.txt), which include packages like `build` and `twine`.

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

## 🤝 Contribute

We welcome contributions from the community! Whether you're fixing bugs, adding new features, or improving documentation, your input is invaluable. Take a look at our [Contributing Guide](https://docs.ultralytics.com/help/contributing) to get started. Also, we'd love to hear about your experience with Ultralytics products. Please consider filling out our [Survey](https://ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey). A huge 🙏 and thank you to all of our contributors!

<!-- Ultralytics contributors -->

<a href="https://github.com/ultralytics/yolov5/graphs/contributors">
<img width="100%" src="https://github.com/ultralytics/assets/raw/main/im/image-contributors.png" alt="Ultralytics open-source contributors"></a>

## ©️ License

Ultralytics is excited to offer two different licensing options to meet your needs:

- **AGPL-3.0 License**: Perfect for students and hobbyists, this [OSI-approved](https://opensource.org/licenses/) open-source license encourages collaborative learning and knowledge sharing. Please refer to the [LICENSE](https://github.com/ultralytics/ultralytics/blob/main/LICENSE) file for detailed terms.
- **Enterprise License**: Ideal for commercial use, this license allows for the integration of Ultralytics software and AI models into commercial products without the open-source requirements of AGPL-3.0. For use cases that involve commercial applications, please contact us via [Ultralytics Licensing](https://ultralytics.com/license).

## 📬 Contact Us

For bug reports, feature requests, and contributions, head to [GitHub Issues](https://github.com/ultralytics/pip/issues). For questions and discussions about this project and other Ultralytics endeavors, join us on [Discord](https://ultralytics.com/discord)!

<br>
<div align="center">
  <a href="https://github.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="3%" alt="Ultralytics GitHub"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.linkedin.com/company/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="3%" alt="Ultralytics LinkedIn"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://twitter.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png" width="3%" alt="Ultralytics Twitter"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://youtube.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="3%" alt="Ultralytics YouTube"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.tiktok.com/@ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="3%" alt="Ultralytics TikTok"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://ultralytics.com/bilibili"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-bilibili.png" width="3%" alt="Ultralytics BiliBili"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://ultralytics.com/discord"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="3%" alt="Ultralytics Discord"></a>
</div>

[distribution tutorial]: https://packaging.python.org/tutorials/packaging-projects/
[packaging guide]: https://packaging.python.org
[src]: https://github.com/pypa/sampleproject
