from flask import Blueprint, jsonify, request
from src.main.factories.calculator1_factory import calculator1_factory
from src.errors.error_controller import handler_errors

calc_route_bp = Blueprint("calc_routes", __name__)


@calc_route_bp.route("/calculator/1", methods=["POST"])
def calculator1():
    try:
        calc = calculator1_factory()
        response = calc.calculate(request)

        return jsonify(response), 200
    except  Exception as exception:
        error_respoonse = handler_errors(exception)
        return jsonify(error_respoonse["body"]), error_respoonse["status_code"]