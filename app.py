
import streamlit as st

st.set_page_config(page_title="Generatore BOV Quimmo", page_icon=":office:", layout="centered")

st.title("Generatore di Broker Opinion (BOV) - Quimmo")
st.markdown("Inserisci i dati dell'immobile per generare la tua BOV in PDF")

with st.form("bov_form"):
    indirizzo = st.text_input("Indirizzo immobile")
    superficie = st.number_input("Superficie (mq)", min_value=1)
    categoria = st.selectbox("Categoria", ["Residenziale", "Commerciale", "Produttivo", "Altro"])
    stato = st.selectbox("Stato immobile", ["Ottimo", "Buono", "Da ristrutturare", "Altro"])
    note = st.text_area("Note aggiuntive")
    submitted = st.form_submit_button("Genera BOV")

if submitted:
    st.success("BOV generata con successo!")
    st.markdown("*(Qui va integrato il codice per generare e scaricare il PDF)*")
    st.download_button("Scarica BOV (PDF)", data="Demo PDF", file_name="BOV_Quimmo.pdf")
