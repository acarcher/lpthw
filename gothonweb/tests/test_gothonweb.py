from app import app
import unittest

app.config['TESTING'] = True


class test_app(unittest.TestCase):

    def setUp(self):
        self.web = app.test_client()

    def test_dne_without_session(self):
        rv = self.web.get('/dne', follow_redirects=True)
        self.assertEqual(rv.status_code, 404)

        rv = self.web.post('/dne', follow_redirects=True)
        self.assertEqual(rv.status_code, 404)

    def test_index_without_session(self):
        rv = self.web.get('/', follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b'Central Corridor', rv.data)

        rv = self.web.post('/', follow_redirects=True)
        self.assertEqual(rv.status_code, 405)

    def test_game_without_session(self):
        rv = self.web.get('/game', follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b'You Died!', rv.data)

        rv = self.web.post('/game', data=dict(action='***'), follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b'You Died!', rv.data)

    def test_corridor_with_session(self):
        with self.web as web:
            with web.session_transaction() as sess:
                sess['room_name'] = 'central_corridor'

            rv = web.get('/game', follow_redirects=True)
            self.assertEqual(rv.status_code, 200)
            self.assertIn(b'Central Corridor', rv.data)

        with self.web as web:
            with web.session_transaction() as sess:
                sess['room_name'] = 'central_corridor'

            rv = web.post('/game', data=dict(action='dodge!'), follow_redirects=True)
            self.assertEqual(rv.status_code, 200)
            self.assertIn(b'death', rv.data)

        with self.web as web:
            with web.session_transaction() as sess:
                sess['room_name'] = 'central_corridor'

            rv = web.post('/game', data=dict(action='shoot!'), follow_redirects=True)
            self.assertEqual(rv.status_code, 200)
            self.assertIn(b'death', rv.data)

        with self.web as web:
            with web.session_transaction() as sess:
                sess['room_name'] = 'central_corridor'

            rv = web.post('/game', data=dict(action='tell a joke'), follow_redirects=True)
            self.assertEqual(rv.status_code, 200)
            self.assertIn(b'Laser Weapon Armory', rv.data)

    def test_armory_with_session(self):
        with self.web as web:
            with web.session_transaction() as sess:
                sess['room_name'] = 'laser_weapon_armory'

            rv = web.get('/game', follow_redirects=True)
            self.assertEqual(rv.status_code, 200)
            self.assertIn(b'Laser Weapon Armory', rv.data)

        with self.web as web:
            with web.session_transaction() as sess:
                sess['room_name'] = 'laser_weapon_armory'

            rv = web.post('/game', data=dict(action='*'), follow_redirects=True)
            self.assertEqual(rv.status_code, 200)
            self.assertIn(b'death', rv.data)

        with self.web as web:
            with web.session_transaction() as sess:
                sess['room_name'] = 'laser_weapon_armory'

            rv = web.post('/game', data=dict(action='132'), follow_redirects=True)
            self.assertEqual(rv.status_code, 200)
            self.assertIn(b'The Bridge', rv.data)

    def test_bridge_with_session(self):
        with self.web as web:
            with web.session_transaction() as sess:
                sess['room_name'] = 'the_bridge'

            rv = web.get('/game', follow_redirects=True)
            self.assertEqual(rv.status_code, 200)
            self.assertIn(b'The Bridge', rv.data)

        with self.web as web:
            with web.session_transaction() as sess:
                sess['room_name'] = 'the_bridge'

            rv = web.post('/game', data=dict(action='throw the bomb'), follow_redirects=True)
            self.assertEqual(rv.status_code, 200)
            self.assertIn(b'death', rv.data)

        with self.web as web:
            with web.session_transaction() as sess:
                sess['room_name'] = 'the_bridge'

            rv = web.post('/game', data=dict(action='slowly place the bomb'), follow_redirects=True)
            self.assertEqual(rv.status_code, 200)
            self.assertIn(b'Escape Pod', rv.data)

    def test_escape_with_session(self):
        with self.web as web:
            with web.session_transaction() as sess:
                sess['room_name'] = 'escape_pod'

            rv = web.get('/game', follow_redirects=True)
            self.assertEqual(rv.status_code, 200)
            self.assertIn(b'Escape Pod', rv.data)

        with self.web as web:
            with web.session_transaction() as sess:
                sess['room_name'] = 'escape_pod'

            rv = web.post('/game', data=dict(action='*'), follow_redirects=True)
            self.assertEqual(rv.status_code, 200)
            self.assertIn(b'jelly', rv.data)

        with self.web as web:
            with web.session_transaction() as sess:
                sess['room_name'] = 'escape_pod'

            rv = web.post('/game', data=dict(action='2'), follow_redirects=True)
            self.assertEqual(rv.status_code, 200)
            self.assertIn(b'You won', rv.data)

