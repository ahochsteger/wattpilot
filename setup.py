
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='wattpilot',
    version='0.0.1',
    description='Python library to connect to a Fronius Wattpilot Wallbox',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/joscha82/wattpilot',
    author='Joscha Arenz',
    author_email='joscha@arenz.co',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10",
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='wattpilot',  
    package_dir={'': 'src'}, 
    packages=find_packages(where='src'),
    python_requires='>=3.9, <4',
    install_requires=['websocket-client'],
    platforms="any",
    license="MIT License",
    project_urls={
        'Bug Reports': 'https://github.com/joscha82/wattpilot/issues',
        'Source': 'https://github.com/joscha82/wattpilot'
    }
)
