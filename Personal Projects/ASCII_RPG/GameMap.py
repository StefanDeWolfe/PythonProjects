# Author: Stefan DeWolfe
# Date: 3/2024
#
import os
import random


class Coord:
    def __init__(self, a:int, b:int):
        self.x = a
        self.y = b
    def __str__(self): return f"({self.x},{self.y})"

    def __eq__(self, other):
        return (self.y == other.y and self.x == other.x)


class Tile:
    colors: dict = {"red": "\033[91m",
                    "purple": "\33[95m",
                    "blue": "\33[34m",
                    "blue2": "\33[36m",
                    "blue3": "\33[96m",
                    "green": "\033[92m",
                    "green2": "\033[32m",
                    "brown": "\33[33m",
                    "yellow": "\33[93m",
                    "grey": "\33[37m",
                    "default": "\033[0m"
                    }
    def __init__(self, name:str, symbol:str, color:str = "default", is_colored: bool = True, is_traversable:bool = True):
        self.symbol = f"{Tile.colors[color]}{symbol}{Tile.colors['default']}" if is_colored else symbol
        self.name = name
        self.is_traversable = is_traversable


class PlainsTile(Tile):
    def __init__(self):
        super().__init__(name="plains", symbol=".", color="yellow", is_traversable = True)

class EmptyTile(Tile):
    def __init__(self):
        super().__init__(name="floor", symbol=" ", color="default", is_traversable=False)

class FloorTile(Tile):
    def __init__(self):
        super().__init__(name="floor", symbol=".", color="default", is_traversable=True)


class SavannahTile(Tile):
    def __init__(self):
        super().__init__(name="savannah", symbol=",", color="brown", is_traversable = True)


class DesertTile(Tile):
    def __init__(self):
        super().__init__(name="desert", symbol="~", color="brown", is_traversable = True)


class ForestTile(Tile):
    def __init__(self):
        super().__init__(name="forest", symbol="T", color="green")


class PinesTile(Tile):
    def __init__(self):
        super().__init__(name="pines", symbol="Y", color="green", is_traversable = True)


class MountainTile(Tile):
    def __init__(self):
        super().__init__(name="mountain", symbol="A", color="brown", is_traversable = True)


class WaterTile(Tile):
    def __init__(self):
        super().__init__(name="water", symbol="~", color="blue2", is_traversable=False)


class WallTile(Tile):
    def __init__(self):
        super().__init__(name="wall", symbol="X", color="default", is_traversable=False)


class TownTile(Tile):
    def __init__(self):
        super().__init__(name="town", symbol="H", is_colored=False, is_traversable = True)


class DungeonTile(Tile):
    def __init__(self):
        super().__init__(name="dungeon", symbol="D", is_colored=False, is_traversable = True)


class LadderTile(Tile):
    def __init__(self):
        super().__init__(name="dungeon", symbol="#", is_colored=False, is_traversable = True)


class GameMap:
    plains = PlainsTile()
    forest = ForestTile()
    pines = PinesTile()
    mountain = MountainTile()
    savannah = SavannahTile()
    desert = DesertTile()
    water = WaterTile()
    town = TownTile()
    dungeon = DungeonTile()
    floor_tile = FloorTile()
    wall = WallTile()
    ladder = LadderTile()
    empty = EmptyTile()
    no_placement_tiles = [water, town, dungeon]

    def __init__(self,
                 width: int,
                 height: int,
                 player_symbol: str = "ጰ",
                 player_color:str = "red",
                 seed: int = None,
                 can_travel_on_water: bool = False,
                 ) -> None:
        self.name = None
        self.player = None  # Location of player.
        self.seed = seed
        self.width = width
        self.height = height
        self.map_data: list[list[Tile]] = []  # 2D array of lists of strings
        self.player_symbol = f"{Tile.colors[player_color]}{player_symbol}{Tile.colors['default']}"
        self.can_travel_on_water = can_travel_on_water

    def is_clear(self, x: int, y: int, bad_tiles: list[Tile] = None):
        if bad_tiles is None:
            bad_tiles = GameMap.no_placement_tiles
        return self.map_data[y][x] not in bad_tiles

    def can_player_move(self, x: int, y: int):
        return (not self.can_travel_on_water and isinstance(self.map_data[y][x], WaterTile))
    def move_player(self, x: int, y: int):
        if self.can_player_move(x, y):
            return False
        else:
            self.player.x = x
            self.player.y = y
            return True


    def get_available_movement_directions(self):
        directions = ["North", "East", "South", "West"]
        if self.player.y <= 0 or self.can_player_move(self.player.x, self.player.y-1):
            directions.remove("North")
        if self.player.x >= self.width or self.can_player_move(self.player.x+1, self.player.y):
            directions.remove("East")
        if self.player.y >= self.height or self.can_player_move(self.player.x, self.player.y+1):
            directions.remove("South")
        if self.player.x <= 0 or self.can_player_move(self.player.x-1, self.player.y):
            directions.remove("West")
        return directions


    def add_site(self,
                 tile: Tile,
                 x: int,
                 y: int,
                 bad_tiles: list[Tile] = None):
        if bad_tiles is None:
            bad_tiles = GameMap.no_placement_tiles
        if self.is_clear(x, y, bad_tiles):
            self.map_data[y][x] = tile
            return True
        return False

    def generate_patch(self,
                       tile: Tile,
                       num_patches: int,
                       min_size: int,
                       max_size: int,
                       irregular: bool = True) -> None:
        for _ in range(num_patches):
            width = random.randint(min_size, max_size)
            height = random.randint(min_size, max_size)
            start_x = random.randint(1, self.width - width -1)
            start_y = random.randint(1, self.height - height -1)
            initial_start_x = 0
            if irregular:
                initial_start_x = random.randint(3, self.width - max_size)
            for i in range(height):
                if irregular:
                    width = random.randint(int(max_size*0.7), max_size)
                    start_x = initial_start_x - random.randint(1,2)
                for j in range(width):
                    self.map_data[start_y+i][start_x+j] = tile

    def generate_coastlines(self, map_edge: int, min_size: int, max_size: int, irregular: bool = True):
        start_x = 0
        start_y = 0
        if map_edge == 0:  # North Coast
            for j in range(self.width):
                for i in range(min_size):
                    self.map_data[start_y + i][start_x + j] = GameMap.water
        elif map_edge == 1:  # East Coast
            start_x = self.width - min_size
            for j in range(min_size):
                for i in range(self.height):
                    self.map_data[start_y + i][start_x + j] = GameMap.water

        elif map_edge == 2:  # South Coast
            start_y = self.height - min_size
            for j in range(self.width):
                for i in range(min_size):
                    self.map_data[start_y + i][start_x + j] = GameMap.water
        else:
            for j in range(min_size):
                for i in range(self.height):
                    self.map_data[start_y + i][start_x + j] = GameMap.water

    def generate_map(self,
                     forest_patches: list[int],
                     pines_patches: list[int],
                     mountain_patches: list[int],
                     savannah_patches: list[int],
                     desert_patches: list[int],
                     water_patches: list[int],
                     overwrite: bool = True
                     ) -> None:
        if self.seed:
            random.seed(self.seed)
        if overwrite:
            self.map_data = [[GameMap.plains for _ in range(self.width)] for _ in range(self.height)]
        self.generate_patch(tile=GameMap.forest,
                            num_patches=forest_patches[0],
                            min_size=forest_patches[1],
                            max_size=forest_patches[2]
                            )
        self.generate_patch(tile=GameMap.pines,
                            num_patches=pines_patches[0],
                            min_size=pines_patches[1],
                            max_size=pines_patches[2]
                            )
        self.generate_patch(tile=GameMap.mountain,
                            num_patches=mountain_patches[0],
                            min_size=mountain_patches[1],
                            max_size=mountain_patches[2]
                            )
        self.generate_patch(tile=GameMap.savannah,
                            num_patches=savannah_patches[0],
                            min_size=savannah_patches[1],
                            max_size=savannah_patches[2]
                            )
        self.generate_patch(tile=GameMap.desert,
                            num_patches=desert_patches[0],
                            min_size=desert_patches[1],
                            max_size=desert_patches[2]
                            )
        self.generate_patch(tile=GameMap.water,
                            num_patches=water_patches[0],
                            min_size=water_patches[1],
                            max_size=water_patches[2]
                            )

    def display(self) -> None:
        frame = "x" + "=" * self.width + "x"
        print(frame)
        for row in self.map_data:
            row_tiles = [tile.symbol for tile in row]
            if self.player and self.map_data.index(row) == self.player.y:
                row_tiles[self.player.x] = self.player_symbol
            print("|" + "".join(row_tiles) + "|")
        print(frame)

    def display_part(self, x_offset: int = 0, y_offset: int = 0, width: int = 20, height: int = 10) -> None:
        if x_offset >= self.width:
            raise IndexError("IndexError in GameMap.display_part: The x offset is greater than the width of the map!")
        if y_offset >= self.height:
            raise IndexError("IndexError in GameMap.display_part: The y offset is greater than the height of the map!")
        if width >= self.width:
            width = self.width - x_offset
        if height >= self.height:
            height = self.height - y_offset
        frame = "x" + "=" * width + "x"
        print(frame)
        for row in self.map_data[y_offset:y_offset+height]:
            row_tiles = [tile.symbol for tile in row[x_offset:x_offset + width]]

            if self.player and self.map_data[y_offset:y_offset+height].index(row) == self.player.y-y_offset:
                row_tiles[self.player.x-x_offset] = self.player_symbol

            print("|" + "".join(row_tiles) + "|")
        print(frame)


class OverworldMap(GameMap):

    def __init__(self,
                 width: int,
                 height: int,
                 player_symbol: str = "ጰ",
                 player_color:str = "red",
                 seed: int = None,
                 can_travel_on_water: bool = False,
                 ) -> None:
        super().__init__(
            width=width,
             height=height,
             player_symbol=player_symbol,
             player_color=player_color,
             seed=seed,
             can_travel_on_water=can_travel_on_water)
        self.towns = {}  # Dictionary of Towns
        self.dungeons = {}  # Dictionary of Dungeons {Coord(x,y): Dungeon}
        self.encounters = {}  # Filled out after creation
        self.random_encounter_chance = 30  # percent


    def is_clear(self, x: int, y: int, bad_tiles: list[Tile] = None):
        if bad_tiles is None:
            bad_tiles = GameMap.no_placement_tiles
        return self.map_data[y][x] not in bad_tiles

    def can_player_move(self, x: int, y: int):
        return not self.can_travel_on_water and isinstance(self.map_data[y][x], WaterTile)
    def move_player(self, x: int, y: int):
        if self.can_player_move(x, y):
            return False
        else:
            self.player.x = x
            self.player.y = y
            return True


    def get_available_movement_directions(self):
        directions = ["North", "East", "South", "West"]
        if self.player.y <= 0 or self.can_player_move(self.player.x, self.player.y-1):
            directions.remove("North")
        if self.player.x >= self.width or self.can_player_move(self.player.x+1, self.player.y):
            directions.remove("East")
        if self.player.y >= self.height or self.can_player_move(self.player.x, self.player.y+1):
            directions.remove("South")
        if self.player.x <= 0 or self.can_player_move(self.player.x-1, self.player.y):
            directions.remove("West")
        return directions


    def add_site(self,
                 tile: Tile,
                 x: int,
                 y: int,
                 bad_tiles: list[Tile] = None):
        if bad_tiles is None:
            bad_tiles = GameMap.no_placement_tiles
        if self.is_clear(x, y, bad_tiles):
            self.map_data[y][x] = tile
            return True
        return False

    def generate_patch(self,
                       tile: Tile,
                       num_patches: int,
                       min_size: int,
                       max_size: int,
                       irregular: bool = True) -> None:
        for _ in range(num_patches):
            width = random.randint(min_size, max_size)
            height = random.randint(min_size, max_size)
            start_x = random.randint(1, self.width - width -1)
            start_y = random.randint(1, self.height - height -1)
            initial_start_x = 0
            if irregular:
                initial_start_x = random.randint(3, self.width - max_size)
            for i in range(height):
                if irregular:
                    width = random.randint(int(max_size*0.7), max_size)
                    start_x = initial_start_x - random.randint(1,2)
                for j in range(width):
                    self.map_data[start_y+i][start_x + j] = tile

    def generate_coastlines(self, map_edge: int, min_size: int, max_size: int, irregular: bool = True):
        start_x = 0
        start_y = 0
        if map_edge == 0:  # North Coast
            for j in range(self.width):
                for i in range(min_size):
                    self.map_data[start_y + i][start_x + j] = GameMap.water
        elif map_edge == 1:  # East Coast
            start_x = self.width - min_size
            for j in range(min_size):
                for i in range(self.height):
                    self.map_data[start_y + i][start_x + j] = GameMap.water

        elif map_edge == 2:  # South Coast
            start_y = self.height - min_size
            for j in range(self.width):
                for i in range(min_size):
                    self.map_data[start_y + i][start_x + j] = GameMap.water
        else:
            for j in range(min_size):
                for i in range(self.height):
                    self.map_data[start_y + i][start_x + j] = GameMap.water

    def generate_map(self,
                     forest_patches: list[int],
                     pines_patches: list[int],
                     mountain_patches: list[int],
                     savannah_patches: list[int],
                     desert_patches: list[int],
                     water_patches: list[int],
                     overwrite: bool = True
                     ) -> None:
        if self.seed:
            random.seed(self.seed)
        if overwrite:
            self.map_data = [[GameMap.plains for _ in range(self.width)] for _ in range(self.height)]
        self.generate_patch(tile=GameMap.forest,
                            num_patches=forest_patches[0],
                            min_size=forest_patches[1],
                            max_size=forest_patches[2]
                            )
        self.generate_patch(tile=GameMap.pines,
                            num_patches=pines_patches[0],
                            min_size=pines_patches[1],
                            max_size=pines_patches[2]
                            )
        self.generate_patch(tile=GameMap.mountain,
                            num_patches=mountain_patches[0],
                            min_size=mountain_patches[1],
                            max_size=mountain_patches[2]
                            )
        self.generate_patch(tile=GameMap.savannah,
                            num_patches=savannah_patches[0],
                            min_size=savannah_patches[1],
                            max_size=savannah_patches[2]
                            )
        self.generate_patch(tile=GameMap.desert,
                            num_patches=desert_patches[0],
                            min_size=desert_patches[1],
                            max_size=desert_patches[2]
                            )
        self.generate_patch(tile=GameMap.water,
                            num_patches=water_patches[0],
                            min_size=water_patches[1],
                            max_size=water_patches[2]
                            )

    def display(self) -> None:
        frame = "x" + "=" * self.width + "x"
        print(frame)
        for row in self.map_data:
            row_tiles = [tile.symbol for tile in row]
            if self.map_data.index(row) == self.player.y:
                row_tiles[self.player.x] = self.player_symbol
            print("|" + "".join(row_tiles) + "|")
        print(frame)

    def display_part(self, x_offset: int = 0, y_offset: int = 0, width: int = 20, height: int = 10) -> None:
        if x_offset >= self.width:
            raise IndexError("IndexError in GameMap.display_part: The x offset is greater than the width of the map!")
        if y_offset >= self.height:
            raise IndexError("IndexError in GameMap.display_part: The y offset is greater than the height of the map!")
        if width >= self.width:
            width = self.width - x_offset
        if height >= self.height:
            height = self.height - y_offset
        frame = "x" + "=" * width + "x"
        print(frame)
        for row in self.map_data[y_offset:y_offset+height]:
            row_tiles = [tile.symbol for tile in row[x_offset:x_offset + width]]

            if self.map_data[y_offset:y_offset+height].index(row) == self.player.y-y_offset:
                row_tiles[self.player.x-x_offset] = self.player_symbol

            print("|" + "".join(row_tiles) + "|")
        print(frame)

class DungeonMap(GameMap):
    def __init__(self,
                 width: int,
                 height: int,
                 player_symbol: str = "ጰ",
                 player_color: str = "red",
                 seed: int = None,
                 can_travel_on_water: bool = False,
                 item_to_unlock=None,
                 levels: int = 1,
                 boss=None,
                 ) -> None:
        super().__init__(
            width=width,
            height=height,
            player_symbol=player_symbol,
            player_color=player_color,
            seed=seed,
            can_travel_on_water=can_travel_on_water)
        self.current_level = 0
        self.item_to_unlock = item_to_unlock
        self.levels = levels
        self.dungeon_data = {}
        self.boss = boss
        self.encounters = {}  # Filled out after creation
        self.random_encounter_chance = 30  # percent

    def check_locked(self):
        return self.item_to_unlock is None

    def generate_dungeon(self,
        room_patches: list[int],
        corridor_patches: list[int],
        hidden_room_patches: list[int],
        overwrite: bool = True,
        irregular:bool = False
        ) -> None:
        if self.seed:
            random.seed(self.seed)

        for level in range(self.levels):
            if overwrite:
                self.dungeon_data[level] = [[GameMap.empty for _ in range(self.width)] for _ in range(self.height)]
            room_centers = []
            number_of_rooms = room_patches[0]
            for _ in range(number_of_rooms):
                width = random.randint(room_patches[1], room_patches[2])
                height = random.randint(room_patches[1], room_patches[2])
                room_centers.append([
                    Coord(random.randint(0, self.width), random.randint(0, self.height)),
                    width-2,
                    height-2
                ])
                start_x = random.randint(1, self.width - width - 1)
                start_y = random.randint(1, self.height - height - 1)
                for i in range(height):
                    for j in range(width):
                        self.dungeon_data[level][start_y + i][start_x + j] = GameMap.wall

                # width = width-2
                # height = height-2
                # start_x += 1
                # start_y += 1
                # for i in range(height):
                #     for j in range(width):
                #         self.dungeon_data[level][start_y + i][start_x + j] = GameMap.floor_tile
            for room in room_centers:
                other_rooms = list(room_centers).remove(room)
                other_room = random.choice(other_rooms)
                width = random.randint(corridor_patches[1], corridor_patches[2])
                height = random.randint(corridor_patches[1], corridor_patches[2])
                start_x = room[0].x
                start_y = room[0].y
                for i in range(height):
                    for j in range(width):
                        self.dungeon_data[level][start_y + i][start_x + j] = GameMap.wall





        self.map_data = self.dungeon_data[0]


def map_tests():
    overworld = OverworldMap(width=80, height=40, seed=12345)
    overworld.generate_map(
        forest_patches=[8, 3, 10],
        pines_patches=[8, 3, 10],
        mountain_patches=[8, 3, 10],
        savannah_patches=[5, 3, 10],
        desert_patches=[4, 3, 10],
        water_patches=[8, 3, 10]
    )
    for _ in range(3):
        while not overworld.add_site(
                tile=GameMap.town,
                x=random.randint(0, overworld.width),
                y=random.randint(0, overworld.height),
                ):
            pass
    for _ in range(3):
        while not overworld.add_site(
                tile=GameMap.dungeon,
                x=random.randint(0, overworld.width),
                y=random.randint(0, overworld.height),
                ):
            pass
    # overworld.generate_coastlines(map_edge=0, min_size=2, max_size=4, irregular=True)
    # overworld.generate_coastlines(map_edge=1, min_size=1, max_size=3, irregular=True)
    # overworld.generate_coastlines(map_edge=2, min_size=3, max_size=4, irregular=True)
    # overworld.generate_coastlines(map_edge=3, min_size=5, max_size=8, irregular=True)
    overworld.player = Coord(overworld.width // 2, overworld.height // 2)
    overworld.display()
    overworld.display_part(
        x_offset=overworld.player.x-10, y_offset=overworld.player.y-5,
        width=20, height=10
    )
    player_movement = 3
    print(f"Move player West {player_movement}")
    print(f"Moved Player: {overworld.move_player(x=overworld.player.x-player_movement, y=overworld.player.y)}")
    overworld.player.x -= player_movement
    overworld.display_part(
        x_offset=overworld.player.x - 10, y_offset=overworld.player.y - 5,
        width=20, height=10
    )

    dungeon = DungeonMap(width=60, height=30, seed=54321, levels=1)
    dungeon.generate_dungeon(
        room_patches=[4, 6, 9],
        corridor_patches=[],
        hidden_room_patches=[],
        overwrite=True,
        irregular=False
        )
    dungeon.display()

if __name__ == "__main__":
    os.system("")
    map_tests()
