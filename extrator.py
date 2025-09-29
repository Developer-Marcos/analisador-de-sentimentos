def extrair_para_lista(arq):
      lista_linhas = list()
      
      with open(arq, 'r') as arquivo: 
            for linha in arquivo.readlines():
                  lista_linhas.append(linha)

      return lista_linhas   