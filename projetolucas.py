class Grafo:
    def __init__(self, conexoes): 
        self.grafo = {}
        for origem, destino, _ in conexoes:
            if origem not in self.grafo:
                self.grafo[origem] = []
            self.grafo[origem].append(destino)

    def busca_em_profundidade_limitada(self, origem, destino, profundidade_max):
        caminho = []
        visitados = set()
        
        def dfs_atual(no_atual, profundidade):
            if profundidade > profundidade_max:
                return False
            caminho.append(no_atual)
            visitados.add(no_atual)
            if no_atual == destino:
                return True
            
            for vizinho in self.grafo.get(no_atual, []):
                if vizinho not in visitados:
                    if dfs_atual(vizinho, profundidade + 1):
                        return True
            
            caminho.pop()
            return False
        
        if dfs_atual(origem, 0):
            return caminho
        else:
            return None


conexoes = [
    ('Oradea', 'Zerind', 71),
    ('Oradea', 'Sibiu', 151),
    ('Zerind', 'Arad', 75),
    ('Zerind', 'Oradea', 71),
    ('Arad', 'Timisoara', 118),
    ('Arad', 'Sibiu', 140),
    ('Timisoara', 'Lugoj', 111),
    ('Lugoj', 'Mehadia', 70),
    ('Mehadia', 'Dobreta', 75),
    ('Dobreta', 'Craiova', 120),
    ('Craiova', 'RimnicuVilcea', 146),
    ('Craiova', 'Pitesti', 138),
    ('RimnicuVilcea', 'Pitesti', 97),
    ('RimnicuVilcea', 'Sibiu', 80),
    ('Sibiu', 'Fagaras', 99),
    ('Pitesti', 'Bucharest', 101),
    ('Fagaras', 'Bucharest', 211),
    ('Bucharest', 'Giurgiu', 90),
    ('Bucharest', 'Urziceni', 85),
    ('Bucharest', 'Pitesti', 101),
    ('Urziceni', 'Hirsova', 98),
    ('Urziceni', 'Vaslui', 142),
    ('Hirsova', 'Eforie', 86),
    ('Vaslui', 'Iasi', 92),
    ('Iasi', 'Neamt', 87)
]


grafo = Grafo(conexoes)


cidade_origem = input("Digite a cidade de origem: ")
cidade_destino = input("Digite a cidade de destino: ")
profundidade_max = len(conexoes)


caminho = grafo.busca_em_profundidade_limitada(cidade_origem, cidade_destino, profundidade_max)


if caminho:
    print(f"Caminho encontrado: {' -> '.join(caminho)}")
else:
    print("Caminho não encontrado.")
