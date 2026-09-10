import pytest
from validar_email import validar_email

def test_validar_email_email_valido():
    # Arrange
    email = "arroz@dot.com"
    resultado_esperado = True

    # Act
    resultado = validar_email(email)

    # Assert
    assert resultado == resultado_esperado
 
def test_validar_email_email_invalido():
    # Arrange
    email = "arroz.dot"
    resultado_esperado = False
    
    # Act
    resultado = validar_email(email)
    
    # Assert
    assert resultado == resultado_esperado