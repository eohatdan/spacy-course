import json
from spacy.lang.en import English
from spacy.tokens import Doc

with open("exercises/en/bookquotes.json") as f:
    DATA = json.loads(f.read())

nlp = English()

# 注册Doc的扩展"author"（默认值为None）
Doc.set_extension("author", default=None)

# 注册Doc的扩展"book"（默认值为None）
Doc.set_extension("book", default=None)

for doc, context in nlp.pipe(DATA, as_tuples=True):
    # 从context中设置属性doc._.book和doc._.author
    doc._.book = context["book"]
    doc._.author = context["author"]

    # 打印文本和定制化的属性数据
    print(f"{doc.text}\n — '{doc._.book}' by {doc._.author}\n")
