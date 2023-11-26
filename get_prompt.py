def get_prompt(sentence):
    prompt = "Act as enlish teacher\n" \
    f"Please correct the English sentence according to English grammar\n" \
    f"sentence : {sentence}\n" \
    f"corrected sentence : \n" \
    f"Just correct the spacing.\n" \
    f"Please send me the original text without modifying or adding the same special symbols.\n"
    f"Please don't change capital letters."
    return prompt