# method vs @classmethod vs @staticmethod

# method - self, método de instância
# nada mais é que uso padrao de classes, self como primeira instancia das funçoes 
# @classmethod - cls, método de classe
# cls ele faz com que nao precisamos passar algum tipo de instancia e ja deixa ela em alguma funçao com valor unico (anonimo)
# @staticmethod - método estático (❌self, ❌cls)
class Connection:
    def __init__(self, host= "local host"):
        self.host = host
        self.user = None
        self.password = None
    def set_user(self, user):
        self.user = user
    def set_password(self, password):
        self.password = password

c1 = Connection()
c1.set_user = 'guilherme'
c1.set_password = 'octo_code'
print(c1.set_user)
print(c1.set_password)