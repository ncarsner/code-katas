import requests
import json
import os
import random
import matplotlib.pyplot as plt
from shapely.geometry import shape, Polygon, MultiPolygon


def save_county_polygons(counties):
    # Ensure the output directory exists
    output_dir = "data/raw/county_polygons"
    os.makedirs(output_dir, exist_ok=True)

    nominatim_url = "https://nominatim.openstreetmap.org/search"

    for county, state in counties:
        params = {
            "q": f"{county} County, {state}, USA",  # Specify the county and state
            "format": "json",  # Request JSON format
            "polygon_geojson": 1,  # Request polygon in GeoJSON format
        }

        response = requests.get(
            nominatim_url, params=params, headers={"User-Agent": "Mozilla/5.0"}
        )

        if response.status_code == 200:
            data = response.json()

            if data:
                county_data = data[0]
                if "geojson" in county_data:
                    polygon = county_data["geojson"]

                    # Define the output file path
                    output_path = os.path.join(
                        output_dir,
                        f"{county.lower().replace(' ', '_')}_county_{state.lower()}.json",
                    )

                    # Write polygon data to the file
                    with open(output_path, "w") as f:
                        json.dump(polygon, f)

                    print(
                        f"Polygon data for {county} County, {state} saved to {output_path}"
                    )
                else:
                    print(f"No polygon data found for {county} County, {state}.")
            else:
                print(f"No results found for {county} County, {state}.")
        else:
            print(
                f"Error fetching data for {county} County, {state}: {response.status_code}"
            )


# Example usage with specified counties
counties = [("Knox", "Tennessee"), ("Davidson", "Tennessee"), ("Cook", "Illinois")]

save_county_polygons(counties)


def plot_random_county_polygon(directory="data/raw/county_polygons"):
    # List all JSON files in the specified directory
    files = [f for f in os.listdir(directory) if f.endswith(".json")]

    if not files:
        print("No JSON files found in the directory.")
        return

    # Select a random JSON file
    random_file = random.choice(files)
    file_path = os.path.join(directory, random_file)

    # Load polygon data from the selected JSON file
    with open(file_path, "r") as f:
        geojson_data = json.load(f)

    # Convert GeoJSON data to a Shapely shape
    polygon = shape(geojson_data)

    # Initialize a plot
    fig, ax = plt.subplots()

    # Plot depending on whether it's a Polygon or MultiPolygon
    if isinstance(polygon, Polygon):
        # For a single Polygon, plot the exterior boundary
        x, y = polygon.exterior.xy
        ax.plot(x, y, color="blue")
    elif isinstance(polygon, MultiPolygon):
        # For a MultiPolygon, iterate through each polygon in the collection
        for poly in polygon.geoms:
            x, y = poly.exterior.xy
            ax.plot(x, y, color="blue")

    # Set aspect ratio and title
    ax.set_aspect("equal")
    ax.set_title(f"Random County Polygon: {random_file}")

    # Display the plot
    plt.show()


# Example usage
plot_random_county_polygon()
