import streamlit as st

st.set_page_config(page_title="Biblioteca da Amanda", page_icon="📚")

st.markdown("# 🎀 **Biblioteca da Amanda** ✨")
st.markdown("---") 


st.markdown("Bem-vinda ao meu cantinho de leitura! Aqui eu guardo minhas histórias favoritas e acompanho minhas leituras. 💖")

st.markdown("### 🎯 **Minha Meta Literária:**")
st.markdown("""
- Ler **40 livros** este ano! 📚
- Deixar tudo catalogado e organizado. 💅
""")

st.image(
    "https://unsplash.com/pt-br/fotografias/papel-branco-para-impressora-yz4VF6x0W3M", 
    caption="Meu mundo em páginas! 🌸✨"
)

st.markdown("### 📝 **Cadastrar Nova Leitura**")
st.markdown("Preencha os detalhes abaixo para guardar mais um livro na sua estante. 💖")

# Formulário
with st.form("form_cadastro_livro"):
    
    titulo = st.text_input("Título do Livro 📖", placeholder="Ex: Os Sete Maridos de Evelyn Hugo")
    autor = st.text_input("Autor(a) ✍️", placeholder="Ex: Taylor Jenkins Reid")
    
    nota = st.number_input("Sua Nota (1 a 5) ⭐", min_value=1, max_value=5, step=1)
    
    data_termino = st.date_input("Quando você terminou de ler? 📅", format="DD/MM/YYYY")
    
    cor_capa = st.color_picker("Qual a cor da capa? 🎨")
    
    btn_salvar = st.form_submit_button("Guardar na Estante 🎀")
    
    if btn_salvar:
        if not titulo:
            st.warning("Eii, você esqueceu de preencher o título!!")
        else:
            st.success(f"Eba! O livro **{titulo}** foi cadastrado com sucesso! 🎉")
            st.balloons() # Uma animação fofa de balões!


