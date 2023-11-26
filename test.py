# # -*- coding: utf-8 -*-
# from get_prompt import get_prompt
# from ppe import ppe
# from sentence_acc import sentence_acc

# def get_corrected_sentence(sentence):
#     prompt = get_prompt(sentence)
#     response = ppe(prompt)
#     return response

# sentence = """Difficulties arise when we do not think of people and machines as collaborative systems, but assign whatever tasks can be automated to the machines and leave the rest to people. This ends up requiring people to behavein machine-like fashion, in ways that differfrom human capabilities. We expect people to monitor machines, which means keeping alert for long periods, Something we are bad at We require people to do repeated operations with the extreme precision and accuracy required by machines, again something we are not good at. When we divide up the machine and human components ofataskin this way, we fail to take advantage of human strengths and capabilities but instead rely upon areas where we are genetically biologically unsuited. Yet, when people fail, they are blamed.
# difficulties of overcoming human weaknesses to avoid failure benefits of allowing machines and humans to work together issues of allocating unfit tasks tohumansin automated systems reasons why humans continue to pursue machine automation influences Of human actions ona machine's performance """

# original = """Difficulties arise when we do not think of people and machines as collaborative systems, but assign whatever tasks can be automated to the machines and leave the rest to people. This ends up requiring people to behave in machine-like fashion, in ways that differ from human capabilities. We expect people to monitor machines, which means keeping alert for long periods, something we are bad at. We require people to do repeated operations with the extreme precision and accuracy required by machines, again something we are not good at. When we divide up the machine and human components of a task in this way, we fail to take advantage of human strengths and capabilities but instead rely upon areas where we are genetically, biologically unsuited. Yet, when people fail, they are blamed. difficulties of overcoming human weaknesses to avoid failure benefits of allowing machines and humans to work together issues of allocating unfit tasks to humans in automated systems reasons why humans continue to pursue machine automation influences of human actions on a machine’s performance."""

# corrected_sen = get_corrected_sentence(sentence).split('Corrected Sentence: ')[-1]

# print(corrected_sen)

# print()

# print(sentence_acc(original, corrected_sen))

#import easyocr
from preprocess import preprocess

#reader = easyocr.Reader(['en'])
image = preprocess('english_19.png', 640, 640)
print(image)
#print(reader.readtext('english_19.png', detail = 0, paragraph=True, decoder='wordbeamsearch', beamWidth=7, workers=4)[0])