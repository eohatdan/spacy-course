import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "i downloaded Fortnite on my laptop and can't open the game at all. Help? "
    "so when I was downloading Minecraft, I got the Windows version where it "
    "is the '.zip' folder and I used the default program to unpack it... do "
    "I also need to download Winzip?"
)

# 写一个模板来匹配"download"的一种形式加一个代词
pattern = [{"LEMMA": ____}, {"POS": ____}]

# 把模板加入到matcher中，然后把matcher应用到doc上面
matcher.add("DOWNLOAD_THINGS_PATTERN", None, pattern)
matches = matcher(doc)
print("Total matches found:", len(matches))

# 遍历所有的匹配，打印span的文本
for match_id, start, end in matches:
    print("Match found:", doc[start:end].text)
