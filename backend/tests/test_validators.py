import pytest
from validators import check_date_format, check_date

# Test check_date_format
def test_check_date_format_valid():
    assert check_date_format("2023-12-31") == True

def test_check_date_format_invalid():
    assert check_date_format("2023/12/31") == False  # Wrong separator
    assert check_date_format("2023-13-01") == False  # Invalid month
    assert check_date_format("2023-02-30") == False  # Invalid day
    assert check_date_format("23-12-31") == False    # Short year
    assert check_date_format("2023-12-31T00:00:00") == False  # Includes time
    assert check_date_format("") == False            # Empty string
    assert check_date_format(None) == False          # None input

# Test check_date
def test_check_date_valid():
    assert check_date("1970-01-01") == True
    assert check_date("2023-12-31") == True

def test_check_date_invalid():
    assert check_date("1969-12-31") == False
    assert check_date("0001-01-01") == False
    assert check_date("invalid-date") == False
    assert check_date(None) == False

# Optional: Test edge cases
def test_leap_year_handling():
    assert check_date_format("2020-02-29") == True   # Valid leap year
    assert check_date_format("2023-02-29") == False  # Invalid leap day