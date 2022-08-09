class Jogador:
    def __init__(self,nome,idade,posicao,habilidade):
        self.nome=nome
        self.idade=idade
        self.posicao=posicao
        self.habilidade=habilidade

class Time:
    def __init__(self, nome, nome_completo, estadio, forca, potencial):
        self.nome=nome
        self.nome_completo=nome_completo
        self.estadio=estadio
        self.forca=forca
        self.potencial=potencial
        self.elenco=[]
        self.dinheiro=0

class Estadio:
    def __init__(self, nome, capacidade, proprietario):
        self.nome=nome
        self.capacidade=capacidade
        self.proprietario=proprietario

class Tecnico:
    def __init__(self, nome):
        self.nome=nome

class Competicao:
    def __init__(self, descricao, formato):
        self.formato=formato
        self.descricao=descricao
        self.clubes=[]
