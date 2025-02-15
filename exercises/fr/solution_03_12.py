import json
from spacy.lang.en import English
from spacy.tokens import Span
from spacy.matcher import PhraseMatcher

with open("exercises/en/countries.json") as f:
    COUNTRIES = json.loads(f.read())

with open("exercises/en/capitals.json") as f:
    CAPITALS = json.loads(f.read())

nlp = English()
matcher = PhraseMatcher(nlp.vocab)
matcher.add("COUNTRY", None, *list(nlp.pipe(COUNTRIES)))


def countries_component(doc):
    # Crée une entité Span avec le label "GPE" pour toutes les correspondances
    matches = matcher(doc)
    doc.ents = [Span(doc, start, end, label="GPE") for match_id, start, end in matches]
    return doc


# Ajoute le composant au pipeline
nlp.add_pipe(countries_component)
print(nlp.pipe_names)

# Getter qui recherche le texte du span dans le dictionnaire
# des capitales des pays
get_capital = lambda span: CAPITALS.get(span.text)

# Déclare l'extension d'attribut de Span "capital" avec le getter get_capital
Span.set_extension("capital", getter=get_capital)

# Traite le texte et affiche le texte de l'entité,
# ses attributs label et capitale
doc = nlp("Czech Republic may help Slovakia protect its airspace")
print([(ent.text, ent.label_, ent._.capital) for ent in doc.ents])
