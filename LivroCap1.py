def pesquisa(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            print("Achou!")
            return meio
        if chute > item:
            alto = meio - 1
        else:
            print("Esta baixo")
            baixo = meio + 1
    return None


print ('Comitando')
minha_lista = [1,3,5,7,9,11]
print(pesquisa(minha_lista, 7))



