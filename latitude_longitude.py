import json

state_coordinates = { # State: [latitude, longitude]
    'AL': [32.31823, -86.902298],
    'AK': [66.160507, -153.369141],
    'AZ': [34.048927, -111.093735],
    'AR': [34.799999, -92.199997],
    'CA': [36.778259, -119.417931],
    'CO': [39.113014, -105.358887],
    'CT': [41.599998, -72.699997],
    'DE': [39, -75.5],
    'FL': [27.994402, -81.760254],
    'GA': [33.247875, -83.441162],
    'HI': [19.741755, -155.844437],
    'ID': [44.068203, -114.742043],
    'IL': [40, -89],
    'IN': [40.273502, -86.126976],
    'IA': [42.032974, -93.581543],
    'KS': [38.5, -98],
    'KY': [37.839333, -84.27002],
    'LA': [30.39183, -92.329102],
    'ME': [45.367584, -68.972168],
    'MD': [39.045753, -76.641273],
    'MA': [42.407211, -71.382439],
    'MI': [44.182205, -84.506836],
    'MN': [46.39241, -94.63623],
    'MS': [33, -90],
    'MO': [38.573936, -92.60376],
    'MT': [46.96526, -109.533691],
    'NE': [41.5, -100],
    'NV': [39.876019, -117.224121],
    'NH': [44, -71.5],
    'NJ': [39.833851, -74.871826],
    'NM': [34.307144, -106.018066],
    'NY': [43, -75],
    'NC': [35.782169, -80.793457],
    'ND': [47.650589, -100.437012],
    'OH': [40.367474, -82.996216],
    'OK': [36.084621, -96.921387],
    'OR': [44, -120.5],
    'PA': [41.203323, -77.194527],
    'RI': [41.742325, -71.742332],
    'SC': [33.836082, -81.163727],
    'SD': [44.5, -100],
    'TN': [35.860119, -86.660156],
    'TX': [31, -100],
    'UT': [39.41922, -111.950684],
    'VT': [44, -72.699997],
    'VA': [37.926868, -78.024902],
    'WA': [47.751076, -120.740135],
    'WV': [39, -80.5],
    'WI': [44.5, -89.5],
    'WY': [43.07597, -107.290283],
}

select_states = [
    'WA', 'OR', 'CA', 'NV',
    'MT', 'CO', 'MN', 'KS',
    'IL', 'MI', 'OH', 'NY',
    'MD', 'NJ', 'VT', 'CT',
    'MA', 'ME',
]

selected_coordinates = {state: state_coordinates[state] for state in select_states}
sorted_coordinates = dict(sorted(selected_coordinates.items(), key=lambda item: item[1][1]))

print(json.dumps(sorted_coordinates, indent=4))

sorted_list = list(sorted_coordinates)
print(sorted_list)