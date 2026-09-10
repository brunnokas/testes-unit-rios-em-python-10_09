import pytest

def validar_email(email: str) -> bool:
#verify email (@ and .)
    return "@" in email and "." in email
