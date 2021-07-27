from setuptools import find_packages, setup


VERSION = "0.1.0"

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pulsecli",
    version=VERSION,
    description="Browse stock news from pulse.zerodha.com on terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Abijith Bahuleyan",
    author_email="abijithbahuleyan@gmail.com",
    url="https://github.com/twentyse7en/pulsecli",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux",
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "click",
        "requests",
        "beautifulsoup4",
        "lxml",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "pulsecli=pulsecli.pulse_cli:cli"
        ]
    }
)
