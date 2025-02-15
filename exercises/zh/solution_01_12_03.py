import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "Features of the app include a beautiful design, smart search, automatic "
    "labels and optional voice responses."
)

# 写一个模板是形容词加上一个或者两个名词
pattern = [{"POS": "ADJ"}, {"POS": "NOUN"}, {"POS": "NOUN", "OP": "?"}]

# 把模板加入到matcher中然后把marcher应用到doc上面
matcher.add("ADJ_NOUN_PATTERN", None, pattern)
matches = matcher(doc)
print("Total matches found:", len(matches))

# 遍历所有的匹配，打印span的文本
for match_id, start, end in matches:
    print("Match found:", doc[start:end].text)
