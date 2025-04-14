from datetime import datetime

# Returns true if date is correct format
# Returns false otherwise
def check_date_format(date: str) -> bool:
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        return False

# Returns true if date is 1970+
# Returns false otherwise
def check_date(date: str) -> bool:
    try:
        year = int(date.split("-")[0])
        return year >= 1970
    except (IndexError, ValueError, AttributeError):
        return False