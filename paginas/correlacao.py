import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import re
import base64
import tabulate


def ajustar_caminho_imagem(texto_markdown):
    # Expressão regular para encontrar imagens no markdown
    padrao = r"!\[.*?\]\((.*?)\)"
    
    # Função auxiliar para converter imagem para base64
    def converter_para_base64(match):
        caminho_imagem = match.group(1)
        try:
            with open(caminho_imagem, "rb") as img_file:
                encoded_string = base64.b64encode(img_file.read()).decode("utf-8")
            return f'![Imagem](data:image/png;base64,{encoded_string})'
        except Exception as e:
            return f"Erro ao carregar imagem: {str(e)}"

    # Substitui os caminhos de imagem pelo formato base64
    texto_corrigido = re.sub(padrao, converter_para_base64, texto_markdown)
    return texto_corrigido

st.title('Correlação: visualização e interpretação')

# Dados para o gráfico 1
tamanho = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
custo = [65, 120, 210, 260, 380, 450, 510, 555, 615, 660]

base1 = pd.DataFrame({'Tamanho': tamanho, 'Custo': custo})
grafico = sns.scatterplot(data = base1, x = 'Tamanho', y = 'Custo')
grafico1_path = 'grafico1.png'
plt.savefig(grafico1_path, dpi=300, bbox_inches='tight')
plt.close()

correlacao1 = base1.corr()

# Texto para o primeiro gráfico
texto1 = f'''## Diagrama de dispersão: tamanho x custo

![]({grafico1_path})

{correlacao1.to_markdown()}

Os dados estão positivamente correlacionados. Com um coeficiente de correlação linear de,
aproximadamente, 0.994, analisa-se que o tamanho está associado ao custo. Quanto maior o tamanho, maior será o custo.'''

# Corrigir caminho da imagem no texto usando base64
texto1_final = ajustar_caminho_imagem(texto1)

st.markdown(texto1_final)

# Dados para o gráfico 2
brancas = [8, 5, 12, 4, 11, 6, 8, 7, 7, 12, 7,
           3, 11, 14, 11, 9, 6, 6, 5, 6, 10, 14,
           4, 5, 5]

tempo = [5, 10, 6, 11, 5, 14, 30, 11, 17, 3, 9,
         3, 8, 8, 5, 5, 7, 4, 3, 7, 9, 11,
         11, 9, 4]

base2 = pd.DataFrame({'brancas': brancas, 'tempo': tempo})
grafico2 = sns.scatterplot(data = base2, y = 'tempo', x = 'brancas')
grafico2_path = 'grafico2.png'
plt.savefig(grafico2_path, dpi = 300, bbox_inches = 'tight')
plt.close()
correlacao2 = base2.corr()

# Texto para o segundo gráfico
texto2 = f'''## Diagrama de dispersão: Células Brancas x Tempo de Internação

![]({grafico2_path})

{correlacao2.to_markdown()}

Com um coeficiente de correlação linear de Pearson de -0.04, verifica-se que os dados não estão correlacionados. 
Como o valor está próximo de zero, não podemos afirmar que existe relação entre as variáveis.'''

# Corrigir caminho da imagem no texto usando base64
texto2_final = ajustar_caminho_imagem(texto2)

st.markdown(texto2_final)
