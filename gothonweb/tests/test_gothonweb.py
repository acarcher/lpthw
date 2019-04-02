from app import app
import unittest

app.config['TESTING'] = True
web = app.test_client()


class test_index(unittest.TestCase):

    def test_index(self):
        rv = web.get('/', follow_redirects=True)
        self.assertEqual(rv.status_code, 404)

    def test_hello_get(self):
        rv = web.get('/hello', follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b"Fill Out This Form", rv.data)

    def test_hello_post(self):
        data = {'name': 'Zed', 'greet': 'Hola'}
        rv = web.post('/hello', follow_redirects=True, data=data)
        self.assertIn(b"Zed", rv.data)
        self.assertIn(b"Hola", rv.data)
