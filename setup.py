###
### gobbler_diarize setup.py
### 
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("VERSION", "r") as version_file:
    version = version_file.read().strip()

setup(
    name='gobbler_diarize',
    version=version,
    packages=find_packages(),
    author='David Hooton',
    author_email='gobbler_diarize+david@hooton.org',
    description='Diarize a 16 bit PCM mono WAV file using WhisperX',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/djh00t/gobbler_diarize',
    include_package_data=True,
    install_requires=[
        'datetime',
        'netifaces',
        'pytest',
        'uuid',
        'setuptools'
    ],
    entry_points={
        'console_scripts': [
            'gobbler_diarize=diarize:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)