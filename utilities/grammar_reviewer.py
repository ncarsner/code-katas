import re
from collections import defaultdict


class GrammarReviewer:
    def __init__(self):
        self.replacements = {
            "allocate": ["assign", "allot", "distribute", "apportion"],
            "allotment": ["allocation", "portion", "quota", "share", "stake", "interest", "percentage", "part"],
            "area": ["domain", "field", "realm", "territory", "sphere", "scope", "zone", "region", "section", "division"],
            "improve": ["better", "eclipse", "surpass", "top", "outdo"],
            "cadence": ["rhythm", "beat", "pulse", "tempo", "time", "meter", "pace"],
            "conduit": ["channel", "medium", "vehicle", "pipeline", "path", "line"],
            "conserve": ["preserve", "protect", "safeguard", "save", "maintain", "store", "sustain", "reserve"],
            "desire": ["drive", "hunger", "aspiration", "resolve", "will"],
            "effort": ["attempt", "endeavor", "struggle", "undertaking", "work"],
            "enhance": ["develop", "improve", "upgrade", "augment", "elevate", "enrich", "further", "refine"],
            "evaluate": ["assess", "appraise", "rate", "review", "analyze", "examine", "inspect", "scrutinize"],
            "general": ["universal", "common", "collective", "global", "overall", "broad", "inclusive"],
            "generic": ["common", "collective", "universal", "standard", "typical", "conventional", "umbrella", "catchall", "blanket"],
            "get": ["obtain", "acquire", "secure", "procure", "gain", "attain", "earn", "win", "achieve", "accomplish", "gather", "collect", "elicit", "capture"],
            "intend": ["plan", "mean", "aim", "propose", "design", "purport", "expect", "anticipate"],
            "isolate": ["separate", "insulate", "sequester", "cloister", "seclude", "silo"],
            "label": ["brand", "identify", "name", "denote", "characterize", "call", "dub"],
            "means": ["method", "way", "mode", "manner", "system", "mechanism", "vehicle", "instrument", "tool", "medium"],
            "regard": ["respect", "heed", "follow", "mind", "observe"],
            "sequence": ["order", "succession", "series", "chain", "line", "string", "concatenation", "train"],
            "skilled": ["proficient", "experienced", "qualified", "trained", "capable", "competent", "adept", "accomplished"],
            "specific": ["particular", "detailed", "precise", "explicit", "definite", "clear-cut", "distinct", "individual"],
            "use": ["utilize", "employ", "apply", "operate", "work with", "handle", "manipulate"],
            "useful": ["helpful", "beneficial", "valuable", "advantageous", "effective", "practical"],
            "useless": ["worthless", "futile", "pointless", "futile", "ineffective", "unproductive"],
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
                print(f"For '{word}', consider:")
                print("0: Keep original")
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
    text = input("Enter text to review: ")
    suggestions = reviewer.review_text(text)
    revised_text = reviewer.display_suggestions(text, suggestions)
    print(f"\nOriginal text: {text}")
    print(f"Revised text: {revised_text}")
