texto = "Computação em nuvem é a possibilidade de acessar arquivos " \
        " e executar diferentes tarefas pela internet, sem a necessidade de instalar aplicativos no computador "
contador = 0
contadorC = 0
maiorpalavra = ""
listamaior = []
listamaiorespalavras = []
listamenor = []
listamenorsv = []
listamenorespalavras = []
listamenorespalavrassv = []
menorpalavra = ""
listapalavrascomc = []

# -------------------filtro das menores palavras-------------------------------#
for i in range(0, len(listamenor)):  # for que vai de 0 até o tamanho da lista preliminar das menores
    if len(listamenor[i]) == len(
            listamenor[-1]):  # comparação levando em conta que o ultimo item da lista com certeza é um dos menores
        listamenorespalavras.append(listamenor[i])  # append numa outra lista filtrada
# -----------------------------------------------------------------------------#
# ---------------------menor palavra se as não vogais contarem-----------------#
menorpalavra = ""  # reset na menor palavra
for i in range(0, len(texto.split())):
    if len(texto.split()[i]) > 1:
        contador += 1  # contador das palavras
        if menorpalavra == "":
            menorpalavra = texto.split()[i]
        if len(texto.split()[i]) <= len(
                menorpalavra):
            menorpalavra = texto.split()[i]
            listamenorsv.append(menorpalavra)
# -------------------filtro das menores palavras sem vogal-------------------------------#
for i in range(0, len(listamenorsv)):  # for que vai de 0 até o tamanho da lista preliminar das menores
    if len(listamenorsv[i]) == len(
            listamenorsv[-1]):  # comparação levando em conta que o ultimo item da lista com certeza é um dos menores
        listamenorespalavrassv.append(listamenorsv[i])  # append numa outra lista filtrada
# -----------------------------------------------------------------------------#
# -------------------maiores palavras -----------------------------#
for i in range(0, len(texto.split())):
    if maiorpalavra == "":
        maiorpalavra = texto.split()[i]
    if len(texto.split()[i]) >= len(
            maiorpalavra):
        maiorpalavra = texto.split()[i]
        listamaior.append(maiorpalavra)
# -----------------------------------------------------------------------------#
# -------------------filtro das maiores palavras-------------------------------#
for i in range(0, len(listamaior)):  # for que vai de 0 até o tamanho da lista preliminar das maiores
    if len(listamaior[i]) == len(
            listamaior[-1]):  # comparação levando em conta que o ultimo item da lista com certeza é um dos maiores
        listamaiorespalavras.append(listamaior[i])  # append numa outra lista filtrada
# -----------------------------------------------------------------------------#
for i in range(0, len(texto.split())):
    if "C" in texto.upper().split()[i][0]:
        contadorC += 1
        listapalavrascomc.append(texto.upper().split()[i])

print(f"\nSe as vogais contarem, o texto tem {len(texto.split())} palavras, mas se elas não contarem o texto tem {contador} palavras ")
print(f"\nAs palavras que começam com C são: {listapalavrascomc} no total são {contadorC} palavras")
print(f"\nA maior palavra do texto é : {listamaiorespalavras} com {len(listamaiorespalavras[-1])} caracteres")
print(f"\nA lista das menores palavras são : {listamenorespalavrassv} com {len(listamenorespalavrassv[-1])} caracter(es) cada palavra")
