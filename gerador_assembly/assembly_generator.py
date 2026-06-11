class AssemblyGenerator:

    def __init__(self, codigo_3ac, tabela_simbolos):
        self.codigo_3ac = codigo_3ac
        self.tabela_simbolos = tabela_simbolos
        self.codigo = []
        self.strings = {}
        self.string_count = 0

    def gerar(self):
        self.pre_coletar_strings()
        self.gerar_data()
        self.gerar_code()

        return self.codigo

    def nova_string(self, valor):
        if valor in self.strings:
            return self.strings[valor]

        nome = f"str_{self.string_count}"
        self.string_count += 1
        self.strings[valor] = nome

        return nome

    def pre_coletar_strings(self):
        for linha in self.codigo_3ac:
            partes = linha.split()

            if len(partes) >= 3 and partes[1] == "=":
                origem = " ".join(partes[2:])

                if origem.startswith('"') and origem.endswith('"'):
                    texto = origem.strip('"')
                    self.nova_string(texto)

            if len(partes) >= 2 and partes[0] == "WRITE":
                valor = " ".join(partes[1:])

                if valor.startswith('"') and valor.endswith('"'):
                    texto = valor.strip('"')
                    self.nova_string(texto)

    def gerar_data(self):
        self.codigo.append("section .data")

        for simbolo in self.tabela_simbolos.simbolos.values():
            if simbolo.tipo == "INTEGER":
                self.codigo.append(f"{simbolo.nome} dw 0")
            elif simbolo.tipo == "BOOLEAN":
                self.codigo.append(f"{simbolo.nome} db 0")
            elif simbolo.tipo == "STRING":
                self.codigo.append(f"{simbolo.nome} db 255 dup(0)")

        for temp in self.coletar_temporarios():
            self.codigo.append(f"{temp} dw 0")

        for texto, nome in self.strings.items():
            self.codigo.append(f'{nome} db "{texto}",0')

        self.codigo.append("")

    def gerar_code(self):
        self.codigo.append("section .text")
        self.codigo.append("global _start")
        self.codigo.append("")
        self.codigo.append("_start:")

        for linha in self.codigo_3ac:
            self.traduzir_linha(linha)

        self.codigo.append("")
        self.codigo.append("; fim do programa")

    def coletar_temporarios(self):
        temporarios = set()

        for linha in self.codigo_3ac:
            partes = linha.split()

            for parte in partes:
                if parte.startswith("t_"):
                    temporarios.add(parte)

        return sorted(temporarios)

    def traduzir_linha(self, linha):
        partes = linha.split()

        if not partes:
            return

        if linha.endswith(":"):
            self.codigo.append(linha)
            return

        if partes[0] == "GOTO":
            self.codigo.append(f"    jmp {partes[1]}")
            return

        if partes[0] == "IF_FALSE":
            condicao = partes[1]
            label = partes[3]

            self.codigo.append(f"    cmp byte ptr [{condicao}], 0")
            self.codigo.append(f"    je {label}")
            return

        if partes[0] == "WRITE":
            valor = " ".join(partes[1:])

            if valor.startswith('"') and valor.endswith('"'):
                texto = valor.strip('"')
                label = self.nova_string(texto)
                self.codigo.append(f"    ; WRITE string {label}")
            else:
                self.codigo.append(f"    ; WRITE {valor}")

            return

        if partes[0] == "READ":
            valor = partes[1]
            self.codigo.append(f"    ; READ {valor}")
            return

        if len(partes) == 3 and partes[1] == "=":
            destino = partes[0]
            origem = partes[2]
            self.gerar_atribuicao(destino, origem)
            return

        if len(partes) >= 3 and partes[1] == "=":
            destino = partes[0]
            origem = " ".join(partes[2:])

            if origem.startswith('"') and origem.endswith('"'):
                self.gerar_atribuicao(destino, origem)
                return

        if len(partes) == 4 and partes[1] == "=" and partes[2] == "~":
            destino = partes[0]
            valor = partes[3]
            self.gerar_logico(destino, valor, "~")
            return

        if len(partes) == 5 and partes[1] == "=":
            destino = partes[0]
            esquerda = partes[2]
            operador = partes[3]
            direita = partes[4]
            self.gerar_operacao(destino, esquerda, operador, direita)
            return

        self.codigo.append(f"    ; instrução não traduzida: {linha}")

    def eh_numero(self, valor):
        return valor.lstrip("-").isdigit()

    def operando_word(self, valor):
        if self.eh_numero(valor):
            return valor

        return f"word ptr [{valor}]"

    def tipo_de(self, nome):
        if nome in ["TRUE", "FALSE"]:
            return "BOOLEAN"

        if nome.startswith("t_"):
            return "TEMP"

        simbolo = self.tabela_simbolos.buscar(nome)

        if simbolo is not None:
            return simbolo.tipo

        return None

    def operando_byte(self, valor):
        if valor == "TRUE":
            return "1"

        if valor == "FALSE":
            return "0"

        return f"byte ptr [{valor}]"

    def gerar_atribuicao(self, destino, origem):
        tipo_destino = self.tipo_de(destino)

        if origem.lstrip("-").isdigit():
            self.codigo.append(f"    mov word ptr [{destino}], {origem}")

        elif origem == "TRUE":
            self.codigo.append(f"    mov byte ptr [{destino}], 1")

        elif origem == "FALSE":
            self.codigo.append(f"    mov byte ptr [{destino}], 0")

        elif origem.startswith('"') and origem.endswith('"'):
            texto = origem.strip('"')
            label = self.nova_string(texto)

            self.codigo.append(f"    lea si, [{label}]")
            self.codigo.append(f"    lea di, [{destino}]")
            self.codigo.append(f"    ; copiar string de {label} para {destino}")

        elif tipo_destino == "BOOLEAN":
            self.codigo.append(f"    mov al, {self.operando_byte(origem)}")
            self.codigo.append(f"    mov byte ptr [{destino}], al")

        else:
            self.codigo.append(f"    mov ax, {self.operando_word(origem)}")
            self.codigo.append(f"    mov word ptr [{destino}], ax")

    def gerar_operacao(self, destino, esquerda, operador, direita):
        if operador in ["AND", "OR"]:
            self.gerar_logico(destino, esquerda, operador, direita)
            return

        if operador in ["<", "<=", ">", ">=", "==", "<>"]:
            self.gerar_relacional(destino, esquerda, operador, direita)
            return

        self.codigo.append(f"    mov ax, {self.operando_word(esquerda)}")

        if operador == "+":
            self.codigo.append(f"    add ax, {self.operando_word(direita)}")
        elif operador == "-":
            self.codigo.append(f"    sub ax, {self.operando_word(direita)}")
        elif operador == "*":
            self.codigo.append(f"    imul {self.operando_word(direita)}")
        elif operador == "/":
            self.codigo.append("    cwd")
            self.codigo.append(f"    idiv {self.operando_word(direita)}")
        else:
            self.codigo.append(f"    ; operação não implementada: {operador}")

        self.codigo.append(f"    mov word ptr [{destino}], ax")

    def gerar_relacional(self, destino, esquerda, operador, direita):
        label_true = f"{destino}_true"
        label_fim = f"{destino}_fim"

        self.codigo.append(f"    mov ax, {self.operando_word(esquerda)}")
        self.codigo.append(f"    cmp ax, {self.operando_word(direita)}")

        if operador == "<":
            salto = "jl"
        elif operador == "<=":
            salto = "jle"
        elif operador == ">":
            salto = "jg"
        elif operador == ">=":
            salto = "jge"
        elif operador == "==":
            salto = "je"
        elif operador == "<>":
            salto = "jne"
        else:
            self.codigo.append(
                f"    ; operador relacional não implementado: {operador}"
            )
            return

        self.codigo.append(f"    {salto} {label_true}")
        self.codigo.append(f"    mov byte ptr [{destino}], 0")
        self.codigo.append(f"    jmp {label_fim}")
        self.codigo.append(f"{label_true}:")
        self.codigo.append(f"    mov byte ptr [{destino}], 1")
        self.codigo.append(f"{label_fim}:")

    def gerar_logico(self, destino, esquerda, operador, direita=None):
        if operador == "~":
            self.codigo.append(f"    mov al, {self.operando_byte(esquerda)}")
            self.codigo.append("    xor al, 1")
            self.codigo.append(f"    mov byte ptr [{destino}], al")
            return

        self.codigo.append(f"    mov al, {self.operando_byte(esquerda)}")

        if operador == "AND":
            self.codigo.append(f"    and al, {self.operando_byte(direita)}")
        elif operador == "OR":
            self.codigo.append(f"    or al, {self.operando_byte(direita)}")
        else:
            self.codigo.append(f"    ; operação lógica não implementada: {operador}")
            return

        self.codigo.append(f"    mov byte ptr [{destino}], al")

    def salvar(self, caminho="output/final.asm"):
        with open(caminho, "w", encoding="utf-8") as arquivo:
            for linha in self.codigo:
                arquivo.write(linha + "\n")