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
      Analise a avaliacao e retorne o usuario que fez ela, a avaliacao original, a traducao dessa avaliacao em portugues-BR, e
      se essa avaliacao foi positiva, negativa ou neutra. Tudo isso em JSON.
                              
      Essa é a avaliacao que voce tem que analisar: {avaliacao}. {formatacao_saida}
      """,

      input_variables=["avaliacao"],
      partial_variables={"formatacao_saida": parseador.get_format_instructions()})

      chain = prompt | llm
      resposta = chain.invoke({"avaliacao": avalicao})
      
      return resposta.content
