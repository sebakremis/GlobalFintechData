"""
schema
======

Defines the standard schema for descriptive financial instrument data
used by the `instrument_profile` module.

The schema is designed to be:
- Standards-aligned (ISO 6166 for ISIN, ISO 10962 for CFI, ISO 10383 for MIC, LEI)
- Descriptive-first, focusing on static and semi-static attributes
- Extensible for future enrichment (e.g., corporate actions, ratings, ESG data)

Each field definition includes:
- `type`: Expected Python type
- `required`: Whether the field must be present
- `description`: Human-readable explanation of the field
- `example`: Example value for clarity
"""

INSTRUMENT_SCHEMA = {
    "isin": {
        "type": str,
        "required": True,
        "description": "International Securities Identification Number (ISO 6166)",
        "example": "US0378331005"
    },
    "ticker": {
        "type": str,
        "required": False,
        "description": "Exchange ticker symbol",
        "example": "AAPL"
    },
    "cusip": {
        "type": str,
        "required": False,
        "description": "CUSIP identifier (North America)",
        "example": "037833100"
    },
    "sedol": {
        "type": str,
        "required": False,
        "description": "SEDOL identifier (UK)",
        "example": "2046251"
    },
    "issuer_name": {
        "type": str,
        "required": True,
        "description": "Full legal name of the issuing entity",
        "example": "Apple Inc."
    },
    "issuer_country": {
        "type": str,
        "required": True,
        "description": "Country of issuance (ISO 3166-1 alpha-2 code)",
        "example": "US"
    },
    "instrument_type": {
        "type": str,
        "required": True,
        "description": "Type of instrument (e.g., Equity, Bond, ETF)",
        "example": "Equity"
    },
    "sector": {
        "type": str,
        "required": False,
        "description": "Economic sector classification",
        "example": "Technology"
    },
    "industry": {
        "type": str,
        "required": False,
        "description": "Industry classification",
        "example": "Consumer Electronics"
    },
    "mic": {
        "type": str,
        "required": False,
        "description": "Market Identifier Code (ISO 10383) of the primary listing",
        "example": "XNAS"
    },
    "cfi_code": {
        "type": str,
        "required": False,
        "description": "Classification of Financial Instruments code (ISO 10962)",
        "example": "ESVUFR"
    },
    "listing_date": {
        "type": str,
        "required": False,
        "description": "Date of initial listing (YYYY-MM-DD)",
        "example": "1980-12-12"
    },
    "maturity_date": {
        "type": str,
        "required": False,
        "description": "Maturity date for debt instruments (YYYY-MM-DD)",
        "example": None
    },
    "currency": {
        "type": str,
        "required": False,
        "description": "Trading currency (ISO 4217 code)",
        "example": "USD"
    },
    "dividend_policy": {
        "type": str,
        "required": False,
        "description": "Summary of dividend policy (if applicable)",
        "example": "Quarterly dividends"
    },
    "coupon_rate": {
        "type": float,
        "required": False,
        "description": "Coupon rate for fixed income instruments (percentage)",
        "example": None
    },
    "rating": {
        "type": str,
        "required": False,
        "description": "Credit rating (if applicable)",
        "example": "AA+"
    },
    "last_updated": {
        "type": str,
        "required": True,
        "description": "Timestamp of last data update (ISO 8601)",
        "example": "2025-08-31T20:00:00Z"
    }
}
