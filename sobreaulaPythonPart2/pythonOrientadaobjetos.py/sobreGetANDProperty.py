# class Caneta():
#     def __init__(self, cor):
#         self.cor_tinta = cor 

#     def get_cor(self):
#         return self.cor_tinta
##########################################################
# @properety - é um getter no modo Pythonico 
# getter - uum metodo para obter um atributo 
# cor -> get_cor()
# modo pythonico -- modo do python de fazer coisas
# property é uma propriedade do objeto, ela
# é um metodo que se comporto como um atributo  
####################################################
class Caneta():
   def __init__(self, cor):
       self._cor_tinta = cor
     # uso bom de desenvolvedor, quando quero dizer que aquele metodo de instancia
     # é (PRIVATE) (PROTECT) (PUBLIC)
     # os DEV utilizam atributos comecaçando com underline "_" para dizer que ele estar protegido
     # fora que com undeline ele nao deve ser USADO!!!!
   @property  # diferença que getter ele so faz açoes com instancias sem receber valores
   def cor(self):
        print("PROPERTY")
        return self._cor_tinta
  # aqui recebe o valor 
   

   @cor.setter #configura o valor
   def cor(self, valor_dacor):
    print(f'estou no setter com cor {valor_dacor}')
    self._cor_tinta = valor_dacor  


caneta = Caneta('azul')
caneta.cor = "rosa com verde claro"
print(caneta.cor)
#############################################################
# agora sobre o ''SETTER' - getter e setter no modo pythonico 
# ja o setter ele pode mudar valores e receber
# aqui vou dar um breve resumo com minhas palavras sobre conteudo da semana
# getter usando como metado para receber um valor e nao muda-lo e fazer algum comando
# ja o setter ele recebe o valor da instancia original ou de alguma outra, e consegue mudar ela ou add algo nela
# dois comandos mais usados dos decoradores deles sao: "Property" and "(nome da class)+.setter"
