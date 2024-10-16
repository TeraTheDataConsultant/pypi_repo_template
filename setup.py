from setuptools import setup, find_packages
import os

# Utility function to read the requirements.txt file


def read_requirements():
    requirements_path = "requirements.txt"
    if os.path.isfile(requirements_path):
        with open(requirements_path) as req:
            return req.read().splitlines()
    return []


setup(
    name="pypi-repo-template",
    version="0.0.1",
    description="PYPI Repository Template",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/TeraTheDataConsultant/pypi_repo_template",
    author="Tera Earlywine",
    author_email="tera.earlywine@qbizinc.com",
    packages=find_packages(where="core"),
    package_dir={"": "src"},
    install_requires=read_requirements(),
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            # command=folder.script_name.main       # example
            "template=cli.main:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
