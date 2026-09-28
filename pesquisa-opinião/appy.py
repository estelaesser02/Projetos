# Pesquisa de satisfação - TudoWeb

excelente = 0
ruim = 0

# Pesquisa com 50 entrevistados
for i in range(1, 51):
    print(f"\n--- Entrevistado {i} ---")

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opção: "))

    # Verifica a opinião do entrevistado
    if opiniao == 1:
        excelente += 1
    elif opiniao == 2:
        pass
    elif opiniao == 3:
        ruim += 1
    else:
        print("Opção inválida!")

# Exibe os resultados
print("\n===== RESULTADO DA PESQUISA =====")
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM: {ruim}")