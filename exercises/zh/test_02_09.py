def test():
    assert (
        'spacy.load("en_core_web_md")' in __solution__
    ), "你有正确读入中等规模的模型了吗？"
    assert "doc[1].vector" in __solution__, "你有得到正确的向量吗？"
    __msg__.good(
        "干得漂亮！下一个练习，我们会用spaCy来通过这些词向量计算document、span、和token"
        "之间的相似度。"
    )
