import re
from collections import defaultdict


class GrammarReviewer:
    def __init__(self):
        self.replacements = {
            "accessible": ["available", "reachable", "obtainable", "attainable", "open", "admissible"],
            "allocate": ["assign", "allot", "distribute", "apportion"],
            "allotment": ["allocation", "portion", "quota", "share", "stake", "interest", "percentage", "part"],
            "area": ["domain", "field", "realm", "territory", "sphere", "scope", "zone", "region", "section", "division"],
            "big": ["large", "huge", "giant", "massive", "immense", "enormous", "tremendous", "vast", "great", "sizeable", "colossal", "gigantic", "astronomical", "mammoth", "oversized"],
            "cadence": ["rhythm", "beat", "pulse", "tempo", "time", "meter", "pace"],
            "conduit": ["channel", "medium", "vehicle", "pipeline", "path", "line"],
            "conserve": ["preserve", "protect", "safeguard", "save", "maintain", "store", "sustain", "reserve"],
            "delicate": ["fragile", "frail", "faint", "breakable", "brittle", "vulnerable", "sensitive", "tender", "dainty", "mild", "soft"],
            "desire": ["drive", "hunger", "aspiration", "resolve", "will"],
            "demonstration": ["display", "exhibition", "presentation", "show", "manifestation", "expression", "indication", "proof", "evidence", "confirmation", "token"],
            "divulge": ["reveal", "disclose", "expose", "uncover", "unveil", "declare", "acknowledge", "make known"],
            "effort": ["attempt", "endeavor", "struggle", "undertaking", "work"],
            "enhance": ["develop", "improve", "upgrade", "augment", "elevate", "enrich", "further", "refine"],
            "evaluate": ["assess", "appraise", "rate", "review", "analyze", "examine", "inspect", "scrutinize"],
            "general": ["universal", "common", "collective", "global", "overall", "broad", "inclusive"],
            "generic": ["common", "collective", "universal", "standard", "typical", "conventional", "umbrella", "catchall", "blanket"],
            "get": ["obtain", "acquire", "secure", "procure", "gain", "attain", "earn", "win", "achieve", "accomplish", "gather", "collect", "elicit", "capture"],
            "improve": ["better", "eclipse", "surpass", "top", "outdo"],
            "indication": ["flag", "giveaway", "sign", "signal", "mark", "symptom", "evidence", "proof", "hint", "clue", "suggestion"],
            "individual": ["person", "character", "party", "entity"],
            "intend": ["plan", "mean", "aim", "propose", "design", "purport", "expect", "anticipate"],
            "isolate": ["separate", "insulate", "sequester", "cloister", "seclude", "silo"],
            "label": ["brand", "identify", "name", "denote", "characterize", "call", "dub"],
            "means": ["method", "way", "mode", "manner", "system", "mechanism", "vehicle", "instrument", "tool", "medium"],
            "regard": ["respect", "heed", "follow", "mind", "observe"],
            "require": ["demand", "necessitate", "compel", "obligate", "enforce", "dictate", "constrain", "press", "impose"],
            "required": ["necessary", "needed", "requisite", "essential", "compulsory", "mandatory", "obligatory", "prerequisite"],
            "sequence": ["order", "succession", "series", "chain", "line", "string", "concatenation", "train"],
            "skilled": ["proficient", "experienced", "qualified", "trained", "capable", "competent", "adept", "accomplished"],
            "soon": ["shortly", "quickly", "promptly", "swiftly", "rapidly", "immediately", "presently", "before long"],
            "specific": ["particular", "detailed", "precise", "explicit", "definite", "clear-cut", "distinct", "exact", "concrete", "unambiguous"],
            "structure": ["framework", "organization", "system", "composition", "construction", "format", "layout", "design", "pattern"],
            "substantial": ["significant", "considerable", "sizeable", "material", "meaningful", "important", "valuable", "worthwhile", "weighty", "noteworthy"],
            "template": ["pattern", "model", "guide", "blueprint", "prototype", "example", "standard", "format", "framework"],
            "use": ["utilize", "employ", "apply", "operate", "work with", "handle", "manipulate"],
            "useful": ["helpful", "beneficial", "valuable", "advantageous", "effective", "practical"],
            "useless": ["worthless", "pointless", "futile", "ineffective", "unproductive"],
        }

    def review_text(self, text):
        words = text.split()
        suggestions = defaultdict(list)

        for word in words:
            clean_word = re.sub(r"^\W+|\W+$", "", word).lower()
            for key, values in self.replacements.items():
                if clean_word == key:
                    suggestions[word] = [v for v in values if v != clean_word]
                    break
                elif clean_word in values:
                    suggestions[word] = [key] + [v for v in values if v != clean_word]
                    break

        return suggestions

    def display_suggestions(self, text, suggestions):
        words = text.split()
        for i, word in enumerate(words):
            if word in suggestions:
                options = suggestions[word]
                print(f"\nFor '{word}', consider:")
                print("0: NO CHANGE")
                for idx, option in enumerate(options, 1):
                    print(f"{idx}: {option}")
                choice = input("Choose an option: ")
                if choice.isdigit() and 0 <= int(choice) <= len(options):
                    if int(choice) != 0:
                        words[i] = options[int(choice) - 1]

        return " ".join(words)

    def add_replacement(self, word, replacements):
        self.replacements[word] = replacements


if __name__ == "__main__":
    reviewer = GrammarReviewer()
    file_path = "path/to/your/file.txt"
    
    try:
        with open(file_path, 'r') as file:
            text = file.read().strip()
    except FileNotFoundError:
        text = input("Enter text to review: ")
    
    suggestions = reviewer.review_text(text)
    revised_text = reviewer.display_suggestions(text, suggestions)
    print(f"\nOriginal text: {text}")
    print(f"Revised text: {revised_text}")
