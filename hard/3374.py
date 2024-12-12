"""3374. First Letter Capitalization II"""

import pandas as pd


def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    user_content["converted_text"] = user_content["content_text"].apply(
        transform_sentence
    )

    user_content.rename(columns={"content_text": "original_text"}, inplace=True)

    return user_content


def transform_word(word):
    if "-" in word:
        return "-".join(part.title() for part in word.split("-"))

    return word.title()


def transform_sentence(sentence):
    if "-" not in sentence:
        return sentence.title()

    return " ".join(transform_word(word) for word in sentence.split())
