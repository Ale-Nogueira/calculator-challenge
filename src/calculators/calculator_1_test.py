from typing import Dict
from pytest import raises
from .calculator_1 import Calculator1

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest(body={"numbers": [15, 20, 30]})

    calculator_1 = Calculator1()

    response = calculator_1.calculate(mock_request)
    
    #formato da resposta
    assert "data" in response
    assert "calculator" in response["data"]
    assert "result" in response["data"]

    #Assertividade da resposta
    assert response["data"]["result"] == 21.67
    assert response["data"]["calculator"] == 1
    
def test_calculate_with_body_error():
    mock_request = MockRequest(body={"something": [15, 20, 30]})
    calculator_1 = Calculator1()

    with raises(Exception) as excinfo:
        calculator_1.calculate(mock_request)

    assert str(excinfo.value) == "Body mal formatado! O campo 'numbers' deve ser uma lista."

def test_calculate_with_list_error():
    mock_request = MockRequest(body={"numbers": []})
    calculator_1 = Calculator1()

    with raises(ValueError) as valinfo:
        calculator_1.calculate(mock_request)

    assert str(valinfo.value) == "A lista 'numbers' não pode estar vazia."
