import re
from collections import defaultdict


class GrammarReviewer:
    def __init__(self):
        self.replacements = {
            "access": ["entry", "admittance"],
            "accessible": ["available", "reachable", "obtainable", "attainable", "open", "admissible"],
            "allocate": ["assign", "allot", "distribute", "apportion"],
            "allotment": ["allocation", "portion", "quota", "share", "stake", "interest", "percentage", "part"],
            "anticipate": ["expect", "foresee", "predict", "forecast", "envision"],
            "area": ["domain", "field", "realm", "territory", "sphere", "scope", "zone", "region", "section", "division"],
            "asset": ["resource", "property", "investment", "equity"],
            "basic": ["fundamental", "elementary", "primary", "rudimentary", "core", "central"],
            "big": ["large", "huge", "giant", "massive", "immense", "enormous", "tremendous", "mammoth", "oversized"],
            "cadence": ["rhythm", "beat", "pulse", "tempo", "time", "meter", "pace"],
            "cluster": ["bunch", "collection", "set", "array", "assortment"],
            "coincide": ["coexist", "overlap"],
            "conduit": ["channel", "medium", "pipeline", "path"],
            "connection": ["link", "association", "relationship"],
            "conserve": ["preserve", "protect", "safeguard", "save", "maintain", "store", "sustain", "reserve"],
            "consume": ["expend", "spend", "deplete", "exhaust", "absorb", "devour", "ingest"],
            "cost": ["price", "expense", "expenditure"],
            "create": ["generate", "produce", "invent", "construct", "build", "form", "forge", "fabricate", "manufacture", "compose"],
            "decisive": ["conclusive", "definitive", "clear-cut", "deciding"],
            "delicate": ["fragile", "frail", "faint", "breakable", "brittle", "vulnerable", "sensitive", "tender", "dainty", "mild", "soft"],
            "desire": ["drive", "hunger", "resolve", "will"],
            "demonstration": ["display", "exhibition", "presentation", "expression"],
            "disagree": ["differ", "conflict", "contradict", "oppose", "dispute"],
            "divulge": ["reveal", "disclose", "expose", "uncover", "unveil", "declare", "acknowledge", "make known"],
            "effort": ["attempt", "endeavor", "struggle", "undertaking", "work"],
            "enhance": ["develop", "upgrade", "augment", "elevate", "enrich", "further", "refine"],
            "estimate": ["calculate", "approximate", "gauge", "measure", "quantify", "value"],
            "evaluate": ["assess", "appraise", "rate", "review", "analyze", "examine", "inspect", "scrutinize"],
            "general": ["collective", "global", "overall", "broad", "inclusive"],
            "generic": ["common", "universal", "standard", "typical", "conventional", "umbrella", "catchall", "blanket"],
            "get": ["obtain", "acquire", "secure", "procure", "gain", "attain", "earn", "win", "achieve", "accomplish", "gather", "collect", "elicit", "capture"],
            "improve": ["better", "eclipse", "surpass", "top", "outdo"],
            "identify": ["recognize", "distinguish", "discern", "pinpoint", "diagnose", "detect", "differentiate"],
            "impartial": ["unbiased", "neutral"],
            "indication": ["flag", "giveaway", "sign", "signal", "mark", "symptom", "evidence", "proof", "hint", "clue", "suggestion"],
            "individual": ["person", "character", "party", "entity"],
            "influence": ["impact", "affect", "sway", "control", "pressure", "manipulate", "shape", "determine", "persuade"],
            "intend": ["plan", "mean", "aim", "propose", "purport"],
            "isolate": ["separate", "insulate", "sequester", "cloister", "seclude", "silo"],
            "label": ["brand", "name", "characterize", "call", "dub"],
            "means": ["method", "way", "mode", "manner", "mechanism", "instrument", "tool"],
            "objective": ["goal", "target", "purpose", "intent", "ambition", "aspiration"],
            "penalty": ["punishment", "fine", "fee", "charge"],
            "organization": ["institution", "agency", "group", "body"],
            "regard": ["respect", "heed", "follow", "mind", "observe"],
            "require": ["demand", "necessitate", "compel", "obligate", "enforce", "dictate", "constrain", "press", "impose"],
            "required": ["necessary", "needed", "requisite", "essential", "compulsory", "mandatory", "prerequisite"],
            "sequence": ["order", "succession", "series", "chain", "line", "string", "concatenation", "train"],
            "signify": ["indicate", "denote", "represent", "suggest", "imply"],
            "skilled": ["proficient", "experienced", "qualified", "trained", "capable", "competent", "adept", "accomplished"],
            "soon": ["shortly", "quickly", "promptly", "swiftly", "rapidly", "immediately", "presently", "before long"],
            "specific": ["particular", "detailed", "precise", "explicit", "definite", "distinct", "exact", "concrete", "unambiguous"],
            "structure": ["framework", "system", "composition", "construction", "format", "layout", "design"],
            "substantial": ["worthwhile", "weighty", "noteworthy"],
            "symbol": ["emblem", "token", "representation", "badge", "insignia", "crest"],
            "template": ["pattern", "model", "guide", "blueprint", "prototype", "example"],
            "transfer": ["move", "shift", "relocate", "transport", "convey", "carry", "send", "pass"],
            "unique": ["distinctive", "special", "exclusive", "singular", "uncommon", "unusual", "rare", "incomparable", "unparalleled"],
            "use": ["utilize", "employ", "apply", "operate"],
            "useful": ["helpful", "beneficial", "valuable", "advantageous", "effective", "practical"],
            "useless": ["worthless", "pointless", "futile", "ineffective", "unproductive"],
            "variation": ["deviation", "fluctuation", "alteration", "modification"],
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
