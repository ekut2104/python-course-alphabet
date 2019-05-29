class Cat:

    def __init__(self, age: int):
        self._set_average_speed(age)
        self._saturation_level = 50

    def eat(self, product):
        val = 0
        if product == 'fodder':
            val = 10
        elif product == 'apple':
            val = 5
        elif product == 'milk':
            val = 2

        self._increase_saturation_level(val)

    def _reduce_saturation_level(self, value: int):
        self._saturation_level -= value
        self._saturation_level = self._saturation_level if self._saturation_level >= 0 else 0

    def _increase_saturation_level(self, value: int):
        self._saturation_level += value
        self._saturation_level = self._saturation_level if self._saturation_level <= 100 else 100

    def _set_average_speed(self, age: int):
        if age <= 7:
            self._average_speed = 12
        elif 7 < age <= 10:
            self._average_speed = 9
        else:
            self._average_speed = 6

    def run(self, hours: int):
        distance = self.get_average_speed() * hours

        if distance <= 25:
            self._reduce_saturation_level(2)
        elif 25 < distance <= 50:
            self._reduce_saturation_level(5)
        elif 50 < distance <= 100:
            self._reduce_saturation_level(15)
        elif 100 < distance <= 200:
            self._reduce_saturation_level(25)
        else:
            self._reduce_saturation_level(50)

        return f'Your cat ran {distance} kilometers'

    def get_saturation_level(self):
        return self._saturation_level if self._saturation_level > 0 else 'Your cat is died :('

    def get_average_speed(self):
        return self._average_speed


class Cheetah(Cat):

    def eat(self, product):
        val = 0
        if product == 'gazelle':
            val = 30
        elif product == 'rabbit':
            val = 15

        self._increase_saturation_level(val)

    def _set_average_speed(self, age: int):
        if age <= 5:
            self._average_speed = 90
        elif 5 < age <= 15:
            self._average_speed = 75
        else:
            self._average_speed = 40


class Wall:

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def wall_square(self):
        return self.width * self.height

    def number_of_rolls_of_wallpaper(self, roll_width_m: float, roll_length_m: float):

        lines = roll_length_m // self.height
        lines_in_roll = self.width // roll_width_m

        return lines_in_roll / lines


class Roof:

    def __init__(self, width: float, height: float, roof_type: str):
        self.width = width
        self.height = height
        self.roof_type = roof_type

    def roof_square(self):
        if self.roof_type == 'gable':
            return self.width * self.height * 2
        elif self.roof_type == 'single-pitch':
            return self.width * self.height
        else:
            raise ValueError('Sorry there is only two types of roofs')


class Window:

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def window_square(self):
        return self.width * self.height


class Door:

    wood_price = 10
    metal_price = 3

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def door_square(self):
        return self.width * self.height

    def door_price(self, material: str):
        if material == 'wood':
            return self.door_square() * self.wood_price
        elif material == 'metal':
            return self.door_square() * self.metal_price
        else:
            raise ValueError('Sorry we don\'t have such material')

    def update_wood_price(self, price: int):
        self.wood_price = price

    def update_metal_price(self, price: int):
        self.metal_price = price


class House:

    def __init__(self):
        self.__walls = []
        self.__windows = []
        self.__roof = None
        self.__door = None

    def create_wall(self, width: float, height: float):
        if width == 0 or height == 0:
            raise ValueError('Value must be not 0')
        if self.get_count_of_walls() == 4:
            raise ValueError('Our house can not have more than 4 walls')

        self.__walls.append(Wall(width, height))

    def create_roof(self, width: float, height: float, roof_type: str):
        if width == 0 or height == 0:
            raise ValueError('Value must be not 0')
        if self.__roof is not None:
            raise ValueError('The house can not have two roofs')

        self.__roof = Roof(width, height, roof_type)

    def create_window(self, width: float, height: float):
        if width == 0 or height == 0:
            raise ValueError('Value must be not 0')

        self.__windows.append(Window(width, height))

    def create_door(self, width: float, height: float):
        if width == 0 or height == 0:
            raise ValueError('Value must be not 0')
        if self.__door is not None:
            raise ValueError('The house can not have two doors')

        self.__door = Door(width, height)

    def get_count_of_walls(self):
        return len(self.__walls)

    def get_count_of_windows(self):
        return len(self.__windows)

    def get_door_price(self, material: str):
        return self.__door.door_price(material)

    def update_wood_price(self, new_wood_price: int):
        self.__door.update_wood_price(new_wood_price)

    def update_metal_price(self, new_metal_price: int):
        self.__door.update_metal_price(new_metal_price)

    def get_roof_square(self):
        return self.__roof.roof_square()

    def get_walls_square(self):
        return sum([wall.wall_square() for wall in self.__walls])

    def get_windows_square(self):
        return sum([window.window_square() for window in self.__windows])

    def get_door_square(self):
        return self.__door.door_square()

    def get_number_of_rolls_of_wallpapers(self, roll_width_m: float, roll_length_m: float):
        if roll_width_m == 0 or roll_length_m == 0:
            raise ValueError('Sorry length must be not 0')

        return sum([wall.number_of_rolls_of_wallpaper(roll_width_m, roll_length_m) for wall in self.__walls])

    def get_room_square(self):
        return self.get_walls_square() - self.get_windows_square() - self.get_door_square()