
from docxtpl import DocxTemplate

immobile = {
    "indirizzo": "Via Esempio 123, Milano",
    "superficie": 120,
    "altezza": "3,00 m",
    "categoria": "Residenziale",
    "descrizione": "Appartamento ristrutturato in zona servita, dotato di balcone e cantina.",
    "classe_energetica": "B",
    "comparabili": [
        {"indirizzo": "Via A 1", "mq": 110, "prezzo": 330000},
        {"indirizzo": "Via B 2", "mq": 125, "prezzo": 370000},
    ],
    "valore_medio": 3000,
    "valore_totale_medio": 360000,
    "valore_totale_min": 330000,
    "valore_totale_max": 390000,
    "ntn_anni": [2019, 2020, 2021, 2022, 2023],
    "ntn_res": [920, 903, 1171, 1125, 1021],
    "ntn_comm": [1503, 1764, 1967, 1909, 1838],
    "criticita": {
        "contesto": "zona periferica",
        "stato": "n.d.",
        "mercato": "Domanda rivolta a immobili con caratteristiche differenti dal subject"
    }
}

doc = DocxTemplate("bov_template.docx")
doc.render(immobile)
doc.save("BOV_Generata.docx")
