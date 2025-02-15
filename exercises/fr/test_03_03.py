def test():
    assert nlp.meta["name"] == "core_web_sm", "Charges-tu le bon modèle ?"
    assert "print(nlp.pipe_names)" in __solution__, "As-tu affiché les noms des composants ?"
    assert "print(nlp.pipeline)" in __solution__, "Affiches-tu le pipeline ?"

    __msg__.good(
        "Bien joué ! Chaque fois que tu as un doute à propos du pipeline "
        "courant, tu peux l'inspecter en affichant nlp.pipe_names ou "
        "nlp.pipeline."
    )
