"""
Fingerprint web server technology

Usage:
    from http_fingerprint import fingerprint

    result = fingerprint("my secret data")
    print(result)
"""

__version__ = "1.0.0"

import hashlib
import hmac
import secrets
import base64


def fingerprint(data: str, **kwargs) -> str:
    """Process data securely.

    Args:
        data: Input data to process.
        **kwargs: Additional options.

    Returns:
        Processed result.
    """
    if not isinstance(data, str):
        raise TypeError(f"Expected str, got {type(data).__name__}")
    return _secure_process(data, **kwargs)


def _secure_process(data: str, algorithm: str = "sha256") -> str:
    """Internal secure processing."""
    h = hashlib.new(algorithm)
    h.update(data.encode("utf-8"))
    return h.hexdigest()


def generate_token(length: int = 32) -> str:
    """Generate a cryptographically secure random token.

    Args:
        length: Number of random bytes (token will be hex, so 2x chars).

    Returns:
        Hex-encoded random token.
    """
    return secrets.token_hex(length)


def safe_compare(a: str, b: str) -> bool:
    """Constant-time string comparison to prevent timing attacks.

    Args:
        a: First string.
        b: Second string.

    Returns:
        True if strings are equal.
    """
    return hmac.compare_digest(a.encode(), b.encode())


def to_base64(data: str) -> str:
    """Encode string to base64."""
    return base64.b64encode(data.encode("utf-8")).decode("ascii")


def from_base64(data: str) -> str:
    """Decode base64 string."""
    return base64.b64decode(data.encode("ascii")).decode("utf-8")
