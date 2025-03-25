from typing import Dict, List
from flask import request as FlaskRequest


class Calculator1:

    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)

        media_calculate_result = self.__media_calculate(input_data) 
        response = self.__format_response(media_calculate_result)

        return response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body or not isinstance(body["numbers"], list):
            raise ValueError("Body mal formatado! O campo 'numbers' deve ser uma lista.")

        numbers = body["numbers"]

        if not all(isinstance(num, (int, float)) for num in numbers):
            raise ValueError("Todos os elementos em 'numbers' devem ser números.")

        if not numbers:
            raise ValueError("A lista 'numbers' não pode estar vazia.")

        return numbers
    
    def __media_calculate(sel, numbers: List[float]) -> float:
        return sum(numbers) / len(numbers)
    
    def __format_response(self, calc_result: float) -> Dict:
        return{
            "data": {
                "calculator": 1,
                "result": calc_result
            }

        }