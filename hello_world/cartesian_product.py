def cartesian_product(ranges: list[list]) -> list[list]:
    points = []
    for val in ranges[0]:
        points.append([val])

    for r in ranges[1:]:
        new = []
        for val in r:
            for point in points:
                copy = point.copy()
                copy.append(val)
                new.append(copy)

        points = new.copy()

    return points

ranges = [
    ['a'],
    [1, 2, 3],
    ['Y', 'Z']
]
print(cartesian_product(ranges))
