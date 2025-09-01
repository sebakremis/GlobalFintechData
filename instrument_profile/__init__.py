"""
instrument_profile
==================

This module provides tools to fetch, normalize, and validate descriptive
metadata for a given financial instrument.

Unlike most market data tools that focus on prices and trading activity,
`instrument_profile` is designed to aggregate static, descriptive attributes
from multiple trusted sources — such as regulatory filings, exchange metadata,
and public financial databases.

Core functionality:
- Retrieve instrument metadata by identifier (e.g., ISIN, ticker, CUSIP)
- Normalize fields to a consistent schema aligned with ISO and market standards
- Validate completeness and format of key attributes
- Return results as Python dictionaries or pandas DataFrames

Example:
    >>> from globalfintechdata.instrument_profile import get_instrument_profile
    >>> profile = get_instrument_profile("US0378331005")  # Apple ISIN
    >>> print(profile["issuer_name"])
    Apple Inc.

Notes:
    - This module focuses on static data; historical prices are available
      via optional connectors.
    - All data sources should be vetted for reliability and licensing terms.
"""

from typing import Dict, Any, Optional

def fetch_instrument_data(identifier: str) -> Dict[str, Any]:
    """
    Fetch raw descriptive data for a given financial instrument.

    Args:
        identifier (str): An instrument identifier (e.g., ISIN, ticker, CUSIP).

    Returns:
        dict: Raw data as returned by the source(s).
    """
    # TODO: Implement data retrieval from trusted sources
    # Example: call an API, scrape a regulatory database, or read from a CSV
    return {}


def normalize_instrument_data(raw_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Normalize raw instrument data to a consistent schema.

    Args:
        raw_data (dict): Raw instrument data from fetch_instrument_data().

    Returns:
        dict: Normalized data with standardized field names and formats.
    """
    # TODO: Map source-specific fields to standard schema
    # Example: convert date strings to datetime objects, standardize codes
    return raw_data

from .schema import INSTRUMENT_SCHEMA

def validate_instrument_data(data):
    """
    Validate that the normalized instrument data meets schema requirements.

    Args:
        data (dict): Normalized instrument data.

    Returns:
        tuple:
            - bool: True if data passes validation, False otherwise.
            - list: A list of error messages (empty if validation passes).
    """
    errors = []

    for field, rules in INSTRUMENT_SCHEMA.items():
        # Check required fields
        if rules["required"] and field not in data:
            errors.append(f"Missing required field: '{field}'")
            continue  # No need to check type if field is missing

        # If field is present and not None, check type
        if field in data and data[field] is not None:
            expected_type = rules["type"]
            if not isinstance(data[field], expected_type):
                errors.append(
                    f"Field '{field}' has wrong type: expected {expected_type.__name__}, "
                    f"got {type(data[field]).__name__}"
                )

    return (len(errors) == 0, errors)




def get_instrument_profile(identifier: str, source: Optional[str] = None) -> Dict[str, Any]:
    """
    High-level function to retrieve, normalize, and validate an instrument profile.

    Args:
        identifier (str): An instrument identifier (e.g., ISIN, ticker, CUSIP).
        source (str, optional): Specific data source to use (if applicable).

    Returns:
        dict: Final validated instrument profile.
    """
    raw_data = fetch_instrument_data(identifier)
    normalized_data = normalize_instrument_data(raw_data)
    if not validate_instrument_data(normalized_data):
        raise ValueError(f"Instrument data for {identifier} failed validation.")
    return normalized_data
