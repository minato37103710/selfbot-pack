import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="selfbot-pack",
    version="0.0.1",
    author="orarange",
    author_email="arigatoudane@outlook.jp",
    description="This package is for creating a discord self bot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/minato37103710/selfbot-pack",
    project_urls={
        "Bug Tracker": "https://github.com/minato37103710/selfbot-pack/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)