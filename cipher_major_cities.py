import pprint


def is_prime(n):
    if n <= 1:
        return False
    for y in range(2, int(n / 2) + 1):
        if n % y == 0:
            return False
    return True


def calculate_sum_and_check_prime(a, b, c):
    sum_values = abs(a) + abs(b) + abs(c)
    return sum_values, is_prime(sum_values)


def calculate_product_and_check_prime(a, b, c):
    product_values = abs(a * b * c)
    return product_values, is_prime(product_values)


cities = { # Latitude, Longitude, UTC Offset
    "Brisbane": [-27, 153, 10],
    "New Delhi": [28, 77, 5.5],
    "Detroit": [42, -83, -5],
    "Honolulu": [21, -157, -10],
    "Brussels": [50, 4, 1],
    "Capetown": [-33, 18, 2],
    "Tokyo": [35, 139, 9],
    "Paris": [48, 2, 1],
    "New York": [40, -74, -5],
    "Los Angeles": [34, -118, -8],
    "Sydney": [-33, 151, 10],
    "Moscow": [55, 37, 3],
    "Cairo": [30, 31, 2],
    "Rio de Janeiro": [-22, -43, -3],
    "London": [51, 0, 0],
    "Beijing": [39, 116, 8],
    "Singapore": [1, 103, 8],
    "Mexico City": [19, -99, -6],
    "Buenos Aires": [-34, -58, -3],
    "Istanbul": [41, 29, 3],
    "Bangkok": [13, 100, 7],
    "Dubai": [25, 55, 4],
    "Toronto": [43, -79, -5],
    "Berlin": [52, 13, 1],
    "Madrid": [40, -3, 1],
    "Rome": [41, 12, 1],
    "Jakarta": [-6, 106, 7],
    "Seoul": [37, 126, 9],
    "Hong Kong": [22, 114, 8],
    "Lagos": [6, 3, 1],
    "Chicago": [41, -87, -6],
    "Lima": [-12, -77, -5],
    "Manila": [14, 121, 8],
    "Athens": [37, 23, 2],
    "Karachi": [24, 67, 5],
    "Lahore": [31, 74, 5],
    "Tehran": [35, 51, 3.5],
    "Kuala Lumpur": [3, 101, 8],
    "Riyadh": [24, 46, 3],
    "Baghdad": [33, 44, 3],
    "Santiago": [-33, -70, -4],
    "Bogota": [4, -74, -5],
    "Nairobi": [-1, 36, 3],
    "Algiers": [36, 3, 1],
    "Dhaka": [23, 90, 6],
    "Accra": [5, 0, 0],
    "Kinshasa": [-4, 15, 1],
    "Casablanca": [33, -7, 0],
    "Vienna": [48, 16, 1],
    "Addis Ababa": [9, 38, 3],
}

for city, values in cities.items():
    lat, lon, offset = values
    sum_values, sum_is_prime = calculate_sum_and_check_prime(lat, lon, offset)
    product_values, product_is_prime = calculate_product_and_check_prime(
        lat, lon, offset
    )

    values.append(sum_is_prime)
    values.append(product_is_prime)

pprint.pprint(cities)
