from gothonweb.planisphere import *
import unittest


class test_planisphere(unittest.TestCase):

    def test_room(self):
        gold = Room("GoldRoom",
                    """This room has gold in it you can grab. There's a
                    door to the north.""")
        self.assertEqual(gold.name, "GoldRoom")
        self.assertEqual(gold.paths, {})

    def test_room_paths(self):
        center = Room("Center", "Test room in the center.")
        north = Room("North", "Test room in the north.")
        south = Room("South", "Test room in the south.")

        center.add_paths({'north': north, 'south': south})

        self.assertEqual(center.go('north'), north)
        self.assertEqual(center.go('south'), south)

    def test_map(self):
        start = Room("Start", "You can go west and down a hole.")
        west = Room("Trees", "There are trees here, you can go east.")
        down = Room("Dungeon", "It's dark down here, you can go up.")

        start.add_paths({'west': west, 'down': down})
        west.add_paths({'east': start})
        down.add_paths({'up': start})

        self.assertEqual(start.go('west'), west)
        self.assertEqual(start.go('west').go('east'), start)
        self.assertEqual(start.go('down').go('up'), start)

    def test_gothon_game_map(self):
        start_room = load_room(START)
        self.assertEqual(start_room.go('shoot!'), shoot_death)
        self.assertEqual(start_room.go('dodge!'), dodge_death)

        room = start_room.go('tell a joke')
        self.assertEqual(room, laser_weapon_armory)

        self.assertEqual(room.go('*'), keypad_death)

        room = room.go('132')
        self.assertEqual(room, the_bridge)

        self.assertEqual(room.go('throw the bomb'), bomb_death)

        room = room.go('slowly place the bomb')
        self.assertEqual(room, escape_pod)

        self.assertEqual(room.go('*'), the_end_loser)

        room = room.go('2')
        self.assertEqual(room, the_end_winner)
