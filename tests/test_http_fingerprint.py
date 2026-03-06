"""Tests for http-fingerprint."""

import pytest
from http_fingerprint import fingerprint


class TestFingerprint:
    """Test suite for fingerprint."""

    def test_basic(self):
        """Test basic usage."""
        result = fingerprint("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            fingerprint("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = fingerprint(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
