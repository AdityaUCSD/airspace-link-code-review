import geopandas as gpd
import numpy as np


def fake_data_setup(number_records: int = 10000) -> None:
    """
    Creates a geodataframe with some fake data in it for testing purposes
    :param number_records: Number of records to include in the geodataframe
    """
    colors = ['red', 'orange', 'blue', 'magenta', 'magenta', 'magenta']
    df = gpd.GeoDataFrame(np.arange(number_records), columns=["id"])
    df['geometry'] = df.id.apply(lambda i: f"POINT Z ({160 - i % 320} {60 - i % 120} {i % 1500})")
    df['color'] = df.id.apply(lambda i: colors[i % len(colors)])
    df.to_csv('demo_data.csv', index=False)


if __name__ == '__main__':
    fake_data_setup(10_000_000)
