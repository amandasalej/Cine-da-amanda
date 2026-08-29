import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

if not firebase_admin._apps:
    cred_dict = dict(st.secrets["firebase"])
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred)

db = firestore.client()

st.markdown("### 📝 **Cadastrar Nova Leitura**")
st.markdown("Preencha os detalhes abaixo para guardar mais um livro na sua estante. 💖")

with st.form("form_cadastro_livro"):
    titulo = st.text_input("Título do Livro 📖", placeholder="Ex: Os Sete Maridos de Evelyn Hugo")
    autor = st.text_input("Autor(a) ✍️", placeholder="Ex: Taylor Jenkins Reid")
    nota = st.number_input("Sua Nota (1 a 5) ⭐", min_value=1, max_value=5, step=1)
    data_termino = st.date_input("Quando terminou de ler? 📅", format="DD/MM/YYYY")
    cor_capa = st.color_picker("Qual a cor principal da capa? 🎨")
    
    btn_salvar = st.form_submit_button("Guardar na Estante 🎀")
    
    if btn_salvar:
        if not titulo:
            st.warning("Oh, esqueceu-se de preencher o título! 🥺")
        else:
            
            novo_livro = {
                "titulo": titulo,
                "autor": autor,
                "nota": nota,
                "data_termino": str(data_termino), 
        		"cor_capa": cor_capa
            }
            
            
            db.collection("livros").add(novo_livro)
            
            st.success(f"BOA! O livro **{titulo}** foi guardado no banco de dados com sucesso! 🎉")
            st.balloons()
