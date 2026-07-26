import re

from setuptools import setup

with open("README.md") as f:
    readme = f.read()

version = ""
with open("opentube/__init__.py") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)  # type: ignore


setup(
    name="opentube",
    version=version,
    description="Access YouTube Public Data without YouTubeAPI",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/jnsougata/opentube",
    author="Sougata Jana",
    author_email="jnsougata@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    packages=["opentube"],
    keywords="youtube, youtube-data, youtube-api, youtube-data-api-v3",
    python_requires=">=3.8.0",
    install_requires=["urllib3"],
    project_urls={
        "Documentation": "https://opentube.readthedocs.io/en/latest/",
        "Source": "https://github.com/jnsougata/opentube",
    },
)
