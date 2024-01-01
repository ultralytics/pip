# Ultralytics pip template

from pathlib import Path

from setuptools import find_packages, setup

setup(
    name="ultralytics-hub-sdk",
    version="0.0.0",
    description="A placeholder for future Ultralytics projects.",
    long_description=Path("README_simple.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    author="Ultralytics",
    author_email="hello@ultralytics.com",
    url="https://github.com/ultralytics/pip",
    project_urls={
        "Bug Reports": "https://github.com/ultralytics/pip/issues",
        "Funding": "https://ultralytics.com",
        "Source": "https://github.com/ultralytics/pip",
    },
    license="AGPL-3.0",
    packages=find_packages(),
    install_requires=[
        "ultralytics>8.0.170",
    ],
    entry_points={"mkdocs.plugins": ["ultralytics = plugin:MetaPlugin"]},
)
