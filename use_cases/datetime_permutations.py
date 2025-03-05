import random
from datetime import datetime

# Function to generate variations of a given datetime format
def generate_variations(dt):
    # Extract the full datetime string as a concatenation of the components
    full_datetime = dt.strftime('%m%d%H%M')
    
    # Generate zero-padded and non-zero-padded versions
    parts = [full_datetime[i:i+2] for i in range(0, len(full_datetime), 2)]
    single_digit_parts = [part.lstrip('0') if part != '00' else part for part in parts]
    
    # Combine both versions to generate all possible variations
    variations_set = set()
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    variation = f"{parts[0] if i == 0 else single_digit_parts[0]}" \
                                f"{parts[1] if j == 0 else single_digit_parts[1]}" \
                                f"{parts[2] if k == 0 else single_digit_parts[2]}" \
                                f"{parts[3] if l == 0 else single_digit_parts[3]}"
                    variations_set.add(variation)
    
    return list(variations_set)

# Function to parse variations into 2-digit increments with a random punctuation
def parse_variations(variations):
    punctuation = random.choice(['-', '/', ':', '.'])
    parsed_variations = []
    
    for variation in variations:
        parsed_variation = punctuation.join([variation[i:i+2] for i in range(0, len(variation), 2)])
        parsed_variations.append(parsed_variation)
    
    return parsed_variations

# Example datetime
dt = datetime(2024, 6, 14, 15, 30)  # June 14, 2024, 15:30

# Generate variations
variations = generate_variations(dt)

# Parse variations
parsed_variations = parse_variations(variations)

# Print variations
for var in parsed_variations:
    print(var)

# # Optionally, save variations to a file
# with open('datetime_variations.txt', 'w') as f:
#     for var in parsed_variations:
#         f.write(var + '\n')
