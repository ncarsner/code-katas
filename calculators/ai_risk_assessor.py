from itertools import product

# Assign risk values
entity = {
    "Human": 4,
    "AI": 5,
    "Unknown": 2
}
intent = {
    "Intentional": 5,
    "Unintentional": 2,
    "Unknown": 3
}
timing = {
    "Pre-Deployment": 3,
    "Post-Deployment": 4,
    "Indeterminant": 2
}

# Calculate all combinations with severity score
combinations = []
for e, i, t in product(entity, intent, timing):
    # Calculate the severity score as the product of risk values
    severity_score = entity[e] * intent[i] * timing[t]
    combinations.append({
        "Entity": e,
        "Intent": i,
        "Timing": t,
        "Severity": severity_score
    })

# Sort combinations by severity score in descending order
sorted_combinations = sorted(combinations, key=lambda x: x["Severity"], reverse=True)

# Display sorted combinations with severity scores
for combo in sorted_combinations:
    print(f"{combo['Entity']} entity, {combo['Intent']} intent, {combo['Timing']} timing, Severity: {combo['Severity']}")
