import streamlit as st

st.set_page_config(page_title='Atividade 1 - Análise de Regressão', layout='centered', initial_sidebar_state='expanded')

paginas = {
    'Atividades': [st.Page('paginas/correlacao.py', title='Correlação', default=True),
                  st.Page('paginas/tarefa_m.py', title = 'Tarefa de amostragem (março)', default=True)]
}

pag = st.navigation(paginas)
pag.run()
