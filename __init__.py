# paper_fetcher/__init__.py
from .fetch_details import fetch_details
from .filter_papers import filter_papers

__all__ = ["fetch_pubmed_ids", "fetch_details", "filter_papers", "parse_authors", "write_to_csv"]
__version__ = "0.1.0"

"""
Initialize the paper_fetcher package
"""
# Makes this folder a Python package
# This file is used to mark the directory as a Python package and to define the package's metadata.
# It allows for importing modules from this package in other parts of the codebase.


