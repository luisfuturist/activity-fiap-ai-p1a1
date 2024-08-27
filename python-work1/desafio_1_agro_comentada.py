# Definindo as culturas que serão suportadas pelo programa
# Aqui, estamos criando uma lista de culturas chamadas "culturas"
culturas = ["Café", "Soja"]

# Criamos duas listas vazias para armazenar os dados que vamos coletar
area_plantio = []  # Lista para armazenar as áreas plantadas
manejo_insumos = []  # Lista para armazenar as informações de manejo de insumos

# Função para calcular a área de plantio
# Ela recebe como parâmetros a cultura, a largura e o comprimento do terreno
def calcular_area_cultura(cultura, largura, comprimento):
    # Verifica qual cultura foi selecionada
    if cultura == "Café":
        # Se a cultura for "Café", calcula a área como sendo largura x comprimento
        return largura * comprimento
    elif cultura == "Soja":
        # Se a cultura for "Soja", também calcula a área como largura x comprimento
        return largura * comprimento
    else:
        # Se a cultura não for uma das suportadas, mostra uma mensagem de erro
        print("Cultura não suportada.")
        return 0  # Retorna 0 caso a cultura não seja suportada

# Função para calcular o manejo de insumos
# Ela calcula a quantidade total de insumos necessários para o plantio
def calcular_manejo_insumos(cultura, produto, quantidade_por_metro, largura, comprimento):
    # Primeiro, calcula a área de plantio usando a função acima
    area = calcular_area_cultura(cultura, largura, comprimento)
    # Depois, multiplica a área pela quantidade de insumo por metro quadrado
    total_insumos = area * quantidade_por_metro
    return total_insumos  # Retorna a quantidade total de insumos necessários

# Função para entrada de dados pelo usuário
# Essa função coleta todos os dados necessários para fazer os cálculos
def entrada_dados():
    # Mostra as opções de cultura para o usuário escolher
    print("\nEscolha a cultura:")
    for idx, cultura in enumerate(culturas):
        print(f"{idx + 1} - {cultura}")
    escolha_cultura = int(input("Digite o número da cultura escolhida: ")) - 1

    # Coleta os dados de largura e comprimento da área de plantio
    largura = float(input("Digite a largura da área de plantio (em metros): "))
    comprimento = float(input("Digite o comprimento da área de plantio (em metros): "))
    
    # Calcula a área de plantio e a adiciona na lista de áreas
    area = calcular_area_cultura(culturas[escolha_cultura], largura, comprimento)
    area_plantio.append(area)
    
    # Coleta o tipo de produto que será usado no manejo de insumos
    produto = input("Digite o produto para manejo de insumos: ")
    # Coleta a quantidade de produto necessária por metro quadrado
    quantidade_por_metro = float(input("Digite a quantidade do produto por metro quadrado: "))
    
    # Calcula a quantidade total de insumos necessários e adiciona na lista de manejo
    total_insumos = calcular_manejo_insumos(culturas[escolha_cultura], produto, quantidade_por_metro, largura, comprimento)
    manejo_insumos.append({
        "cultura": culturas[escolha_cultura],
        "produto": produto,
        "quantidade_por_metro": quantidade_por_metro,
        "total_insumos": total_insumos
    })

# Função para exibir os dados armazenados
def saida_dados():
    # Exibe os dados das áreas de plantio armazenadas
    print("\nDados da área de plantio:")
    for i, area in enumerate(area_plantio):
        print(f"Área {i + 1}: {area} metros quadrados")
    
    # Exibe os dados de manejo de insumos armazenados
    print("\nDados do manejo de insumos:")
    for i, manejo in enumerate(manejo_insumos):
        print(f"Insumo {i + 1}: Cultura: {manejo['cultura']}, Produto: {manejo['produto']}, Total Insumos: {manejo['total_insumos']} litros")

# Função para atualizar dados armazenados
def atualizar_dados():
    posicao = int(input("Digite a posição do dado que deseja atualizar: ")) - 1
    if 0 <= posicao < len(area_plantio):
        largura = float(input("Digite a nova largura da área de plantio (em metros): "))
        comprimento = float(input("Digite o novo comprimento da área de plantio (em metros): "))
        nova_area = calcular_area_cultura(culturas[posicao], largura, comprimento)
        area_plantio[posicao] = nova_area
        print("Área atualizada com sucesso.")
    else:
        print("Posição inválida.")

# Função para deletar dados armazenados
def deletar_dados():
    posicao = int(input("Digite a posição do dado que deseja deletar: ")) - 1
    if 0 <= posicao < len(area_plantio):
        del area_plantio[posicao]
        del manejo_insumos[posicao]
        print("Dado deletado com sucesso.")
    else:
        print("Posição inválida.")

# Função principal do menu, que permite ao usuário interagir com o programa
def menu():
    while True:
        # Exibe as opções do menu para o usuário
        print("\nMenu de Opções:")
        print("1 - Entrada de dados")
        print("2 - Saída de dados")
        print("3 - Atualizar dados")
        print("4 - Deletar dados")
        print("5 - Sair do programa")
        
        # Coleta a escolha do usuário
        opcao = int(input("Escolha uma opção: "))
        
        # Chama a função correspondente à opção escolhida
        if opcao == 1:
            entrada_dados()
        elif opcao == 2:
            saida_dados()
        elif opcao == 3:
            atualizar_dados()
        elif opcao == 4:
            deletar_dados()
        elif opcao == 5:
            print("Saindo do programa...")
            break  # Sai do loop e encerra o programa
        else:
            print("Opção inválida. Tente novamente.")

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    menu()  # Chama a função menu para iniciar o programa
