from extrator import extrair_para_lista
from servico_langchain import processar_avaliacao

arquivo_extraido = extrair_para_lista('interagindo_com_uma_llm_local/Analisador_de_sentimentos/avaliacoes.txt')

pross = 0
lista_avaliacoes = list()
for linha in arquivo_extraido:
      lista_avaliacoes.append(processar_avaliacao(linha))
      pross += 1
      print(f"processamento {pross} completo")

print(lista_avaliacoes)