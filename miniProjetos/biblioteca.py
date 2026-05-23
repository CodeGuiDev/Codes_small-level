
class Biblioteca:

    def __init__(self):
        self.lista_livros = []
        self.lista_usuarios = []

    def cadastrar_livro(self, livro):
        self.lista_livros.append(livro)

    def cadastrar_usuario(self, usuario):
        self.lista_usuarios.append(usuario)

    def emprestar(self, usuario, livro):

        if livro.disponibilidade:

            livro.disponibilidade = False

            usuario.livros_emprestados.append(livro)

            print(f"{usuario.nomeuser} pegou o livro {livro.nome}")

        else:
            print("Livro indisponível")

    def devolver(self, usuario, livro):

        if livro in usuario.livros_emprestados:

            livro.disponibilidade = True

            usuario.livros_emprestados.remove(livro)

            print(f"{usuario.nomeuser} devolveu o livro {livro.nome}")

        else:
            print("Esse usuário não possui esse livro")

    def listar_livros(self):

        print("\n=== LIVROS ===")

        for livro in self.lista_livros:
            livro.informacoes()
            print("-" * 20)


class CadastroBook:

    def __init__(self, nome, autor):

        self.nome = nome
        self.autor = autor
        self.disponibilidade = True

    def informacoes(self):

        print(f"Título: {self.nome}")

        print(f"Autor: {self.autor}")

        if self.disponibilidade:
            print("Disponível")
        else:
            print("Emprestado")


class CadastroUSER:

    def __init__(self, nomeuser, idade):

        self.idade = idade
        self.nomeuser = nomeuser

        self.livros_emprestados = []

    def infoUSER(self):

        print(f"Nome: {self.nomeuser}")

        print(f"Idade: {self.idade}")

        print("Livros emprestados:")

        if len(self.livros_emprestados) == 0:
            print("Nenhum livro")

        else:
            for livro in self.livros_emprestados:
                print(livro.nome)


# livros que citei
livro1 = CadastroBook("Harry Potter", "J.K Rowling")

livro2 = CadastroBook("Senhor dos Anéis", "Tolkien")

#user ne
usuario1 = CadastroUSER("Guilherme", 17)


#nome da biblioteca que criei
biblioteca = Biblioteca()


#cadastro dos livros e usuario aqui
biblioteca.cadastrar_livro(livro1)
biblioteca.cadastrar_livro(livro2)

biblioteca.cadastrar_usuario(usuario1)
