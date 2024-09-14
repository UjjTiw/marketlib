# Always prefer setuptools over distutils

from setuptools import setup, find_packages
import pathlib
here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
#long_description = (here / 'README.md').read_text(encoding='utf-8')

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='electricity_markets',  # Required
    version='0.1.0',  # Required
    description='Project to model the trading of energy to different markets using various power plant models',  # Optional
    # long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/UjjTiw/marketlib',  # Optional #Change later
    author='UjjTiw',  # Optional
    include_package_data=True,
    package_data={
        
        # Include any *.msg files found in the "hello" package, too:
        "electricity_markets": ["raw/*.csv","raw/*.json","raw/*.xlsx"],
    },
       keywords='Electricity, Markets, Energy',  # Optional
    packages=find_packages(
        where="src",
    ),
    package_dir={"": "src"},
    python_requires='>=3.6, <4',
    install_requires=[
        "matplotlib",
        "oemof.solph",
        "openpyxl",
        "xlsxwriter", ],

    project_urls={  # Optional
        'Bug Reports': 'https://github.com/UjjTiw/marketlib',
        #'Funding': 'ZLE Funders',
        'Documentation': "https://github.com/UjjTiw/marketlib",
        'Source': "https://github.com/UjjTiw/marketlib",
    },
)


if __name__ == '__main__':
    pass
