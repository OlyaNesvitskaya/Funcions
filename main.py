def direction(facing, turn):
    lst = ('N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW')
    if type(turn) != int or not -1080 <= turn <= 1080 or turn % 45:
        return "Value 'turn' must be number between -1080 and should be a multiple of 45"
    if facing not in lst:
        return f"Select one of the directions {lst}"

    step = turn // 45
    start = lst.index(facing)
    return lst[(step + start) % len(lst)]

