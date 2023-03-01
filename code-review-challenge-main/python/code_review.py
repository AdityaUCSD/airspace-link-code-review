import datetime
from pathlib import Path
from shapely.geometry import box
from shapely import wkt


def count_records_in_bounds(csv_file, bounds):
    """
    :param csv_file: Csv file to read
    :param bounds: Spatial extent to query
    :return: counts
    """
    with open(csv_file) as cursor:
        red = 0
        orange = 0
        blue = 0
        i = 0
        for row in cursor:
            id, geometry, color = row.split(',')
            geometry = wkt.loads(geometry)
            if bounds.contains(geometry):
                i = i + 1
            if color == 'red':
                red = red + 1
            if color == 'orange':
                orange = orange + 1
            if color == 'blue':
                blue = blue + 1

        max = -10000000000
        min = 10000000000
        for x in (red, orange, blue):
            if x > max:
                max = x
            if x < min:
                min = x

        dict_values = {
            'red': red,
            'orange': orange,
            'blue': blue
        }
    return \
        i, \
        [k for k, v in dict_values.items() if v == max][0], \
        [k for k, v in dict_values.items() if v == min][0],


if __name__ == '__main__':

    s = datetime.datetime.now()
    result = count_records_in_bounds(
        Path('demo_data.csv'),
        box(-20, -20, 20, 20)
    )

    print(datetime.datetime.now() - s)

    print(result)
