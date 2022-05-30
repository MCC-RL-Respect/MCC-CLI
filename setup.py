from setuptools import setup, find_packages

# with open('README.md') as f:
#     long_description = f.read()
long_description = "mcccli"

setup(
    name='mcccli',
    version="0.0.1",
    description='Client for MCC Platform',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Minrui Wang',
    url='',
    author_email='wangminrui0804@gmail.com',
    license='MIT',
    install_requires=["requests",
                      "pyyaml",
                      "prompt_toolkit==1.0.9",
                      "prettytable",
                      "termcolor",
                      "colorama",
                      "click",
                      "pyzmq",
                      ],
    packages=find_packages(),
    entry_points={
        'console_scripts': 'mcccli = mcccli.main:main'
    },
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License"
    ]
)
