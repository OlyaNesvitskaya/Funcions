def direction(facing, turn):
    compass_points = ('N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW')
    if type(turn) != int or not -1080 <= turn <= 1080 or turn % 45:
        raise TypeError("Value 'turn' must be number between -1080 and should be a multiple of 45")
    if facing not in compass_points:
        raise TypeError(f"Select one of the directions {compass_points}")

    step = turn // 45
    start = compass_points.index(facing)
    return compass_points[(step + start) % len(compass_points)]

