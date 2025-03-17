from setuptools import setup, find_packages

setup(
    name="graphqlfb",
    version="1.0.0",
    author="Jepluk",
    description="Library untuk scraping dan interaksi dengan Facebook",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jepluk/graphqlfb",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

