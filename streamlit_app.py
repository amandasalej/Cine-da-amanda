import streamlit as st

st.set_page_config(page_title="Minha Biblioteca", page_icon="🎀", layout="wide")

st.markdown("""
    <style>
    .title { 
        color: #D81B60; text-align: center; font-size: 2.8rem; 
        font-family: 'Avenir', sans-serif; margin-bottom: 5px; font-weight: bold;
    }
    .subtitle { 
        color: #8E24AA; text-align: center; font-size: 1.2rem; margin-bottom: 30px; 
    }
    .welcome-box {
        background-color: #FFFFFF; border-radius: 15px; padding: 25px;
        border-left: 6px solid #FF6B8B; box-shadow: 0px 4px 12px rgba(255, 107, 139, 0.15);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>🎀 Clube de Leitura da Amanda 🎀</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Buy me books & tell me I'm pretty ✨</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.image("https://i.ibb.co/0yf6PM7S/IMG-1554-removebg-preview.png", use_container_width=True)
    st.write("")
    st.image("https://i.ibb.co/W4JwrkRM/IMG-1555-removebg-preview.png", use_container_width=True)

with col2:
    st.markdown("""
        <div class='welcome-box'>
            <h3 style='color: #AD1457; margin-top:0;'>Bem-vinda ao seu diário literário! 🌸</h3>
            <p style='font-size: 1.1rem;'>Aqui é o lugar perfeito para guardar as suas aventuras e acompanhar a sua meta de 40 livros.</p>
            <hr style='border: 1px solid #FFE4EC;'>
            <ul style='font-size: 1.1rem; color: #4A3B40;'>
                <li>📝 <b>Cadastrar:</b> Adicione os novos livros que devorou (com a cor da capa!).</li>
                <li>📚 <b>A Minha Estante:</b> Gerencie os seus livros lidos e veja o seu progresso.</li>
            </ul>
            <p style='text-align: center; font-style: italic; color: #D81B60; margin-top: 20px;'>
                "Books are the mirror of the soul. - Virginia Woolf"
            </p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.image("https://i.ibb.co/KcjbQzLz/IMG-1556-removebg-preview.png", use_container_width=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #888; font-size: 0.9rem;'>Feito com 💖 e Streamlit</p>", unsafe_allow_html=True)




