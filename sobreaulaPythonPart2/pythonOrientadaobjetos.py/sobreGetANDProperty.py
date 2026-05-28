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
       self.cor_tinta = cor
   @property 
   def cor(self):
        print("PROPERTY")
        return 'qualquer coisa, executei automatico, nao precisei chama o comando'
   @property  
   def cor_tampa(self):
        return "cor da tampa é preta ksksk"
caneta = Caneta('azul')
print(caneta.cor_tampa)
print(caneta.cor_tinta)
print(caneta.cor)
#############################################################
# agora sobre o ''SETTER' - getter e setter no modo pythonico 
