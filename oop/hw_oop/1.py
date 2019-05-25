def create_wall(width: float, height: float):
    if width == 0 or height == 0:
        raise ValueError('Value must be not 0')
    print('11111')
    if get_count_of_walls() == 4:
        raise ValueError('Our house can not have more than 4 walls')


def get_count_of_walls():
    return 4


if __name__=='__main__':
    print(create_wall(1, 7))