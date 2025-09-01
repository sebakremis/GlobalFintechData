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


def validate_instrument_data(data: Dict[str, Any]) -> bool:
    """
    Validate that the normalized instrument data meets schema requirements.

    Args:
        data (dict): Normalized instrument data.

    Returns:
        bool: True if data passes validation, False otherwise.
    """
    required_fields = {
        "isin": str,
        "ticker": str,
        "issuer_name": str,
        "issuer_country": str,
        "instrument_type": str,
        "mic": str,
        "listing_date": str,
        "currency": str,
        "last_updated": str,
    }
    optional_fields = {
        "cusip": (str, type(None)),
        "sedol": (str, type(None)),
        "sector": (str, type(None)),
        "industry": (str, type(None)),
        "cfi_code": (str, type(None)),
        "maturity_date": (str, type(None)),
        "dividend_policy": (str, type(None)),
        "coupon_rate": (float, type(None)),
        "rating": (str, type(None)),
    }

    # Check required fields
    for field, field_type in required_fields.items():
        if field not in data or not isinstance(data[field], field_type):
            return False

    # Check optional fields if present
    for field, field_types in optional_fields.items():
        if field in data and not isinstance(data[field], field_types):
            return False

    return True


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
