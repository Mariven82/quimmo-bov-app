
import streamlit as st
from docxtpl import DocxTemplate
from io import BytesIO

st.set_page_config(page_title="BOV Quimmo", layout="centered")

st.title("Generatore di Broker Opinion (BOV) - Quimmo")

with st.form("bov_form"):
    indirizzo = st.text_input("Indirizzo immobile")
    superficie = st.number_input("Superficie (mq)", min_value=1)
    categoria = st.text_input("Categoria")
    stato = st.selectbox("Stato immobile", ["Ottimo", "Buono", "Da ristrutturare", "Altro"])
    descrizione = st.text_area("Descrizione immobile")
    submitted = st.form_submit_button("Genera BOV")

if submitted:
    # Carica il template
    tpl = DocxTemplate("bov_template.docx")

    # Dati da inserire nel template
    context = {
        "indirizzo": indirizzo,
        "superficie": superficie,
        "altezza": "n.d.",
        "categoria": categoria,
        "classe_energetica": "n.d.",
        "descrizione": descrizione,
        "comparabili": [],
        "valore_totale_min": 0,
        "valore_totale_medio": 0,
        "valore_totale_max": 0,
        "ntn_anni": [2019, 2020, 2021, 2022, 2023],
        "ntn_res": [920, 903, 1171, 1125, 1021],
        "ntn_comm": [1503, 1764, 1967, 1909, 1838],
        "criticita": {
            "contesto": "zona periferica",
            "stato": "n.d.",
            "mercato": "Domanda rivolta a immobili con caratteristiche differenti dal subject"
        }
    }

    tpl.render(context)
    output = BytesIO()
    tpl.save(output)
    output.seek(0)

    st.success("BOV generata con successo!")
    st.download_button("📄 Scarica BOV in formato Word", data=output, file_name="BOV_Quimmo.docx")
