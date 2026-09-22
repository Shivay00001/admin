"""Minimal license manager backing the admin key-generator UI.

key_gen_ui.py expects:
  - LicensePlans with BASIC / PRO / ENTERPRISE / TRIAL members
  - get_license_manager() returning an object with generate_license_key(plan)

Keys encode the plan in a prefix followed by a random component, matching
the scheme described in key_gen_ui.py ("simple generation logic encodes
Plan in prefix").
"""
import secrets


class LicensePlans:
    BASIC = "BASIC"
    PRO = "PRO"
    ENTERPRISE = "ENTERPRISE"
    TRIAL = "TRIAL"


class LicenseManager:
    """Generates random license keys prefixed by plan name."""

    def generate_license_key(self, plan: str) -> str:
        prefix = str(plan).upper()
        token = secrets.token_hex(8).upper()
        return f"{prefix}-{token[0:4]}-{token[4:8]}-{token[8:12]}-{token[12:16]}"


_manager: LicenseManager | None = None


def get_license_manager() -> LicenseManager:
    global _manager
    if _manager is None:
        _manager = LicenseManager()
    return _manager
