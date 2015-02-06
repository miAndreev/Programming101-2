from fight import Fight
from orc import Orc
from hero import Hero
from weapon import Weapon
import random

class Dungeon():

    def __init__(self, path):
        raw_dungeon_file = open(path, "r")
        raw_dungeon = raw_dungeon_file.read()
        raw_dungeon_file.close()
        raw_dungeon = raw_dungeon.split()
        self.dungeon = []
        for line in raw_dungeon:
            self.dungeon.append(list(line))
        self.lines = len(raw_dungeon)
        self.line_leng = len(self.dungeon[0])
        self.players = {}
        self.weapons = {}

    def print_map(self):
        rows = []
        for row in self.dungeon:
            rows.append("".join(row))
        return "\n".join(rows)

    def find_char(self, char):
        for i in range(0, len(self.dungeon)):
            line = self.dungeon[i]
            for y in range(0, len(line)):
                if line[y] == char :
                    return [i,y]
        return "err"

    def set_position(self, pos, new):
        self.dungeon[pos[0]][pos[1]] = new

    def spawn(self, player_name, entity):
        position = self.find_char("S")
        if position == "err":
            return False

        self.players[player_name] = [entity, position]
        if type(entity) is Hero:
            #self.dungeon[position[0]][position[1]] = "H"
            self.set_position(position, "H")
        else:
            #self.dungeon[position[0]][position[1]] = "O"
            self.set_position(position, "O")

        return True

    def get_on_position(self, pos):
        return self.dungeon[pos[0]][pos[1]]

    def move(self, player_name, direction):
        old_position = self.players[player_name]
        old_position = old_position[1]
        if direction is "up":
            new_position = [old_position[0]-1, old_position[1]]
        elif direction is "down":
            new_position = [old_position[0] + 1, old_position[1]]
        elif direction is "left":
            new_position = [old_position[0], old_position[1]- 1]
        else:
            new_position = [old_position[0], old_position[1] + 1]

        change_map_after_move(self, player_name, old_position, new_position)


    def change_map_after_move(self, player_name, old_position, new_position):
        if 0 <= new_position[0] < self.lines and 0 <= new_position[1] < self.line_leng:
            self.players[player_name][1] = new_position
            char_on_new_position = self.get_on_position(new_position)
            if char_on_new_position in {"."}:
                self.set_position(new_position, self.get_on_position(old_position))

            elif char_on_new_position in {"O", "H"}:
                entity_0 = self.players[player_name][0]
                entity_1 = None
                print (self.players)
                for p in self.players.values():
                    a = p[1]

                    if a == new_position:
                        entity_1 = p[0]
                fight = Fight(entity_0, entity_1)
                fight.simulate_fight()

                if entity_0.is_alive():
                    self.set_position(new_position, self.get_on_position(old_position))
                
            elif char_on_new_position in {"W"}:
                self.players[player_name][0].equip_weapon(self.weapons[(new_position[0],new_position[1])])
                del self.weapons[(new_position[0],new_position[1])]
                self.set_position(new_position, self.get_on_position(old_position))
            
            self.set_position(old_position, ".")
            self.players[player_name][1] = new_position
            return True
        
        else:
            return False

    def take_weapon(self, position):
        return self.weapons[position]

    def spawn_weapon(self, weapon):
        found = False
        while not found:
            a = random.randint(0, self.lines-1)
            b = random.randint(0, self.line_leng-1)
            if self.dungeon[a][b] == ".":
                self.weapons[(a,b)] = weapon
                found = True
                self.set_position((a,b), "W")


