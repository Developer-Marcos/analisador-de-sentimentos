from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from parser import AvaliacaoParser

LLM_API_BASE = "http://localhost:1234/v1"
API_KEY_PLACEHOLDER = "LM_Studio"

llm = ChatOpenAI(
      model="gemma-3-12b",
      base_url=LLM_API_BASE,
      api_key=API_KEY_PLACEHOLDER
)

parseador = JsonOutputParser(pydantic_object=AvaliacaoParser)
def processar_avaliacao(avalicao):
      prompt = PromptTemplate(template="""
Você é um analista de resenhas. Sua única tarefa é PREENCHER o esquema JSON fornecido.
Analise a avaliacao e retorne um objeto JSON que contenha:
1. o usuario que fez a avaliacao,
2. a avaliacao original,
3. a traducao dessa avaliacao em portugues-BR,
4. a polaridade (Positiva, Negativa ou Neutra).
                              
**NÃO RETORNE NENHUM TEXTO ALÉM DO OBJETO JSON. NÃO REPITA O ESQUEMA.**

Siga este formato JSON: {formatacao_saida}
                                 
Essa é a avaliacao que você tem que analisar: {avaliacao}
""",

      input_variables=["avaliacao"],
      partial_variables={"formatacao_saida": parseador.get_format_instructions()})

      chain = prompt | llm | parseador
      resposta = chain.invoke({"avaliacao": avalicao})
      
      return resposta
