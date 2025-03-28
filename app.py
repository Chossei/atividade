import streamlit as st

st.set_page_config(page_title='Atividade 1 - Análise de Regressão', layout='centered', initial_sidebar_state='expanded')

paginas = {
    'Análise de Regressão (MAT229)': [st.Page('paginas/correlacao.py', title='Correlação', default=True)],
    'Amostragem (MATD44)': [st.Page('paginas/tarefa_m.py', title = 'Tarefa de amostragem (março)', default=False)]
}

pag = st.navigation(paginas)
pag.run()
