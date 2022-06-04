import markovify
import random
import MeCab
import re

with open('./txt/source.txt', 'r', encoding='utf-8') as f:
    _text = f.read().strip()

text =''

for __text in _text:
    __text = re.sub(r'[（）「」『』｛｝【】＠”’！？｜～・]', '', __text)
    __text = re.sub(r'[()\[\]{}@\'\"!?|~-]', '', __text)
    __text = re.sub(r'\u3000', '', __text)
    __text = re.sub(r' ', '', __text)
    __text = re.sub(r'\n', '', __text)

    __text = re.sub(r'。', '。\n', __text)

    text += __text

# print(text)
parsed_text = MeCab.Tagger('-Owakati').parse(text)
# print(parsed_text)

parsed_text = re.sub(r'。', '。\n', parsed_text)
# print(parsed_text)

text_model = markovify.NewlineText(parsed_text, state_size=2, well_formed=False)

rnd = random.randint(1,3)

for i in range(rnd):
    sentence = text_model.make_short_sentence(140, 30, tries=100)
    print(sentence.replace(' ', ''))