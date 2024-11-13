import os
import json
import random
import requests
import matplotlib.pyplot as plt
from scipy.interpolate import splprep, splev
import numpy as np
from shapely.geometry import shape, Polygon, MultiPolygon
from shapely.geometry.geo import mapping


def save_state_polygons(states):
    # Ensure the output directory exists
    output_dir = "data/raw/state_polygons"
    os.makedirs(output_dir, exist_ok=True)

    nominatim_url = "https://nominatim.openstreetmap.org/search"

    for state in states:
        params = {
            "q": f"{state}, USA",  # Query for the specific state in the USA
            "format": "json",  # Request JSON format
            "polygon_geojson": 1,  # Request polygon in GeoJSON format
        }

        response = requests.get(
            nominatim_url, params=params, headers={"User-Agent": "Mozilla/5.0"}
        )

        if response.status_code == 200:
            data = response.json()

            if data:
                state_data = data[0]
                if "geojson" in state_data:
                    polygon = state_data["geojson"]

                    # Define the output file path
                    output_path = os.path.join(output_dir, f"{state.lower()}.json")

                    # Write polygon data to the file
                    with open(output_path, "w") as f:
                        json.dump(polygon, f)

                    print(f"Polygon data for {state} saved to {output_path}")
                else:
                    print(f"No polygon data found for {state}.")
            else:
                print(f"No results found for {state}.")
        else:
            print(f"Error fetching data for {state}: {response.status_code}")


# Example usage
# states = ["Ohio", "Tennessee", "California", "Texas"]
# states = ["Alabama", "Alaska", "Arizona", "Arkansas", "Colorado", "Connecticut"]
# states = ["Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana"]
# states = ["Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland"]
# states = ["Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana"]
# states = ["Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York"]
# states = ["North Carolina", "North Dakota", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island"]
# states = ["South Carolina", "South Dakota", "Utah", "Vermont", "Virginia", "Washington"]
# states = ["West Virginia", "Wisconsin", "Wyoming"]
# save_state_polygons(states)





# def plot_polygon_from_json(file_path):
#     # Load polygon data from the JSON file
#     with open(file_path, 'r') as f:
#         geojson_data = json.load(f)
    
#     # Convert GeoJSON data to a Shapely shape
#     polygon = shape(geojson_data)
    
#     # Initialize a plot
#     fig, ax = plt.subplots()
    
#     # Plot depending on whether it's a Polygon or MultiPolygon
#     if isinstance(polygon, Polygon):
#         # For a single Polygon, plot the exterior boundary
#         x, y = polygon.exterior.xy
#         ax.plot(x, y, color='black')
#     elif isinstance(polygon, MultiPolygon):
#         # For a MultiPolygon, iterate through each polygon in the collection
#         for poly in polygon.geoms:
#             x, y = poly.exterior.xy
#             ax.plot(x, y, color='black')
    
#     # Set aspect ratio and title
#     ax.set_aspect('equal')
#     ax.set_title(f"Polygon Plot from {file_path}")
    
#     # Display the plot
#     plt.show()



def smooth_coordinates(x, y, smoothing_factor=0.01):
    # Prepare data for spline interpolation
    tck, u = splprep([x, y], s=smoothing_factor)
    # Evaluate spline to get smooth coordinates
    x_smooth, y_smooth = splev(np.linspace(0, 1, len(x) * 2), tck)
    return x_smooth, y_smooth

def plot_polygon_from_json(file_path, smoothing_factor=0.01):
    # Load polygon data from the JSON file
    with open(file_path, 'r') as f:
        geojson_data = json.load(f)
    
    # Convert GeoJSON data to a Shapely shape
    polygon = shape(geojson_data)
    
    # Initialize a plot
    fig, ax = plt.subplots()
    
    # Plot depending on whether it's a Polygon or MultiPolygon
    if isinstance(polygon, Polygon):
        # Extract exterior coordinates
        x, y = polygon.exterior.xy
        # Smooth coordinates
        x_smooth, y_smooth = smooth_coordinates(x, y, smoothing_factor)
        ax.plot(x_smooth, y_smooth, color='black')
    elif isinstance(polygon, MultiPolygon):
        # For a MultiPolygon, iterate through each polygon in the collection
        for poly in polygon.geoms:
            x, y = poly.exterior.xy
            x_smooth, y_smooth = smooth_coordinates(x, y, smoothing_factor)
            ax.plot(x_smooth, y_smooth, color='black')
    
    # Set aspect ratio and title
    ax.set_aspect('equal')
    ax.set_title(f"Smoothed Polygon Plot from {file_path}")
    
    # Display the plot
    plt.show()

# Example usage
selection = ["Ohio", "Tennessee", "California", "Texas", "West Virginia", "Wisconsin", "Wyoming"]
selection.extend(["Alabama", "Alaska", "Arizona", "Arkansas", "Colorado", "Connecticut", "Delaware"])
selection.extend(["Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana"])
selection.extend(["Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts"])
selection.extend(["Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska"])
selection.extend(["Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "Oregon"])
selection.extend(["North Carolina", "North Dakota", "Oklahoma", "Pennsylvania", "Rhode Island"])
selection.extend(["South Carolina", "South Dakota", "Utah", "Vermont", "Virginia", "Washington"])

selected_state = random.choice(selection)
file_path = f'data/raw/state_polygons/{selected_state}.json'
plot_polygon_from_json(file_path, smoothing_factor=0.05)
