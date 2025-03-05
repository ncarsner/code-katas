import random


def generate_random_event(
    week, opponent, home_away, quarter, drive, team_score, opponent_score
):
    field_position = random.choice(["OWN", "OPP", "50"])
    down = random.randint(1, 4)
    distance = random.randint(1, 10)
    pass_attempts = 1
    completions = random.randint(0, 1)
    passing_yards = completions * random.randint(0, 30)
    touchdowns = completions * random.randint(0, 1)
    interceptions = 0 if completions == 1 else random.randint(0, 1)

    return {
        "week": week,
        "opponent": opponent,
        "home_away": home_away,
        "quarter": quarter,
        "drive": drive,
        "field_position": field_position,
        "down": down,
        "distance": distance,
        "team_score": team_score,
        "opponent_score": opponent_score,
        "pass_attempts": pass_attempts,
        "completions": completions,
        "passing_yards": passing_yards,
        "touchdowns": touchdowns,
        "interceptions": interceptions,
    }


qb_passing_events = []
week = 1
opponent = "NYG"
home_away = "home"
team_score = 0
opponent_score = 0
drive = 1

for quarter in range(1, 5):
    for _ in range(6):  # Simulate 6 drives per quarter
        event = generate_random_event(
            week, opponent, home_away, quarter, drive, team_score, opponent_score
        )
        qb_passing_events.append(event)
        team_score += event["touchdowns"] * 7
        opponent_score += random.choice([0, 3, 7])  # Randomly update opponent score
        drive += 1

# Define the data object for quarterback's passing events over a simulated game
qb_passing_events = [
    {
        "week": 1,
        "opponent": "NYG",
        "home_away": "home",
        "quarter": 1,
        "drive": 1,
        "field_position": "OPP 45",
        "down": 1,
        "distance": 10,
        "team_score": 0,
        "opponent_score": 0,
        "pass_attempts": 1,
        "completions": 1,
        "passing_yards": 15,
        "touchdowns": 0,
        "interceptions": 0,
    },
    {
        "week": 1,
        "opponent": "NYG",
        "home_away": "home",
        "quarter": 1,
        "drive": 1,
        "field_position": "OPP 30",
        "down": 2,
        "distance": 5,
        "team_score": 0,
        "opponent_score": 0,
        "pass_attempts": 1,
        "completions": 1,
        "passing_yards": 10,
        "touchdowns": 0,
        "interceptions": 0,
    },
    {
        "week": 1,
        "opponent": "NYG",
        "home_away": "home",
        "quarter": 1,
        "drive": 2,
        "field_position": "OWN 20",
        "down": 1,
        "distance": 10,
        "team_score": 7,
        "opponent_score": 0,
        "pass_attempts": 1,
        "completions": 0,
        "passing_yards": 0,
        "touchdowns": 0,
        "interceptions": 0,
    },
    {
        "week": 1,
        "opponent": "NYG",
        "home_away": "home",
        "quarter": 2,
        "drive": 3,
        "field_position": "OPP 35",
        "down": 3,
        "distance": 8,
        "team_score": 7,
        "opponent_score": 3,
        "pass_attempts": 1,
        "completions": 1,
        "passing_yards": 20,
        "touchdowns": 0,
        "interceptions": 0,
    },
    {
        "week": 1,
        "opponent": "NYG",
        "home_away": "home",
        "quarter": 2,
        "drive": 4,
        "field_position": "50",
        "down": 1,
        "distance": 10,
        "team_score": 14,
        "opponent_score": 3,
        "pass_attempts": 1,
        "completions": 1,
        "passing_yards": 30,
        "touchdowns": 1,
        "interceptions": 0,
    },
    {
        "week": 1,
        "opponent": "NYG",
        "home_away": "home",
        "quarter": 3,
        "drive": 5,
        "field_position": "OWN 40",
        "down": 2,
        "distance": 5,
        "team_score": 21,
        "opponent_score": 10,
        "pass_attempts": 1,
        "completions": 1,
        "passing_yards": 15,
        "touchdowns": 0,
        "interceptions": 0,
    },
    {
        "week": 1,
        "opponent": "NYG",
        "home_away": "home",
        "quarter": 4,
        "drive": 6,
        "field_position": "OPP 25",
        "down": 3,
        "distance": 7,
        "team_score": 21,
        "opponent_score": 17,
        "pass_attempts": 1,
        "completions": 0,
        "passing_yards": 0,
        "touchdowns": 0,
        "interceptions": 1,
    },
    {
        "week": 1,
        "opponent": "NYG",
        "home_away": "home",
        "quarter": 4,
        "drive": 7,
        "field_position": "OWN 10",
        "down": 1,
        "distance": 10,
        "team_score": 21,
        "opponent_score": 24,
        "pass_attempts": 1,
        "completions": 1,
        "passing_yards": 10,
        "touchdowns": 1,
        "interceptions": 0,
    },
    # Additional events to reach 30 pass attempts
    {
        "week": 1,
        "opponent": "NYG",
        "home_away": "home",
        "quarter": 1,
        "drive": 1,
        "field_position": "OPP 45",
        "down": 1,
        "distance": 10,
        "team_score": 0,
        "opponent_score": 0,
        "pass_attempts": 1,
        "completions": 1,
        "passing_yards": 15,
        "touchdowns": 0,
        "interceptions": 0,
    },
    {
        "week": 1,
        "opponent": "NYG",
        "home_away": "home",
        "quarter": 1,
        "drive": 1,
        "field_position": "OPP 30",
        "down": 2,
        "distance": 5,
        "team_score": 0,
        "opponent_score": 0,
        "pass_attempts": 1,
        "completions": 1,
        "passing_yards": 10,
        "touchdowns": 0,
        "interceptions": 0,
    },
    {
        "week": 1,
        "opponent": "NYG",
        "home_away": "home",
        "quarter": 1,
        "drive": 2,
        "field_position": "OWN 20",
        "down": 1,
        "distance": 10,
        "team_score": 7,
        "opponent_score": 0,
        "pass_attempts": 1,
        "completions": 0,
        "passing_yards": 0,
        "touchdowns": 0,
        "interceptions": 0,
    },
    {
        "week": 1,
        "opponent": "NYG",
        "home_away": "home",
        "quarter": 2,
        "drive": 3,
        "field_position": "OPP 35",
        "down": 3,
        "distance": 8,
        "team_score": 7,
        "opponent_score": 3,
        "pass_attempts": 1,
        "completions": 1,
        "passing_yards": 20,
        "touchdowns": 0,
        "interceptions": 0,
    },
    {
        "week": 1,
        "opponent": "NYG",
        "home_away": "home",
        "quarter": 2,
        "drive": 4,
        "field_position": "50",
        "down": 1,
        "distance": 10,
        "team_score": 14,
        "opponent_score": 3,
        "pass_attempts": 1,
        "completions": 1,
        "passing_yards": 30,
        "touchdowns": 1,
        "interceptions": 0,
    },
    {
        "week": 1,
        "opponent": "NYG",
        "home_away": "home",
        "quarter": 3,
        "drive": 5,
        "field_position": "OWN 40",
        "down": 2,
        "distance": 5,
        "team_score": 21,
        "opponent_score": 10,
        "pass_attempts": 1,
        "completions": 1,
        "passing_yards": 15,
        "touchdowns": 0,
        "interceptions": 0,
    },
    {
        "week": 1,
        "opponent": "NYG",
        "home_away": "home",
        "quarter": 4,
        "drive": 6,
        "field_position": "OPP 25",
        "down": 3,
        "distance": 7,
        "team_score": 21,
        "opponent_score": 17,
        "pass_attempts": 1,
        "completions": 0,
        "passing_yards": 0,
        "touchdowns": 0,
        "interceptions": 1,
    },
    {
        "week": 1,
        "opponent": "NYG",
        "home_away": "home",
        "quarter": 4,
        "drive": 7,
        "field_position": "OWN 10",
        "down": 1,
        "distance": 10,
        "team_score": 21,
        "opponent_score": 24,
        "pass_attempts": 1,
        "completions": 1,
        "passing_yards": 10,
        "touchdowns": 1,
        "interceptions": 0,
    },
    {
        "week": 1,
        "opponent": "NYG",
        "home_away": "home",
        "quarter": 1,
        "drive": 1,
        "field_position": "OPP 45",
        "down": 1,
        "distance": 10,
        "team_score": 0,
        "opponent_score": 0,
        "pass_attempts": 1,
        "completions": 1,
        "passing_yards": 15,
        "touchdowns": 0,
        "interceptions": 0,
    },
    {
        "week": 1,
        "opponent": "NYG",
        "home_away": "home",
        "quarter": 1,
        "drive": 1,
        "field_position": "OPP 30",
        "down": 2,
        "distance": 5,
        "team_score": 0,
        "opponent_score": 0,
        "pass_attempts": 1,
        "completions": 1,
        "passing_yards": 10,
        "touchdowns": 0,
        "interceptions": 0,
    },
    {
        "week": 1,
        "opponent": "NYG",
        "home_away": "home",
        "quarter": 1,
        "drive": 2,
        "field_position": "OWN 20",
        "down": 1,
        "distance": 10,
        "team_score": 7,
        "opponent_score": 0,
        "pass_attempts": 1,
        "completions": 0,
        "passing_yards": 0,
        "touchdowns": 0,
        "interceptions": 0,
    },
    {
        "week": 1,
        "opponent": "NYG",
        "home_away": "home",
        "quarter": 2,
        "drive": 3,
        "field_position": "OPP 35",
        "down": 3,
        "distance": 8,
        "team_score": 7,
        "opponent_score": 3,
        "pass_attempts": 1,
        "completions": 1,
        "passing_yards": 20,
        "touchdowns": 0,
        "interceptions": 0,
    },
    {
        "week": 1,
        "opponent": "NYG",
        "home_away": "home",
        "quarter": 2,
        "drive": 4,
        "field_position": "50",
        "down": 1,
        "distance": 10,
        "team_score": 14,
        "opponent_score": 3,
        "pass_attempts": 1,
        "completions": 1,
        "passing_yards": 30,
        "touchdowns": 1,
        "interceptions": 0,
    },
    {
        "week": 1,
        "opponent": "NYG",
        "home_away": "home",
        "quarter": 3,
        "drive": 5,
        "field_position": "OWN 40",
        "down": 2,
        "distance": 5,
        "team_score": 21,
        "opponent_score": 10,
        "pass_attempts": 1,
        "completions": 1,
        "passing_yards": 15,
        "touchdowns": 0,
        "interceptions": 0,
    },
    {
        "week": 1,
        "opponent": "NYG",
        "home_away": "home",
        "quarter": 4,
        "drive": 6,
        "field_position": "OPP 25",
        "down": 3,
        "distance": 7,
        "team_score": 21,
        "opponent_score": 17,
        "pass_attempts": 1,
        "completions": 0,
        "passing_yards": 0,
        "touchdowns": 0,
        "interceptions": 1,
    },
    {
        "week": 1,
        "opponent": "NYG",
        "home_away": "home",
        "quarter": 4,
        "drive": 7,
        "field_position": "OWN 10",
        "down": 1,
        "distance": 10,
        "team_score": 21,
        "opponent_score": 24,
        "pass_attempts": 1,
        "completions": 1,
        "passing_yards": 10,
        "touchdowns": 1,
        "interceptions": 0,
    },
]


# Example function to calculate passer rating (simplified version)
def calculate_passer_rating(events):
    completions = sum(event["completions"] for event in events)
    attempts = sum(event["pass_attempts"] for event in events)
    yards = sum(event["passing_yards"] for event in events)
    touchdowns = sum(event["touchdowns"] for event in events)
    interceptions = sum(event["interceptions"] for event in events)

    if attempts == 0:
        return 0

    a = ((completions / attempts) - 0.3) * 5
    b = ((yards / attempts) - 3) * 0.25
    c = (touchdowns / attempts) * 20
    d = 2.375 - ((interceptions / attempts) * 25)

    passer_rating = ((a + b + c + d) / 6) * 100
    return max(0, min(passer_rating, 158.3))


def filter_by_down(events, down):
    return [event for event in events if event["down"] == down]


def filter_by_distance(events, distance):
    return [event for event in events if event["distance"] == distance]


def filter_by_field_position(events, position):
    if position == "OWN":
        return [event for event in events if event["field_position"].startswith("OWN")]
    elif position == "OPP":
        return [event for event in events if event["field_position"].startswith("OPP")]
    elif position == "50":
        return [event for event in events if event["field_position"] == "50"]
    else:
        return []


def filter_by_game_scenario(events, scenario):
    if scenario == "ahead":
        return [
            event for event in events if event["team_score"] > event["opponent_score"]
        ]
    elif scenario == "behind":
        return [
            event for event in events if event["team_score"] < event["opponent_score"]
        ]
    elif scenario == "tied":
        return [
            event for event in events if event["team_score"] == event["opponent_score"]
        ]
    else:
        return []


# Example usage
down_events = {down: filter_by_down(qb_passing_events, down) for down in range(1, 5)}
down_passer_ratings = {
    down: calculate_passer_rating(events) for down, events in down_events.items()
}
for down, rating in down_passer_ratings.items():
    print(f"Passer Rating for down {down}: {rating:.1f}")
print()

unique_distances = set(event["distance"] for event in qb_passing_events)
distance_events = {
    distance: filter_by_distance(qb_passing_events, distance)
    for distance in unique_distances
}

unique_field_positions = set(event["field_position"][:3] for event in qb_passing_events)
field_position_events = {
    position: filter_by_field_position(qb_passing_events, position)
    for position in unique_field_positions
}
field_position_passer_ratings = {
    position: calculate_passer_rating(events)
    for position, events in field_position_events.items()
}

for position, rating in field_position_passer_ratings.items():
    print(f"Passer Rating for field position {position}: {rating:.1f}")
print()

scenarios = ["ahead", "tied", "behind"]
scenario_events = {
    scenario: filter_by_game_scenario(qb_passing_events, scenario)
    for scenario in scenarios
}
scenario_passer_ratings = {
    scenario: calculate_passer_rating(events)
    for scenario, events in scenario_events.items()
}
for scenario in scenarios:
    rating = scenario_passer_ratings[scenario]
    print(f"Passer Rating when {scenario}: {rating:.1f}")
print()

# Calculate passer rating for each quarter
quarter_events = {
    quarter: [event for event in qb_passing_events if event["quarter"] == quarter]
    for quarter in range(1, 5)
}
quarter_passer_ratings = {
    quarter: calculate_passer_rating(events)
    for quarter, events in quarter_events.items()
}
for quarter, rating in quarter_passer_ratings.items():
    print(f"Passer Rating for Q{quarter}: {rating:.1f}")
print()

# Calculate passer rating for the simulated game
passer_rating = calculate_passer_rating(qb_passing_events)
print(f"Passer Rating for game: {passer_rating:.1f}")
