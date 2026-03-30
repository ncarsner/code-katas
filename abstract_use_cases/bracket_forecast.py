from itertools import product
from typing import Dict, List, Tuple, Optional

from prettytable import PrettyTable

SP=40

# Configuration: Teams still alive by region
# Bracket structure: East plays South in Semifinal 1, West plays Midwest in Semifinal 2
final_four = {
    "East": ["UConn"],
    "South": ["Illinois"],
    "West": ["Arizona"],
    "Midwest": ["Michigan"]
}

# Bracket structure definition
BRACKET_STRUCTURE = {
    "semifinal_1": ["East", "South"],
    "semifinal_2": ["West", "Midwest"]
}

# Each participant's Final Four picks (may include eliminated teams)
participant_pool = {
    "Jenny": ["Duke", "Houston", "Arizona", "Michigan"],
    "Rebecca": ["Kansas", "Vanderbilt", "Villanova", "Alabama"],
    "Nick": ["Kansas", "Vanderbilt", "Arizona", "Michigan"],
    "Chris #1": ["Duke", "Florida", "Arizona", "Virginia"],
    "Chris #2": ["Kansa", "Houston", "Arizona", "Michigan"],
    "John": ["Duke", "Illinois", "Purdue", "Michigan"],
    "Mallory": ["Duke", "North Carolina", "High Point", "Kentucky"],
    "Val #1": ["UConn", "Houston", "Arizona", "Michigan"],
    "Val #2": ["Duke", "North Carolina", "Arizona", "Michigan"],
    "Val #3": ["UConn", "Houston", "Arizona", "Michigan"],
    "Val #4": ["Duke", "Illinois", "Arizona", "Michigan"],
    "Arielle": ["UConn", "Houston", "Purdue", "Iowa State"],
    "Laura": ["Duke", "Clemson", "Gonzaga", "Akron"],
    "Christine": ["Duke", "North Carolina", "Purdue", "Akron"],
    "Scott": ["Duke", "Illinois", "Arizona", "Iowa State"],
    "Amanda": ["UCLA", "Vanderbilt", "Missouri", "Kentucky"],
    "Natalie": ["Duke", "Florida", "Arizona", "Michigan"],
    "Bojan": ["UConn", "Illinois", "Arizona", "Virginia"],
    "Joe": ["Duke", "Illinois", "Arizona", "Michigan"],
    "Austin": ["Duke", "Houston", "Arizona", "Michigan"],
    "Justin": ["Michigan State", "Houston", "Purdue", "Michigan"],
    "Krista": ["Duke", "Houston", "Arizona", "Tennessee"],
    "Melinda": ["Kansas", "Florida", "Gonzaga", "Michigan"],
    "Jake": ["Duke", "Illinois", "Arizona", "Michigan"],
    "Michelle": ["Duke", "Florida", "Arizona", "Michigan"],
    "Alan": ["Duke", "Illinois", "Purdue", "Michigan"],
    "Elizabeth": ["Duke", "Florida", "Arizona", "Michigan"],
    "Nicholas #1": ["UConn", "Vanderbilt", "Arizona", "Michigan"],
    "Nicholas #2": ["Duke", "Florida", "Gonzaga", "Michigan"],
    "Nicholas #3": ["UConn", "Illinois", "Arkansas", "Iowa State"],
}

participant_finals_and_championship_picks = {
    "Jenny": ["Duke", "Arizona", "Arizona"],
    "Rebecca": ["Kansas", "Villanova", "Kansas"],
    "Nick": ["Vanderbilt", "Michigan", "Michigan"],
    "Chris #1": ["Duke", "Arizona", "Arizona"],
    "Chris #2": ["Houston", "Arizona", "Houston"],
    "John": ["Duke", "Michigan", "Michigan"],
    "Mallory": ["North Carolina", "Kentucky", "Kentucky"],
    "Val #1": ["UConn", "Michigan", "UConn"],
    "Val #2": ["Duke", "Michigan", "Duke"],
    "Val #3": ["Houston", "Arizona", "Houston"],
    "Val #4": ["Duke", "Arizona", "Duke"],
    "Arielle": ["UConn", "Purdue", "UConn"],
    "Laura": ["Duke", "Gonzaga", "Duke"],
    "Christine": ["Duke", "Purdue", "Duke"],
    "Scott": ["Duke", "Arizona", "Arizona"],
    "Amanda": ["Vanderbilt", "Missouri", "Vanderbilt"],
    "Natalie": ["Duke", "Michigan", "Duke"],
    "Bojan": ["UConn", "Arizona", "Arizona"],
    "Joe": ["Duke", "Arizona", "Duke"],
    "Austin": ["Duke", "Michigan", "Duke"],
    "Justin": ["Houston", "Michigan", "Houston"],
    "Krista": ["Duke", "Tennessee", "Tennessee"],
    "Melinda": ["Kansas", "Michigan", "Kansas"],
    "Jake": ["Duke", "Arizona", "Arizona"],
    "Michelle": ["Duke", "Arizona", "Arizona"],
    "Alan": ["Duke", "Michigan", "Michigan"],
    "Elizabeth": ["Florida", "Michigan", "Florida"],
    "Nicholas #1": ["UConn", "Arizona", "Arizona"],
    "Nicholas #2": ["Duke", "Gonzaga", "Gonzaga"],
    "Nicholas #3": ["Illinois", "Arkansas", "Illinois"],
}

# Current point tallies
participant_scores = {
    "Jenny": 80,
    "Rebecca": 28,
    "Nick": 67,
    "Chris #1": 72,
    "Chris #2": 79,
    "John": 84,
    "Mallory": 50,
    "Val #1": 89,
    "Val #2": 71,
    "Val #3": 89,
    "Val #4": 89,
    "Arielle": 76,
    "Laura": 31,
    "Christine": 56,
    "Scott": 80,
    "Amanda": 24,
    "Natalie": 70,
    "Bojan": 80,
    "Joe": 89,
    "Austin": 76,
    "Justin": 67,
    "Krista": 68,
    "Melinda": 63,
    "Jake": 88,
    "Michelle": 75,
    "Alan": 77,
    "Elizabeth": 79,
    "Nicholas #1": 94,
    "Nicholas #2": 60,
    "Nicholas #3": 80,
}

# Point values for each round
points_by_round = {
    "Round of 64": 1,
    "Round of 32": 2,
    "Sweet 16": 4,
    "Elite 8": 8,
    "Final Four": 16,
    "Championship": 32
}


def get_all_possible_teams(final_four: Dict[str, List[str]]) -> List[str]:
    """Get a flat list of all teams still alive in the tournament."""
    teams = []
    for region_teams in final_four.values():
        teams.extend(region_teams)
    return teams


def generate_final_four_outcomes(final_four: Dict[str, List[str]]) -> List[Dict[str, str]]:
    """
    Generate all possible Final Four combinations.
    Each region must send one team to the Final Four.
    Returns list of dicts mapping region to team.
    """
    regions = list(final_four.keys())
    region_teams = [final_four[region] for region in regions]
    
    # Generate all combinations (one team from each region)
    combinations = list(product(*region_teams))
    
    # Convert to structured format
    outcomes = []
    for combo in combinations:
        outcome = {region: team for region, team in zip(regions, combo)}
        outcomes.append(outcome)
    
    return outcomes


def generate_bracket_outcomes(
    regional_winners: Dict[str, str],
    bracket_structure: Dict[str, List[str]]
) -> List[Tuple[Tuple[str, str], str, Tuple[str, str], str, str]]:
    """
    Generate all valid bracket outcomes respecting semifinal structure.
    
    Args:
        regional_winners: Dict mapping region to winning team
        bracket_structure: Dict defining which regions play in each semifinal
    
    Returns:
        List of tuples: (semifinal_1_matchup, sf1_winner, semifinal_2_matchup, sf2_winner, champion)
    """
    outcomes = []
    
    # Get teams in each semifinal
    sf1_regions = bracket_structure["semifinal_1"]
    sf2_regions = bracket_structure["semifinal_2"]
    
    sf1_team1 = regional_winners[sf1_regions[0]]
    sf1_team2 = regional_winners[sf1_regions[1]]
    
    sf2_team1 = regional_winners[sf2_regions[0]]
    sf2_team2 = regional_winners[sf2_regions[1]]
    
    # Semifinal 1 outcomes (East vs South)
    for sf1_winner in [sf1_team1, sf1_team2]:
        # Semifinal 2 outcomes (West vs Midwest)
        for sf2_winner in [sf2_team1, sf2_team2]:
            # Championship outcomes
            for champion in [sf1_winner, sf2_winner]:
                outcomes.append((
                    (sf1_team1, sf1_team2),  # Semifinal 1 matchup
                    sf1_winner,               # Semifinal 1 winner
                    (sf2_team1, sf2_team2),  # Semifinal 2 matchup
                    sf2_winner,               # Semifinal 2 winner
                    champion                  # Champion
                ))
    
    return outcomes


def calculate_points_for_outcome(
    participant_ff_picks: List[str],
    participant_finals_champ_picks: Optional[List[str]],
    final_four_teams: List[str],
    finalists: Optional[Tuple[str, str]] = None,
    champion: Optional[str] = None,
    include_final_four: bool = True,
    include_finals: bool = True,
    include_championship: bool = True
) -> int:
    """
    Calculate points earned for a specific outcome.
    
    Args:
        participant_ff_picks: The participant's Final Four picks (4 teams)
        participant_finals_champ_picks: [finalist1, finalist2, champion] picks
        final_four_teams: Teams that made the Final Four in this scenario
        finalists: Tuple of (team1, team2) in championship game
        champion: The champion in this scenario
        include_final_four: Whether to include Final Four points
        include_finals: Whether to include Finals matchup points
        include_championship: Whether to include Championship points
    """
    points = 0
    
    # Points for Final Four appearances (16 points each)
    if include_final_four:
        for pick in participant_ff_picks:
            if pick in final_four_teams:
                points += points_by_round["Final Four"]
    
    # Points for correctly picking both finalists (16 points each)
    if include_finals and finalists and participant_finals_champ_picks:
        finalist_picks = set(participant_finals_champ_picks[:2])  # First 2 are finalist picks
        actual_finalists = set(finalists)
        
        # Award points for each correct finalist prediction
        for pick in finalist_picks:
            if pick in actual_finalists:
                points += points_by_round["Final Four"]  # Same as Final Four points
    
    # Points for championship winner (32 points)
    if include_championship and champion and participant_finals_champ_picks:
        champion_pick = participant_finals_champ_picks[2]  # Third element is champion pick
        if champion_pick == champion:
            points += points_by_round["Championship"]
    
    return points


def get_top_n_with_ties(ranked: List[Tuple[str, int]], top_n: int) -> List[Tuple[str, int]]:
    """
    Get top N participants, including all participants tied at each position.
    
    Args:
        ranked: List of (participant, score) tuples sorted by score descending
        top_n: Number of distinct rank positions to show
    
    Returns:
        List including all participants tied at the top N positions
    """
    if not ranked or top_n <= 0:
        return []
    
    result = []
    current_rank = 0
    i = 0
    
    while i < len(ranked) and current_rank < top_n:
        current_score = ranked[i][1]
        
        # Add all participants with the current score (handling ties)
        while i < len(ranked) and ranked[i][1] == current_score:
            result.append(ranked[i])
            i += 1
        
        current_rank += 1
    
    return result


def forecast_final_four_only(
    final_four: Dict[str, List[str]],
    participant_pool: Dict[str, List[str]],
    participant_finals_champ_picks: Dict[str, List[str]],
    current_scores: Dict[str, int],
    top_n: int = 3
) -> List[Dict]:
    """
    Forecast all possible outcomes for the Final Four round only.
    Returns a list of scenarios with top n participants.
    """
    scenarios = []
    final_four_combos = generate_final_four_outcomes(final_four)
    
    for combo_dict in final_four_combos:
        # Convert dict to list of teams for scoring
        ff_teams = list(combo_dict.values())
        scenario_scores = {}
        
        for participant, ff_picks in participant_pool.items():
            current = current_scores.get(participant, 0)
            finals_champ_picks = participant_finals_champ_picks.get(participant)
            earned = calculate_points_for_outcome(
                ff_picks, finals_champ_picks, ff_teams, None, None,
                include_final_four=True, 
                include_finals=False,
                include_championship=False
            )
            scenario_scores[participant] = current + earned
        
        # Sort by score descending
        ranked = sorted(scenario_scores.items(), key=lambda x: x[1], reverse=True)
        
        scenarios.append({
            "final_four": combo_dict,
            "final_four_teams": ff_teams,
            "semifinal_1": None,
            "semifinal_2": None,
            "finalists": None,
            "champion": None,
            "top_participants": get_top_n_with_ties(ranked, top_n),
            "all_scores": scenario_scores
        })
    
    return scenarios


def forecast_full_bracket(
    final_four: Dict[str, List[str]],
    participant_pool: Dict[str, List[str]],
    participant_finals_champ_picks: Dict[str, List[str]],
    bracket_structure: Dict[str, List[str]],
    current_scores: Dict[str, int],
    top_n: int = 3
) -> List[Dict]:
    """
    Forecast all possible outcomes through the championship, respecting bracket structure.
    Returns a list of scenarios with top n participants.
    """
    scenarios = []
    final_four_combos = generate_final_four_outcomes(final_four)
    
    for ff_combo_dict in final_four_combos:
        # Generate valid bracket outcomes respecting semifinal structure
        bracket_outcomes = generate_bracket_outcomes(ff_combo_dict, bracket_structure)
        
        for (sf1_matchup, sf1_winner, sf2_matchup, sf2_winner, champion) in bracket_outcomes:
            # Get all Final Four teams as a list for scoring
            ff_teams = list(ff_combo_dict.values())
            finalists = (sf1_winner, sf2_winner)
            
            scenario_scores = {}
            
            for participant, ff_picks in participant_pool.items():
                current = current_scores.get(participant, 0)
                finals_champ_picks = participant_finals_champ_picks.get(participant)
                earned = calculate_points_for_outcome(
                    ff_picks, finals_champ_picks, ff_teams,
                    finalists, champion,
                    include_final_four=True,
                    include_finals=True,
                    include_championship=True
                )
                scenario_scores[participant] = current + earned
            
            # Sort by score descending
            ranked = sorted(scenario_scores.items(), key=lambda x: x[1], reverse=True)
            
            scenarios.append({
                "final_four": ff_combo_dict,
                "final_four_teams": ff_teams,
                "semifinal_1": {"matchup": sf1_matchup, "winner": sf1_winner},
                "semifinal_2": {"matchup": sf2_matchup, "winner": sf2_winner},
                "championship_game": finalists,
                "champion": champion,
                "top_participants": get_top_n_with_ties(ranked, top_n),
                "all_scores": scenario_scores
            })
    
    return scenarios


def generate_championship_outcomes(final_four_teams: List[str]) -> List[Tuple[str, str, str]]:
    """
    Generate all possible championship outcomes from 4 Final Four teams.
    
    Args:
        final_four_teams: List of 4 teams in the Final Four
    
    Returns:
        List of tuples: (finalist1, finalist2, champion)
    """
    outcomes = []
    teams = final_four_teams
    
    # All possible pairs of teams as finalists
    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            finalist1 = teams[i]
            finalist2 = teams[j]
            
            # Each finalist can win the championship
            for champion in [finalist1, finalist2]:
                outcomes.append((finalist1, finalist2, champion))
    
    return outcomes


def forecast_championship_only(
    final_four_teams: List[str],
    participant_pool: Dict[str, List[str]],
    participant_finals_champ_picks: Dict[str, List[str]],
    current_scores: Dict[str, int],
    top_n: int = 3
) -> List[Dict]:
    """
    Forecast outcomes for championship round only (assuming Final Four is set).
    
    Args:
        final_four_teams: List of exactly 4 teams in the Final Four
        participant_pool: Participant Final Four picks
        participant_finals_champ_picks: Participant finals and championship picks
        current_scores: Current scores including Final Four results
        top_n: Number of top participants to show
    """
    scenarios = []
    championship_outcomes = generate_championship_outcomes(final_four_teams)
    
    for finalist1, finalist2, champion in championship_outcomes:
        scenario_scores = {}
        
        for participant, ff_picks in participant_pool.items():
            current = current_scores.get(participant, 0)
            finals_champ_picks = participant_finals_champ_picks.get(participant)
            # Calculate finals and championship points only
            earned = calculate_points_for_outcome(
                ff_picks, finals_champ_picks, final_four_teams,
                (finalist1, finalist2), champion,
                include_final_four=False,
                include_finals=True,
                include_championship=True
            )
            scenario_scores[participant] = current + earned
        
        # Sort by score descending
        ranked = sorted(scenario_scores.items(), key=lambda x: x[1], reverse=True)
        
        scenarios.append({
            "final_four": final_four_teams,
            "championship_game": (finalist1, finalist2),
            "champion": champion,
            "top_participants": get_top_n_with_ties(ranked, top_n),
            "all_scores": scenario_scores
        })
    
    return scenarios


def print_scenario(scenario: Dict, scenario_num: int):
    """Pretty print a single scenario using PrettyTable."""
    print(f"\n{'='*SP}")
    print(f"Scenario {scenario_num}")
    print(f"{'='*SP}")
    
    # Handle both dict and list formats for final_four
    if isinstance(scenario['final_four'], dict):
        ff_display = ', '.join(f"{region}: {team}" for region, team in scenario['final_four'].items())
        # print(f"Final Four: {ff_display}")
    else:
        print(f"Final Four: {', '.join(scenario['final_four'])}")
    
    # Show semifinals if available
    if scenario.get('semifinal_1'):
        sf1 = scenario['semifinal_1']
        t1, t2 = sf1['matchup']
        # print(f"Semifinal 1 (East vs South): {t1} vs {t2} → Winner: {sf1['winner']}")
        # print(f"Semifinal 1: {t1} vs {t2} → Winner: {sf1['winner']}")
        print(f"Semifinal 1: {t1} vs {t2}")
    
    if scenario.get('semifinal_2'):
        sf2 = scenario['semifinal_2']
        t1, t2 = sf2['matchup']
        # print(f"Semifinal 2 (West vs Midwest): {t1} vs {t2} → Winner: {sf2['winner']}")
        # print(f"Semifinal 2: {t1} vs {t2} → Winner: {sf2['winner']}")
        print(f"Semifinal 2: {t1} vs {t2}")
    
    if scenario.get('championship_game'):
        f1, f2 = scenario['championship_game']
        print(f"Finals: {f1} vs {f2}")
    
    if scenario.get('champion'):
        print(f"Champion: {scenario['champion']}")
    
    # Create table for top participants with tie handling
    table = PrettyTable()
    table.field_names = ["Rank", "Participant(s)", "Points"]
    table.align["Participant(s)"] = "l"
    table.align["Points"] = "r"
    
    # Group participants by score to handle ties
    current_rank = 1
    i = 0
    while i < len(scenario['top_participants']):
        current_score = scenario['top_participants'][i][1]
        tied_participants = []
        
        # Collect all participants with the same score
        while i < len(scenario['top_participants']) and scenario['top_participants'][i][1] == current_score:
            tied_participants.append(scenario['top_participants'][i][0])
            i += 1
        
        # Format rank label
        if len(tied_participants) > 1:
            rank_label = f"{current_rank} (tied)"
        else:
            rank_label = str(current_rank)
        
        # Join participant names
        participants_str = ', '.join(tied_participants)
        
        table.add_row([rank_label, participants_str, current_score])
        current_rank += len(tied_participants)
    
    print("\nTop Participants:")
    print(table)


def print_summary(scenarios: List[Dict]):
    """Print summary statistics across all scenarios using PrettyTable."""
    print(f"\n{'='*SP}")
    print("SUMMARY STATISTICS")
    print(f"{'='*SP}")
    print(f"Total possible scenarios: {len(scenarios)}")
    
    # Track which scenarios each participant finishes in each place (1st, 2nd, 3rd)
    place_scenarios = {1: {}, 2: {}, 3: {}}
    
    for idx, scenario in enumerate(scenarios):
        top_participants = scenario['top_participants']
        
        # Track participants by their finishing position (accounting for ties)
        current_place = 1
        i = 0
        
        while i < len(top_participants) and current_place <= 3:
            current_score = top_participants[i][1]
            tied_participants = []
            
            # Collect all participants with the same score
            while i < len(top_participants) and top_participants[i][1] == current_score:
                tied_participants.append(top_participants[i][0])
                i += 1
            
            # Record this finish for all tied participants at this place
            for participant in tied_participants:
                if participant not in place_scenarios[current_place]:
                    place_scenarios[current_place][participant] = set()
                place_scenarios[current_place][participant].add(idx)
            
            current_place += len(tied_participants)
    
    # Create tables for each place
    for place in [1, 2, 3]:
        if not place_scenarios[place]:
            continue
            
        place_names = {1: "1st Place", 2: "2nd Place", 3: "3rd Place"}
        
        # Group participants who finish in the same scenarios at this place
        scenario_sets = {}
        for participant, scenarios_finished in place_scenarios[place].items():
            frozen_set = frozenset(scenarios_finished)
            if frozen_set not in scenario_sets:
                scenario_sets[frozen_set] = []
            scenario_sets[frozen_set].append(participant)
        
        # Create table
        table = PrettyTable()
        table.title = f"{place_names[place]} Finishes"
        table.field_names = ["Participant(s)", "Scenarios", "Chance"]
        table.align["Participant(s)"] = "l"
        table.align["Scenarios"] = "r"
        table.align["Chance"] = "r"
        
        # Sort by number of scenarios (descending)
        sorted_groups = sorted(scenario_sets.items(), key=lambda x: len(x[0]), reverse=True)
        
        for scenario_set, participants in sorted_groups:
            count = len(scenario_set)
            percentage = (count / len(scenarios)) * 100
            
            # Only group participants if there's more than one (truly tied)
            if len(participants) > 1:
                participants_str = ', '.join(sorted(participants))
            else:
                participants_str = participants[0]
            
            table.add_row([participants_str, count, f"{percentage:.1f}%"])
        
        print(f"\n{table}")
    
    # Add visual bar chart for top candidates
    print(f"\n{'='*SP}")
    print("TOP CANDIDATES - FINISH DISTRIBUTION")
    print(f"{'='*SP}")
    
    # ANSI color codes
    GOLD = '\033[93m'      # Yellow/Gold for 1st
    SILVER = '\033[97m'    # Bright White/Silver for 2nd
    BRONZE = '\033[91m'    # Red/Bronze for 3rd
    RESET = '\033[0m'
    
    # Get all participants who finish in top 3 at least once
    all_candidates = set()
    for place in [1, 2, 3]:
        all_candidates.update(place_scenarios[place].keys())
    
    # Calculate counts for each candidate at each place
    candidate_stats = {}
    for candidate in all_candidates:
        counts = {}
        for place in [1, 2, 3]:
            if candidate in place_scenarios[place]:
                counts[place] = len(place_scenarios[place][candidate])
            else:
                counts[place] = 0
        candidate_stats[candidate] = counts
    
    # Sort candidates by 1st place count, then 2nd, then 3rd (descending)
    sorted_candidates = sorted(candidate_stats.items(), 
                              key=lambda x: (x[1][1], x[1][2], x[1][3]), 
                              reverse=True)
    
    # Find longest name for alignment
    max_name_len = max(len(name) for name in all_candidates) if all_candidates else 0
    bar_width = 40  # Fixed width for all bars representing 100%
    
    print()
    for candidate, counts in sorted_candidates:
        # Calculate total top-3 finishes for this candidate
        total_finishes = counts[1] + counts[2] + counts[3]
        
        if total_finishes == 0:
            continue
        
        # Calculate proportions based on their top-3 finishes (not total scenarios)
        prop_1st = counts[1] / total_finishes if total_finishes > 0 else 0
        prop_2nd = counts[2] / total_finishes if total_finishes > 0 else 0
        prop_3rd = counts[3] / total_finishes if total_finishes > 0 else 0
        
        # Divide bar into 3 equal zones for 1st/2nd/3rd
        zone_width = bar_width // 3
        remainder = bar_width % 3
        
        # Allocate remainder to zones with actual finishes
        zone_1st_width = zone_width + (1 if remainder > 0 and counts[1] > 0 else 0)
        zone_2nd_width = zone_width + (1 if remainder > 1 and counts[2] > 0 else (1 if remainder > 0 and counts[1] == 0 and counts[2] > 0 else 0))
        zone_3rd_width = bar_width - zone_1st_width - zone_2nd_width
        
        # Calculate filled portions within each zone
        fill_1st = int(prop_1st * zone_1st_width) if counts[1] > 0 else 0
        fill_2nd = int(prop_2nd * zone_2nd_width) if counts[2] > 0 else 0
        fill_3rd = int(prop_3rd * zone_3rd_width) if counts[3] > 0 else 0
        
        # Build the bar with three zones
        bar_visual = ""
        
        # Zone 1: 1st place
        if fill_1st > 0:
            bar_visual += f"{GOLD}{'█' * fill_1st}{RESET}"
            bar_visual += ' ' * (zone_1st_width - fill_1st)
        else:
            bar_visual += ' ' * zone_1st_width
        
        # Zone 2: 2nd place  
        if fill_2nd > 0:
            bar_visual += f"{SILVER}{'█' * fill_2nd}{RESET}"
            bar_visual += ' ' * (zone_2nd_width - fill_2nd)
        else:
            bar_visual += ' ' * zone_2nd_width
        
        # Zone 3: 3rd place
        if fill_3rd > 0:
            bar_visual += f"{BRONZE}{'█' * fill_3rd}{RESET}"
            bar_visual += ' ' * (zone_3rd_width - fill_3rd)
        else:
            bar_visual += ' ' * zone_3rd_width
        
        # Format counts
        parts = []
        if counts[1] > 0:
            parts.append(f"{GOLD}1st:{RESET}{counts[1]}")
        if counts[2] > 0:
            parts.append(f"{SILVER}2nd:{RESET}{counts[2]}")
        if counts[3] > 0:
            parts.append(f"{BRONZE}3rd:{RESET}{counts[3]}")
        
        stats_str = " ".join(parts)
        
        # Format output
        name_padded = candidate.ljust(max_name_len)
        print(f"{name_padded} │ {bar_visual} │ {stats_str}")
    
    print()


def main():
    """Main execution function demonstrating the forecaster."""
    # print("BRACKET FORECASTER")
    # print("=" * 80)
    n = 8
    
    # Current standings table
    print("\nCurrent Standings:")
    standings_table = PrettyTable()
    standings_table.field_names = ["Rank", "Participant", "Points"]
    standings_table.align["Participant"] = "l"
    standings_table.align["Points"] = "r"
    
    for rank, (participant, score) in enumerate(sorted(participant_scores.items(), 
                                                        key=lambda x: x[1], reverse=True), 1):
        standings_table.add_row([rank, participant, score])
    
    print(standings_table)
    
    # Teams still alive table
    print("\nTeams Still Alive:")
    teams_table = PrettyTable()
    teams_table.field_names = ["Region", "Teams"]
    teams_table.align["Region"] = "l"
    teams_table.align["Teams"] = "l"
    
    for region, teams in final_four.items():
        teams_table.add_row([region, ', '.join(teams)])
    
    print(teams_table)
    
    print("\nBracket Structure:")
    sf1_regions = BRACKET_STRUCTURE["semifinal_1"]
    sf2_regions = BRACKET_STRUCTURE["semifinal_2"]
    print(f"  Semifinal 1: {sf1_regions[0]} winner vs {sf1_regions[1]} winner")
    print(f"  Semifinal 2: {sf2_regions[0]} winner vs {sf2_regions[1]} winner")
    print("  Finals: Winner of SF1 vs Winner of SF2")
    
    # Sample participant picks table
    print("\nSample Participant Picks:")
    picks_table = PrettyTable()
    picks_table.field_names = ["Participant", "Final Four", "Finals", "Champion"]
    picks_table.align["Participant"] = "l"
    picks_table.align["Final Four"] = "l"
    picks_table.align["Finals"] = "l"
    picks_table.align["Champion"] = "l"
    picks_table.max_width["Final Four"] = 30
    
    for participant in list(participant_pool.keys())[:5]:  # Show first 5
        ff_picks = participant_pool[participant]
        fc_picks = participant_finals_and_championship_picks.get(participant, [])
        
        ff_str = ', '.join(ff_picks)
        finals_str = f"{fc_picks[0]} vs {fc_picks[1]}" if fc_picks else "N/A"
        champ_str = fc_picks[2] if fc_picks else "N/A"
        
        picks_table.add_row([participant, ff_str, finals_str, champ_str])
    
    print(picks_table)
    print(f"... and {len(participant_pool) - 5} more participants")
    
    # Example 1: Forecast Final Four only
    print("\n" + "="*SP)
    print("FORECASTING: FINAL FOUR OUTCOMES ONLY")
    print("="*SP)
    ff_scenarios = forecast_final_four_only(
        final_four, participant_pool, 
        participant_finals_and_championship_picks,
        participant_scores, top_n=3
    )
    
    for i, scenario in enumerate(ff_scenarios[:n], 1):  # Show first n
        print_scenario(scenario, i)
    
    if len(ff_scenarios) > n:
        print(f"\n... and {len(ff_scenarios) - n} more scenarios")
    
    print_summary(ff_scenarios)
    
    # Example 2: Forecast full bracket (Final Four + Championship)
    print("\n\n" + "="*SP)
    print("FORECASTING: FULL BRACKET (RESPECTING SEMIFINAL STRUCTURE)")
    print("="*SP)
    full_scenarios = forecast_full_bracket(
        final_four, participant_pool,
        participant_finals_and_championship_picks,
        BRACKET_STRUCTURE,
        participant_scores, top_n=3
    )
    
    print(f"\nTotal scenarios generated: {len(full_scenarios)}")
    # print("(Note: Fewer scenarios than before due to bracket structure constraints)")
    
    for i, scenario in enumerate(full_scenarios[:n], 1):  # Show first n
        print_scenario(scenario, i)
    
    if len(full_scenarios) > n:
        print(f"\n... and {len(full_scenarios) - n} more scenarios")
    
    print_summary(full_scenarios)


if __name__ == "__main__":
    main()