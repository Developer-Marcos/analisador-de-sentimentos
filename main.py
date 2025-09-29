from extrator import extrair_para_lista
from servico_langchain import processar_avaliacao

arquivo_extraido = extrair_para_lista('interagindo_com_uma_llm_local/Analisador_de_sentimentos/avaliacoes.txt')

for linha in arquivo_extraido[0:5]:
      print(processar_avaliacao(linha))