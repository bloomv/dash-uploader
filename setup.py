import json
from setuptools import setup

with open("package.json") as f:
    package = json.load(f)

with open("docs/README-PyPi.md", encoding="utf-8") as f:
    long_description = f.read()

package_name = package["name"].replace(" ", "_").replace("-", "_")

setup(
    name=package_name,
    version=package["version"],
    author=package["author"],
    author_email="niko@pasanen.me",
    url=package["homepage"],
    packages=[
        package_name,
        package_name + "._build",
    ],
    include_package_data=True,
    license=package["license"],
    description=package.get("description", package_name),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["dash>=1.1.0", "packaging>= 21.0"],
    extras_require={
        "dev": [
            "pyyaml~=5.3.1",  # building with dash-generate-components
            # Packages needed to run the tests.
            "black",  # code formatting
            "pytest",  # running tests
            "selenium",  # running tests
            # Switch into a virtual environment
            # pip install -r requirements.txt
            "dash[testing]>=1.1.0",
            # Automatically get the latest ChromeDriver. If Chrome updated, use
            # pip install --upgrade --force-reinstall chromedriver-binary-auto
            # to update the chromedriver binary.
            # Needs: import chromedriver_binary to the top of your test script.
            "chromedriver-binary-auto",
        ]
    },
    classifiers=[
        "Framework :: Dash",
    ],
)
