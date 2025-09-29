from pydantic import Field, BaseModel

class AvaliacaoParser(BaseModel):
      usuario: str = Field(description="Usuário que fez a avaliacao")
      resenha_original: str = Field(description="Avaliaca original feita pelo usuario")
      resenha_pt: str = Field(description="Avaliacao traduzida em portugues")
      avaliacao: str = Field(description="Polaridade da avaliacao (Positiva, Negativa, Neutra)")
