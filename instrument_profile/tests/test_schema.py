"""
Unit tests for instrument_profile schema and validation.

These tests ensure that:
- Required fields are present and of the correct type
- Optional fields can be missing or None
- Incorrect types or missing required fields cause validation to fail
"""

import unittest
from globalfintechdata.instrument_profile.schema import INSTRUMENT_SCHEMA
from globalfintechdata.instrument_profile import validate_instrument_data


class TestInstrumentSchemaValidation(unittest.TestCase):

    def setUp(self):
        """Create a valid sample instrument profile for testing."""
        self.valid_profile = {
            "isin": "US0378331005",
            "ticker": "AAPL",
            "cusip": "037833100",
            "sedol": "2046251",
            "issuer_name": "Apple Inc.",
            "issuer_country": "US",
            "instrument_type": "Equity",
            "sector": "Technology",
            "industry": "Consumer Electronics",
            "mic": "XNAS",
            "cfi_code": "ESVUFR",
            "listing_date": "1980-12-12",
            "maturity_date": None,
            "currency": "USD",
            "dividend_policy": "Quarterly dividends",
            "coupon_rate": None,
            "rating": "AA+",
            "last_updated": "2025-08-31T20:00:00Z"
        }

    def test_valid_profile_passes(self):
        """A fully valid profile should pass validation."""
        self.assertTrue(validate_instrument_data(self.valid_profile))

    def test_missing_required_field_fails(self):
        """Missing a required field should fail validation."""
        profile = self.valid_profile.copy()
        del profile["isin"]  # Remove required field
        self.assertFalse(validate_instrument_data(profile))

    def test_incorrect_type_fails(self):
        """Incorrect type for a field should fail validation."""
        profile = self.valid_profile.copy()
        profile["coupon_rate"] = "5.0"  # Should be float or None
        self.assertFalse(validate_instrument_data(profile))

    def test_optional_fields_can_be_missing(self):
        """Optional fields can be omitted entirely."""
        profile = self.valid_profile.copy()
        del profile["sector"]
        del profile["industry"]
        self.assertTrue(validate_instrument_data(profile))

    def test_optional_fields_can_be_none(self):
        """Optional fields can be None."""
        profile = self.valid_profile.copy()
        profile["sector"] = None
        profile["industry"] = None
        self.assertTrue(validate_instrument_data(profile))


if __name__ == "__main__":
    unittest.main()
