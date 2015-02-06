import unittest
from dungeon import Dungeon
from fight import Fight
from orc import Orc
from hero import Hero
from weapon import Weapon

class Tests(unittest.TestCase):
    def setUp(self):
        test_dungeon = ["S.##......", "#.##..###.", "#.###.###.", "#.....###.", "###.#####S"]
        self.test_dungeon_data = [list(i) for i in test_dungeon]
        self.map = Dungeon("basic_dungeon.txt")
        self.test_hero = Hero("Bron1", 100, "DragonSlayer")
        self.test_orc = Orc("Bron2", 100, 1.25)
        self.first_weapon = Weapon("BigAxe", 25, 0.2)
        self.second_weapon = Weapon("SmallAxe", 19, 0.7)
        self.line_map = Dungeon("line_map.txt")
    
    def test_init(self): 
        self.assertTrue(self.test_dungeon_data == self.map.dungeon)

    def test_print(self):
        self.assertTrue(self.map.print_map() == "S.##......\n#.##..###.\n#.###.###.\n#.....###.\n###.#####S") 

    def test_spawn(self):
        self.assertTrue(self.map.spawn("player_1",self.test_hero))
        self.assertTrue(self.map.spawn("player_2",self.test_orc))
        self.assertFalse(self.map.spawn("player_3",self.test_hero))

    def test_find_char(self):
        self.assertTrue(self.map.find_char("S") == [0,0])

    def test_set_position(self):
        self.map.set_position([0,0],"H")
        self.assertTrue(self.map.get_on_position([0,0]) == "H")

    def test_get_on_position(self):
        self.assertTrue(self.map.get_on_position([0,0]) == "S")

    def test_move(self):
        self.map.spawn("player_1",self.test_hero)
        self.map.spawn("player_2",self.test_orc)
        self.assertTrue(self.map.move("player_1", "right"))
        self.assertFalse(self.map.move("player_1", "up"))
        self.assertTrue(self.map.move("player_2", "up"))

    def test_spawn_weapon(self):
        self.map.spawn_weapon(self.first_weapon)
        self.assertFalse(self.map.find_char("W") == "err")

    def test_move_weapon(self):
        self.line_map.spawn("player_1", self.test_hero)
        self.line_map.spawn("player_2", self.test_orc)
        self.line_map.spawn_weapon(self.first_weapon)
        self.line_map.spawn_weapon(self.second_weapon)
        self.line_map.move("player_1", "right")
        #player = self.map.players["player_1"]
        first_taken_weapon = self.line_map.players["player_1"][0].weapon
        self.assertTrue(self.line_map.print_map() == ".HWO")
        self.assertTrue(first_taken_weapon in [self.first_weapon, self.second_weapon])
        self.line_map.move("player_1", "right")
        self.assertTrue(self.line_map.print_map() == "..HO")
        self.assertTrue(self.line_map.players["player_1"][0].weapon in [self.first_weapon, self.second_weapon])
        self.assertTrue(self.line_map.players["player_1"][0].weapon != first_taken_weapon)

    def test_move_fight(self):
        self.line_map.spawn("player_1", self.test_hero)
        self.line_map.spawn("player_2", self.test_orc)
        self.line_map.spawn_weapon(self.first_weapon)
        self.line_map.spawn_weapon(self.second_weapon)
        self.line_map.move("player_1", "right")
        self.line_map.move("player_2", "left")
        self.line_map.move("player_1", "right")
        player_1_status = self.line_map.players["player_1"][0].is_alive()
        player_2_status = self.line_map.players["player_2"][0].is_alive()
        self.assertTrue(player_1_status or player_2_status)
        self.assertFalse(player_1_status and player_2_status)


if __name__ == '__main__':
    unittest.main()