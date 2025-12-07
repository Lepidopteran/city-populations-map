# US City/Town Populations with Latitude and Longitude

This is a little data experiment to see the population numbers of US cities and towns with their respective locations.

This project combines the US Census Bureau's 2020-2024 [City and Town Population Totals](https://www.census.gov/data/tables/time-series/demo/popest/2020s-total-cities-and-towns.html) dataset to get the population numbers with the [US Geographic Names Information System](https://www.usgs.gov/us-board-on-geographic-names/download-gnis-data) Federal Codes dataset to get the latitude and longitude.

I've included them inside the `data/` directory so people don't have to download the datasets themselves.

## Usage

You can download the dataset in GeoJSON or CSV from the [`releases`](https://github.com/Lepidopteran/city-populations-map/releases) page.

Alternatively, you can run the Python script that creates the dataset by running the following commands:

```bash
uv sync
uv run main.py

```

The script will create a GeoJSON file called `city-population-with-lat-lng.geojson` and a CSV file called `city-population-with-lat-lng.csv` in `output/`.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Additionally, please use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) to commit your changes.

Please make sure to update tests as appropriate.

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit).
