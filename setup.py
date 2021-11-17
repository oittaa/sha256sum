import os
from setuptools import setup, find_packages  # type: ignore

NAME = "sha256sum"

DESCRIPTION = "Compute SHA256 message digest from a file"
URL = "https://github.com/oittaa/sha256sum"
LONG_DESCRIPTION = open(os.path.join(os.path.dirname(__file__), "README.md")).read()

AUTHOR = "Oittaa"
AUTHOR_EMAIL = ""
GITHUB_REF = os.environ.get("GITHUB_REF")
PREFIX = "refs/tags/"

if GITHUB_REF and GITHUB_REF.startswith(PREFIX):
    prefix_len = len(PREFIX)
    VERSION = GITHUB_REF[prefix_len:]
else:
    VERSION = "0.0.0.dev0"

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    include_package_data=True,
    zip_safe=False,
    keywords=[
        "sha256sum",
        "SHA256",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    setup_requires=[
        "wheel",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
)
