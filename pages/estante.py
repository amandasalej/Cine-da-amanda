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
        margin-bottom: 5px; /* Reduzi um pouco a margem para colar no menu de edição */
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

st.markdown("<h1 class='main-title'>Minha Estante 📖</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Acompanhando minhas leituras ✨</p>", unsafe_allow_html=True)

# 1. PUXANDO OS DADOS E O "RG" DE CADA LIVRO
lista_livros = []
for doc in db.collection("livros").stream():
    livro = doc.to_dict()
    livro["id"] = doc.id  # Guardando o ID único do Firebase
    lista_livros.append(livro)

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
        
        doc_id = livro["id"]
        titulo = livro.get("titulo", "Sem Título")
        autor = livro.get("autor", "Desconhecido")
        nota_num = int(livro.get("nota", 5))
        nota_str = "⭐" * nota_num
        data = livro.get("data_termino", "N/A")
        cor_capa = livro.get("cor_capa", "#FF6B8B")
        
        with col:
            # O Card Visual do Livro
            st.markdown(f"""
                <div class='book-card' style='border-left: 6px solid {cor_capa}; box-shadow: 0px 4px 12px {cor_capa}40;'>
                    <h3 style='margin: 0; color: {cor_capa}; font-size: 1.2rem;'>📖 {titulo}</h3>
                    <p style='margin: 5px 0; color: #666; font-size: 0.95rem;'><b>Autor(a):</b> {autor}</p>
                    <p style='margin: 5px 0; font-size: 1rem;'><b>Avaliação:</b> {nota_str}</p>
                    <p style='margin: 5px 0; color: #888; font-size: 0.85rem;'>🗓️ Finalizado em: {data}</p>
                </div>
            """, unsafe_allow_html=True)
            
            # 2. MENU SANFONA DE EDIÇÃO / EXCLUSÃO
            with st.expander("⚙️ Editar ou Apagar"):
                # Formulário para atualizar os dados
                with st.form(key=f"form_edit_{doc_id}"):
                    novo_titulo = st.text_input("Título", value=titulo)
                    novo_autor = st.text_input("Autor", value=autor)
                    nova_nota = st.number_input("Nota", value=nota_num, min_value=1, max_value=5)
                    nova_cor = st.color_picker("Cor da Capa", value=cor_capa)
                    
                    if st.form_submit_button("💾 Salvar Alterações"):
                        db.collection("livros").document(doc_id).update({
                            "titulo": novo_titulo,
                            "autor": novo_autor,
                            "nota": nova_nota,
                            "cor_capa": nova_cor
                        })
                        st.rerun() # Atualiza a página automaticamente!
                
                # Botão isolado para apagar
                if st.button("🗑️ Apagar Livro", key=f"btn_del_{doc_id}"):
                    db.collection("livros").document(doc_id).delete()
                    st.rerun() # Atualiza a página automaticamente!


