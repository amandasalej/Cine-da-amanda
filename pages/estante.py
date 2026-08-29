import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore


if not firebase_admin._apps:
    cred_dict = dict(st.secrets["firebase"])
    if "private_key" in cred_dict:
        cred_dict["private_key"] = cred_dict["private_key"].replace("\\n", "\n")
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred)

db = firestore.client()


st.markdown("## 🔍 **A Minha Estante** 📚")
st.markdown("Aqui estão as suas leituras guardadas com muito carinho! ✨")



livros_ref = db.collection("livros").stream()


lista_livros = []
for doc in livros_ref:
    livro = doc.to_dict()
    lista_livros.append(livro)


if len(lista_livros) == 0:
    st.info("Sua estante ainda está vazia! 🥺 Vamos à aba de cadastro para adicionar o seu primeiro livro. 🌸")
else:

    total_lidos = len(lista_livros)
    meta = 40
    
    st.markdown(f"### 🎯 **Progresso da Meta:** {total_lidos} de {meta} livros lidos!")
   
    valor_progresso = total_lidos / meta
    if valor_progresso > 1.0:
        valor_progresso = 1.0
    st.progress(valor_progresso)
    st.markdown("---")

    st.dataframe(lista_livros, use_container_width=True)
