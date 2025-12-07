from pathlib import Path
import polars as pl


def main():
    city_populations = (
        pl.read_csv("./data/city-populations.csv", encoding="utf8-lossy")
        .select(pl.all().name.to_lowercase())
        .with_columns(
            pl.col("name").str.replace_all(" city", ""),
        )
    )

    united_states_lat_long_cities = (
        pl.read_csv(
            "./data/FederalCodes_National.txt",
            separator="|",
            columns=[
                "feature_name",
                "state_name",
                "prim_lat_dec",
                "prim_long_dec",
            ],
        )
        .unique(["prim_lat_dec", "prim_long_dec"])
        .select(
            [
                pl.col("feature_name"),
                pl.col("state_name"),
                pl.col("prim_lat_dec").alias("latitude"),
                pl.col("prim_long_dec").alias("longitude"),
            ]
        )
    )

    city_populations_with_lat_long = (
        city_populations.join_where(
            united_states_lat_long_cities,
            pl.col("name") == pl.col("feature_name"),
            pl.col("state") == pl.col("state_name"),
        )
        .select(
            [
                pl.col("name"),
                pl.col("state"),
                pl.col("population"),
                pl.col("latitude"),
                pl.col("longitude"),
            ]
        )
        .unique(["latitude", "longitude"])
    )

    print("Successfully joined city populations with latitude and longitude data")

    output_path = Path("output")

    if not output_path.exists():
        output_path.mkdir()

    city_populations_with_lat_long.write_csv("./output/city_populations_lat_long.csv")

    features = []
    for row in city_populations_with_lat_long.rows(named=True):
        name = row["name"]
        state = row["state"]
        population = int(row["population"])
        longitude = float(row["longitude"])
        latitude = float(row["latitude"])

        properties: dict[str, object] = {
            "name": name,
            "state": state,
            "population": population,
        }
        geometry: dict[str, object] = {
            "type": "Point",
            "coordinates": [
                longitude,
                latitude,
            ],
        }
        features.append(
            {"type": "Feature", "properties": properties, "geometry": geometry}
        )

    geojson: dict[str, object] = {
        "type": "FeatureCollection",
        "features": features,
    }

    import json

    with open("./output/city_populations_lat_long.geojson", "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
