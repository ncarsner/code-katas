from calculator import Calculator

def test_add():
    # Arrange
    calculator_instance = Calculator()
    # Act
    result = calculator_instance.add(2, 3)
    # Assert
    assert result == 5

def test_subtract():
    # Arrange
    calculator_instance = Calculator()
    # Act
    result = calculator_instance.subtract(3, 4)
    # Assert
    assert result == -1

def test_multiply():
    # Arrange
    calculator_instance = Calculator()
    # Act
    result = calculator_instance.multiply(3, 7)
    # Assert
    assert result == 21

def test_divide():
    # Arrange
    calculator_instance = Calculator()
    # Act
    result = calculator_instance.divide(9, 3)
    # Assert
    assert result == 3
