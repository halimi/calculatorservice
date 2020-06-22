from pyramid.response import Response
from pyramid.view import view_config
from calculator.simple import SimpleCalculator


class CalculatorServiceViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(self):
        return Response('<body>For the calculator use <a href="/calculator">calculator</a></body>')

    @view_config(
        route_name='calculator',
        request_method='POST',
        renderer='json'
    )
    def calculator(self):
        calculator = SimpleCalculator()
        #FIXME: Add exception handling
        calc = self.request.json_body["input"]
        calculator.run(calc)
        return {'result': str(calculator.lcd)}
