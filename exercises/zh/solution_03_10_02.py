from spacy.lang.en import English
from spacy.tokens import Span

nlp = English()

# 定义这个方法
def to_html(span, tag):
    # 将span文本包在HTML标签中并返回
    return f"<{tag}>{span.text}</{tag}>"


# 注册这个Span方法扩展名"to_html"及其方法to_html
Span.set_extension("to_html", method=to_html)

# 处理文本，在span上调用to_html方法及其标签名"strong"
doc = nlp("Hello world, this is a sentence.")
span = doc[0:2]
print(span._.to_html("strong"))
