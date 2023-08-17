# PEP Pages Parser

The PEP Pages Parser is a Python package for parsing and extracting information from Python Enhancement Proposal (PEP) pages. It provides a convenient way to access various details about PEPs programmatically.

## Features

- Retrieve each PEP's metadata such as number, author(s) and status.
- Calculate the Python PEP's status statistics (how many PEPs do we have in each status).

## Installation

You can install the PEP Pages Parser using pip:

```shell
git clone git@github.com:kubanez-create/scrapy_parser_pep.git
cd scrapy_parser_pep
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Here's an example demonstrating how to use the PEP Pages Parser library:

```shell
# Parse contents of Python PEP's page and
# create two files: one for PEP's statistics and another for PEP's metadata
scrapy crawl pep
```

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on the [GitHub repository](https://github.com/kubanez-create/bs4_parser_pep). If you would like to contribute code, feel free to submit a pull request.

## Contact

If you have any questions or need further assistance, you can reach out to the project maintainer at [kubanez74@google.com](mailto:kubanez74@google.com).
