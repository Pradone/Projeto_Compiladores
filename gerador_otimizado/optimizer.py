class Optimizer:

    def __init__(self, codigo):
        self.codigo = codigo

    def otimizar(self):
        codigo = self.constant_folding(self.codigo)
        codigo = self.simplificacao_algebrica(codigo)
        codigo = self.propagacao_copia(codigo)
        codigo = self.eliminar_temporarios_mortos(codigo)

        return codigo

    def constant_folding(self, codigo):
        otimizado = []

        for linha in codigo:
            partes = linha.split()

            if len(partes) == 5 and partes[1] == "=":
                destino = partes[0]
                esquerda = partes[2]
                operador = partes[3]
                direita = partes[4]

                if esquerda.lstrip("-").isdigit() and direita.lstrip("-").isdigit():
                    valor_esq = int(esquerda)
                    valor_dir = int(direita)

                    if operador == "+":
                        resultado = valor_esq + valor_dir
                    elif operador == "-":
                        resultado = valor_esq - valor_dir
                    elif operador == "*":
                        resultado = valor_esq * valor_dir
                    elif operador == "/" and valor_dir != 0:
                        resultado = valor_esq // valor_dir
                    else:
                        otimizado.append(linha)
                        continue

                    otimizado.append(f"{destino} = {resultado}")
                    continue

            otimizado.append(linha)

        return otimizado

    def propagacao_copia(self, codigo):
        valores = {}
        otimizado = []

        for linha in codigo:
            partes = linha.split()

            if len(partes) == 3 and partes[1] == "=":
                destino = partes[0]
                origem = partes[2]

                if origem in valores:
                    origem = valores[origem]

                if destino.startswith("t_"):
                    valores[destino] = origem

                otimizado.append(f"{destino} = {origem}")
                continue

            if len(partes) == 5 and partes[1] == "=":
                destino = partes[0]
                esquerda = valores.get(partes[2], partes[2])
                operador = partes[3]
                direita = valores.get(partes[4], partes[4])

                nova_linha = f"{destino} = {esquerda} {operador} {direita}"
                otimizado.append(nova_linha)
                continue

            otimizado.append(linha)

        return otimizado

    def eliminar_temporarios_mortos(self, codigo):
        usados = set()

        for linha in codigo:
            partes = linha.split()

            if len(partes) >= 3 and partes[1] == "=":
                partes_para_verificar = partes[2:]
            else:
                partes_para_verificar = partes

            for parte in partes_para_verificar:
                if parte.startswith("t_"):
                    usados.add(parte)

        otimizado = []

        for linha in codigo:
            partes = linha.split()

            if len(partes) >= 3 and partes[1] == "=":
                destino = partes[0]

                if destino.startswith("t_") and destino not in usados:
                    continue

            otimizado.append(linha)

        return otimizado

    def simplificacao_algebrica(self, codigo):
        otimizado = []

        for linha in codigo:
            partes = linha.split()

            if len(partes) == 5 and partes[1] == "=":
                destino = partes[0]
                esquerda = partes[2]
                operador = partes[3]
                direita = partes[4]

                if operador == "+" and direita == "0":
                    otimizado.append(f"{destino} = {esquerda}")
                    continue

                if operador == "+" and esquerda == "0":
                    otimizado.append(f"{destino} = {direita}")
                    continue

                if operador == "-" and direita == "0":
                    otimizado.append(f"{destino} = {esquerda}")
                    continue

                if operador == "*" and direita == "1":
                    otimizado.append(f"{destino} = {esquerda}")
                    continue

                if operador == "*" and esquerda == "1":
                    otimizado.append(f"{destino} = {direita}")
                    continue

                if operador == "*" and (esquerda == "0" or direita == "0"):
                    otimizado.append(f"{destino} = 0")
                    continue

                if operador == "/" and direita == "1":
                    otimizado.append(f"{destino} = {esquerda}")
                    continue

            otimizado.append(linha)

        return otimizado
