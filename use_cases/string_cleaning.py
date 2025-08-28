import re


def remove_end_spaces(text: str) -> str:
    return text.strip()


def remove_extra_spaces(text: str) -> str:
    return re.sub(r"\s{2,}", " ", text)


def keep_only_letters(text: str) -> str:
    cleaned_text = re.sub(r"[^a-zA-Z\s]", "", text)
    return cleaned_text


def remove_extra_letters(text: str) -> str:
    """Replace any character repeated more than twice with two of that character"""
    return re.sub(r"(.)\1{2,}", r"\1\1", text)


def censor_profanity(text: str) -> str:
    return text


def main(text):
    text = remove_end_spaces(text)
    text = keep_only_letters(text)
    text = remove_extra_spaces(text)
    text = remove_extra_letters(text)
    text = censor_profanity(text)
    print(text)


if __name__ == "__main__":
    text = " this is ###tooo ##much  ##  # esssence to c#lean##  up #   ## "
    main(text)
