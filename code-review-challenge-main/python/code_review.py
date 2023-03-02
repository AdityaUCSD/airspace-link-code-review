import datetime
from pathlib import Path
from shapely.geometry import box
from shapely import wkt


def count_records_in_bounds(csv_file, bounds):
    """
    :param csv_file: Csv file to read
    :param bounds: Spatial extent to query
    :return: (tuple)
        geo_in_bounds (int): count of geometries in bound
        max_categories (list): list of categories with max geometries in bounds
        min_categories (list): list of categories with min geometries in bounds
    """

    color_dict = {}

    with open(csv_file) as cursor:
        # skip csv header row
        next(cursor)

        # init increment
        geo_in_bounds = 0

        for row in cursor:
            # process csv values
            _, geometry, color = row.split(',')
            # remove trailing newline char
            color = color.strip()
            geometry = wkt.loads(geometry)

            # if point is within bounds, increment total and categories
            if bounds.contains(geometry):
                geo_in_bounds = geo_in_bounds + 1
                if color in color_dict:
                    color_dict[color] += 1
                else:
                    color_dict[color] = 1

    # calc min/max within bounds by category 
    cat_max = max(color_dict.values())
    cat_min = min(color_dict.values())

    return \
        geo_in_bounds, \
        [k for k, v in color_dict.items() if v == cat_max], \
        [k for k, v in color_dict.items() if v == cat_min],


if __name__ == '__main__':

    s = datetime.datetime.now()
    result = count_records_in_bounds(
        Path('demo_data.csv'),
        box(-20, -20, 20, 20)
    )

    print(datetime.datetime.now() - s)

    print(result)
