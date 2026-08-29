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

st.markdown("""
    <style>
    .main-title {
        color: #D81B60;
        font-family: 'Avenir', 'Helvetica', sans-serif;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }
    .sub-title {
        color: #8E24AA;
        text-align: center;
        font-size: 1.1rem;
        margin-bottom: 25px;
    }
    .book-card {
        background-color: #FFFFFF;
        border-radius: 15px;
        padding: 18px;
        margin-bottom: 15px;
        transition: transform 0.2s ease-in-out;
    }
    .goal-box {
        background: linear-gradient(135deg, #FFE4EC 0%, #F8BBD0 100%);
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        color: #880E4F;
        font-weight: bold;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🌸 A Minha Estante 📖</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Acompanhando minhas leituras com carinho e estilo ✨</p>", unsafe_allow_html=True)

livros_ref = db.collection("livros").stream()
lista_livros = [doc.to_dict() for doc in livros_ref]

if len(lista_livros) == 0:
    st.info("Sua estante ainda está vazia! 🥺 Vamos à aba de cadastro para adicionar o seu primeiro livro. 🌸")
else:
    total_lidos = len(lista_livros)
    meta = 40
    progresso_pct = min(int((total_lidos / meta) * 100), 100)
    
    st.markdown(f"""
        <div class='goal-box'>
            <h2 style='margin:0; font-size: 1.6rem;'>🎯 Meta de Leituras 2026</h2>
            <p style='margin: 8px 0 0 0; font-size: 1.2rem;'>Você já leu <b>{total_lidos}</b> de <b>{meta}</b> livros! ({progresso_pct}%)</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.progress(min(total_lidos / meta, 1.0))
    st.write("")
    
    st.markdown("### 📚 Livros Lido(s)")
    
    cols = st.columns(2)
    
    for index, livro in enumerate(lista_livros):
        col = cols[index % 2]
        
        titulo = livro.get("titulo", "Sem Título")
        autor = livro.get("autor", "Desconhecido")
        nota = "⭐" * int(livro.get("nota", 5))
        data = livro.get("data_termino", "N/A")
        cor_capa = livro.get("cor_capa", "#FF6B8B")
        
        with col:
            st.markdown(f"""
                <div class='book-card' style='border-left: 6px solid {cor_capa}; box-shadow: 0px 4px 12px {cor_capa}40;'>
                    <h3 style='margin: 0; color: {cor_capa}; font-size: 1.2rem;'>📖 {titulo}</h3>
                    <p style='margin: 5px 0; color: #666; font-size: 0.95rem;'><b>Autor(a):</b> {autor}</p>
                    <p style='margin: 5px 0; font-size: 1rem;'><b>Avaliação:</b> {nota}</p>
                    <p style='margin: 5px 0; color: #888; font-size: 0.85rem;'>🗓️ Finalizado em: {data}</p>
                </div>
            """, unsafe_allow_html=True)

