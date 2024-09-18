sample_text = """
In a recent review by the National Institutes of Health (NIH), the consumption of BLT sandwiches at Minor League Baseball (MiLB) venues has garnered notable attention. The NIH's Dietary Guidelines for Americans (DGA) emphasize nutritional balance, and the prevalence of BLTs at these ballparks raises questions about sodium intake and lipid consumption. BLTs, characterized by bacon, lettuce, and tomato, offer a high sodium content and significant saturated fats, which the NIH suggests could impact cardiovascular health if consumed excessively.

In response, Major League Baseball (MLB) has taken a cautious stance. The MLB’s Fan Health and Safety Committee (FHSC) is examining the nutritional aspects of ballpark concessions to align with broader public health recommendations. The MLB, through its Healthy Ballpark Initiative (HBI), is encouraging MiLB teams to diversify their food offerings to include more low-sodium and low-fat options. This initiative aims to balance the traditional ballpark experience with contemporary health considerations, reflecting a growing trend towards nutritional awareness in sports venues.

Furthermore, the MLB's collaboration with the Centers for Disease Control and Prevention (CDC) underscores the league's commitment to promoting healthier eating habits. The CDC's Dietary Recommendations for Athletic Populations (DRAP) advocate for reduced sodium and increased vegetable intake, principles which the MLB is now integrating into its food service standards. By fostering a more health-conscious environment, MLB hopes to mitigate potential dietary risks associated with popular but nutritionally questionable foods like the BLT.

Overall, while the NIH highlights potential health concerns related to BLTs in MiLB parks, MLB’s proactive measures, guided by FHSC and CDC recommendations, reflect an evolving stance towards integrating health and nutrition with the traditional ballpark experience. This balanced approach aims to enhance the overall well-being of fans while preserving the essence of America’s pastime.
"""

import re


def process_acronyms(text):
    # Regular expression to find acronyms
    acronym_pattern = re.compile(r"\b([A-Z]{2,})\b")
    # Regular expression to find full forms followed by acronyms in parentheses
    full_form_pattern = re.compile(
        r"\b([A-Z][a-z]*(?:\s(?:[A-Z][a-z]*|[a-z]+))*)\s\(([A-Z]{2,})\)"
    )
    full_form_pattern = re.compile(
        r"\b([A-Z][a-z]*(?:\s(?:[A-Z][a-z]*|[a-z]+)){,5})\s\(([A-Z]{2,})\)"
    )

    # Store the first occurrence of each acronym and its full form status
    acronym_dict = {}
    # Store all discovered acronyms and their long-form definitions
    full_form_dict = {}
    # Set to store acronyms that need definitions
    acronyms_needing_definitions = set()

    # Split text into lines for easier processing
    lines = text.split("\n")
    for i, line in enumerate(lines):
        # Find full forms and acronyms
        full_form_matches = full_form_pattern.findall(line)
        for full_form, acronym in full_form_matches:
            full_form_dict[acronym] = full_form.strip()
            acronym_dict[acronym] = {"line": line, "has_full_form": True}

        # Find acronyms
        matches = acronym_pattern.findall(line)
        for match in matches:
            if match not in acronym_dict:
                # Store the first occurrence of the acronym and mark it as not having a full form yet
                acronym_dict[match] = {"line": line, "has_full_form": False}
            else:
                # Replace subsequent occurrences with the acronym
                lines[i] = lines[i].replace(match, match)

    # Identify acronyms that need definitions
    for acronym, info in acronym_dict.items():
        if not info["has_full_form"]:
            acronyms_needing_definitions.add(acronym)

    # Join the lines back into a single text
    modified_text = "\n".join(lines)

    return modified_text, full_form_dict, acronyms_needing_definitions


# Process the text
modified_text, full_form_dict, acronyms_needing_definitions = process_acronyms(
    sample_text
)

print("Modified Text:\n", modified_text)
print("\nAcronyms:\n", full_form_dict)
print("\nUndefined:\n", acronyms_needing_definitions)
