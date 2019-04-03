from app import app
import unittest

app.config['TESTING'] = True
web = app.test_client()


class test_index(unittest.TestCase):

    def test_index(self):
        rv = web.get('/', follow_redirects=True)
        self.assertEqual(rv.status_code, 200)

    def test_dne(self):
        rv = web.get('/dne', follow_redirects=True)
        self.assertEqual(rv.status_code, 404)

    def test_game_get_broken(self):
        rv = web.get('/game', follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b"You Died!", rv.data)

    # def test_hello_post(self):
    #     data = {'room.name': 'central_corridor'}
    #     rv = web.post('/game', follow_redirects=True, data=data)
    #     self.assertIn(b"central_corridor", rv.data)
        # self.assertIn(b"Hola", rv.data)
