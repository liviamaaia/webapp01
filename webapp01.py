# myFirstStreamlitApp.py
#import the libraries
import streamlit as st
from PIL import Image

image01 = Image.open('desenvolvimento.jpg')
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("LULA 2022")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("Motivos para tirar o Bolsonaro da presidencia")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader(" O governo não pode dar educação,porque a educação derruba o governo!!! ")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("Como já deve ter percebido, JR bolsonaro zomba de assuntos serios e tem falas homofobicas,racistas,machistas e etc...")

st.subheader("------ **Desenvolvido por:MAIA** -----
             
             
             Enquanto o Brasil ponteia a liderança mundial no número mortos pelo Covid-19, Bolsonaro lidera um governo incapaz de conviver com a democracia e de atender às reais necessidades do povo brasileiro”, diz a nota distribuída pelos dirigentes do PT aos diretórios municipais e estaduais da sigla.")

menu = [" do presidente Jair Bolsonaro. A campanha ‘Fora Bolsonaro’ é considerada prioridade pelo partido. Os movimentos sociais, a oposição e organizações da sociedade civil já estão com o site campanhaforabolsonaro.org.br, coletando inclusive assinaturas em apoio ao impeachment do presdiente da República.Texto_Colunas",
        "Texto_Markdown",
        "Inserir_Figura"]
choice = st.sidebar.selectbox("Menu de Opções",menu)
st.sidebar.write("Texto Side Bar")
    
if choice == "Texto_Colunas":       
    st.subheader("Texto formatado em colunas")
    st.write("Veja a seguir uma opção de formatação em colunas")    
    cols01 = st.columns(2)    
    cols01[0].write('Texto da Coluna 01')
    cols01[1].write('Texto da Coluna 02')
elif choice == "Texto_Markdown":
    st.subheader("Texto Markdown")
    st.write("Veja a seguir opção de formatação de texto Markdown")
    st.markdown(
    """
    ## *Alguns sites referências*:    
    - [Streamlit: hello world](https://calmcode.io/streamlit/hello-world.html)
    - [:star: Streamlit emoji shortcodes](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlitapp.com/)
    - [Layouts and Containers](https://docs.streamlit.io/library/api-reference/layout)
   
    ##### CRONOGRAMA
    DIA | CH HORÁRIA | CONTEÚDO
    :---------: | :------: | :-------:
    Dia 1 de 2 | ?h | ? a ?
    Dia 2 de 2 | ?h | ? a ?
    """
    )
elif choice == "Inserir_Figura":
    st.image(image01, width=800, caption='Rótulo da Imagem 01') 
    
