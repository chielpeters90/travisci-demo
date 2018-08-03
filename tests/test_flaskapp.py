import unittest, json

from main import app


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_unauthorized(self):
        response = self.app.get('/authorized')
        # Check if the request fails with authorization error
        self.assertEqual(response._status_code, 401, 'Unauthorized access to page without login')

    def test_multiply(self):
        response = self.app.get('/multiply?x=5&y=7')
        resp = json.loads(response.data.decode('utf-8'))
        self.assertEqual(resp['answer'], 35, 'Multiply endpoint failed known answer 7*5 = 35')

    # TODO DEFINE TWO MORE TESTS ON THE END POINTS

    def test_uppercase(self):
        response = self.app.get('/touppercase?s=jadoooeeei')
        resp = json.loads(response.data.decode('utf-8'))
        self.assertEqual(resp['answer'], 'JADOOOEEEI', 'Uppercase endpoint failed known answer jadoooeeei = JADOOOEEEI')

    def test_uppercase(self):
        response = self.app.get('/touppercase?s=OKEDOEI')
        resp = json.loads(response.data.decode('utf-8'))
        self.assertEqual(resp['answer'], 'OKEDOEI', 'Uppercase endpoint failed known answer OKEDOEI = OKEDOEI')


if __name__ == '__main__':
    unittest.main()
