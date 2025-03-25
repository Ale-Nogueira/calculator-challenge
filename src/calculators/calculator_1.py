from typing import Dict, List
from flask import request as FlaskRequest
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.http_bad_request import HttpBadRequestError


class Calculator1:

    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)

        average_calculate_result = self.__average_calculate(input_data) 
        response = self.__format_response(average_calculate_result)

        return response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body or not isinstance(body["numbers"], list):
            raise HttpUnprocessableEntityError("Body mal formatado!O campo 'numbers' deve ser uma lista.")

        numbers = body["numbers"]

        if not numbers:
            raise HttpBadRequestError("A lista 'numbers' não pode estar vazia.")

        return numbers
    
    def __average_calculate(sel, numbers: List[float]) -> float:
        return sum(numbers) / len(numbers)
    
    def __format_response(self, calc_result: float) -> Dict:
        return{
            "data": {
                "calculator": 1,
                "result": round(calc_result, 2)
            }

        }