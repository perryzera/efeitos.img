class SistemaPontuacao:
    def __init__(self):
        self.valores = {
            'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1,
            'b': 2, 'c': 2, 'd': 2, 'f': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2, 'm': 2, 'n': 2, 'p': 2, 'q': 2, 'r': 2, 's': 2, 't': 2, 'v': 2, 'w': 2, 'x': 2, 'y': 2, 'z': 2
        }

    def calc_pts(self, palavra):
        pts = 0
        for letra in palavra:
            if letra.isupper():
                pts += self.valores[letra.lower()] * 2
            else:
                pts += self.valores.get(letra, 0)
        return pts

    def total_pts(self, palavras):
        pontuacoes = {}
        for palavra in palavras:
            pontuacoes[palavra] = self.calc_pts(palavra)
        return pontuacoes

sistema = SistemaPontuacao()
palavras = ['Universidade', 'Positivo', 'Ultimo', 'Ano', 'CHEGAAA']
pontuacoes = sistema.total_pts(palavras)

for palavra, pontos in pontuacoes.items():
    print(f'{palavra}: {pontos}')
