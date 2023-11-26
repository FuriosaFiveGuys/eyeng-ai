from ppe import ppe
from get_prompt import get_prompt

def get_corrected_sentence(sentence):
    prompt = get_prompt(sentence)
    response = ppe(prompt)
    return response