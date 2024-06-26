from setuptools import setup, find_packages

setup(
    name='debug',
    version='0.1',
    packages=find_packages(),
    description='Prints to log history to file for debugging',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Hien Quoc',
    author_email='',
    url='http://yoururl.com',
    install_requires=[
        # List your project's dependencies here
        # e.g., 'requests>=2.23.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
