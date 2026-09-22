"""Smoke tests for the admin license key generator.

Runnable with pytest, or directly:  python3 tests/test_smoke.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from license.license_manager import LicenseManager, LicensePlans, get_license_manager


def test_plans_defined():
    assert LicensePlans.BASIC == "BASIC"
    assert LicensePlans.PRO == "PRO"
    assert LicensePlans.ENTERPRISE == "ENTERPRISE"
    assert LicensePlans.TRIAL == "TRIAL"


def test_generate_key_encodes_plan():
    lm = get_license_manager()
    assert isinstance(lm, LicenseManager)
    key = lm.generate_license_key(LicensePlans.PRO)
    assert key.startswith("PRO-")
    assert len(key) == len("PRO-") + 19  # 4 groups of 4 hex chars + 3 dashes


def test_keys_are_unique():
    lm = get_license_manager()
    keys = {lm.generate_license_key(LicensePlans.BASIC) for _ in range(100)}
    assert len(keys) == 100


if __name__ == "__main__":
    test_plans_defined()
    test_generate_key_encodes_plan()
    test_keys_are_unique()
    print("smoke test: 3 passed")
