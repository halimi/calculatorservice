import unittest

from pyramid import testing


class CalculatorServiceViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from .views import CalculatorServiceViews

        request = testing.DummyRequest()
        inst = CalculatorServiceViews(request)
        response = inst.home()
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'For the calculator', response.body)

    def test_calculator(self):
        from .views import CalculatorServiceViews

        request = testing.DummyRequest(
            json_body={"input": "3 + 2"}, method='POST')
        inst = CalculatorServiceViews(request)
        response = inst.calculator()
        self.assertEqual('5.0', response['result'])


class CalculatorFunctionalTests(unittest.TestCase):
    def setUp(self):
        from calculatorservice import main
        app = main()
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        self.assertIn(b'For the calculator', res.body)

    def test_calculator_get(self):
        res = self.testapp.get('/calculator', status=404)
        self.assertIn(b'request_method = POST', res.body)

    def test_calculator_post(self):
        res = self.testapp.post_json('/calculator', params={'input': '5 - 3'})
        self.assertEqual('2.0', res.json['result'])
