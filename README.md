# PEP Pages Parser

The PEP Pages Parser is a Python library for parsing and extracting information from Python Enhancement Proposal (PEP) pages. It provides a convenient way to access various details about PEPs programmatically.

## Features

- Gather brief summary for a "What's new in Python" page, including link to an article, its name and author(authors).
- Retrieve the latest Python's versions metadata such as link, version and status.
- Download the latest Python's versions documentation.
- Calculate the Python PEP's status statistics (how many PEPs do we have in each status).

## Installation

You can install the PEP Pages Parser library using pip:

```shell
git clone git@github.com:kubanez-create/bs4_parser_pep.git
pip install -r requirements.txt
```

## Usage

Here's a simple example demonstrating how to use the PEP Pages Parser library:

```shell
# Get help
python main.py -h
python main.py --help

# Clear cache
python main.py -c
python main.py --clear-cache

# To redirect program's output to a file use flag
python main.py -o file
python main.py --output file

# To prettify program's output use flag
python main.py -o pretty
python main.py --output pretty

# Get links for the latest Python news pages
python main.py whats-new

# Get a list of Python's versions
python main.py latest-versions

# Download documentation for the latest Python version
python main.py download
```

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on the [GitHub repository](https://github.com/kubanez-create/bs4_parser_pep). If you would like to contribute code, feel free to submit a pull request.

## Contact

If you have any questions or need further assistance, you can reach out to the project maintainer at [kubanez74@google.com](mailto:kubanez74@google.com).
