def validate_input(prompt: str, valid_options: list[str] = None, is_numeric: bool = False, min_value: float = None) -> str or float:
    """
    Validates the user's input based on the provided options and requirements.

    Args:
        prompt (str): The prompt to display to the user.
        valid_options (list[str], optional): A list of valid string options. Defaults to None.
        is_numeric (bool, optional): Whether the input should be a numeric value. Defaults to False.
        min_value (float, optional): The minimum numeric value allowed. Defaults to None.

    Returns:
        str or float: The validated input, either as a string or a float depending on the requirements.
    """
    while True:
        user_input = input(prompt)
        if is_numeric:
            try:
                value = float(user_input)
                if min_value is not None and value < min_value:
                    print(f"Valor deve ser maior ou igual a {min_value}. Tente novamente.")
                else:
                    return value
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")
        elif valid_options is not None:
            if user_input.lower() in valid_options:
                return user_input.lower()
            else:
                print("Opção inválida. Tente novamente.")
        else:
            return user_input

def choose_crop() -> str:
    """
    Presents a list of crops to the user and allows them to choose one.

    Returns:
        str: The chosen crop as a string.
    """
    crops = ["cana-de-açúcar", "laranja"]
    print("\nEscolha a cultura:")
    for i, crop in enumerate(crops):
        print(f"{i + 1}. {crop}")
    
    choice = validate_input("Digite o número correspondente à cultura: ", valid_options=[str(i+1) for i in range(len(crops))])
    return crops[int(choice) - 1]

def calculate_crop_area(crop: str) -> float:
    """
    Calculates the area of land based on the crop type.

    Args:
        crop (str): The type of crop ('cana-de-açúcar' or 'laranja').

    Returns:
        float: The calculated area in square meters.
    """
    if crop == "cana-de-açúcar":
        length = validate_input("Digite o comprimento do terreno (em metros): ", is_numeric=True, min_value=0)
        width = validate_input("Digite a largura do terreno (em metros): ", is_numeric=True, min_value=0)
        # rectangle
        area = length * width
    elif crop == "laranja":
        radius = validate_input("Digite o raio do terreno (em metros): ", is_numeric=True, min_value=0)
        #Circle
        area = 3.14159 * (radius ** 2)
    else:
        print("Cultura não suportada.")
        area = 0
    return area

def calculate_inputs(area: float, crop: str) -> float:
    """
    Calculates the required inputs based on the area and crop type.

    Args:
        area (float): The area of the land in square meters.
        crop (str): The type of crop ('cana-de-açúcar' or 'laranja').

    Returns:
        float: The calculated input quantity in kilograms or liters.
        str: The type of input (herbicide or insecticide).
    """

    if crop == "cana-de-açúcar":
        input_per_square_meter = 0.02 # 20 mL/m²
        input_quantity = area * input_per_square_meter
        input_type = "Inseticida"
    elif crop == "laranja":
        input_per_square_meter = 0.03 # 30 mL/m²
        input_quantity = area * input_per_square_meter
        input_type = "Herbicida"
    else:
        print("Cultura não suportada.")
        input_quantity = 0
    return input_quantity, input_type

def display_data(crops: list[str], areas: list[float], inputs: list[float]) -> None:
    """
    Displays all stored data with indexes.

    Args:
        crops (list[str]): List of crop types.
        areas (list[float]): List of corresponding areas.
        inputs (list[float]): List of corresponding input quantities.
    """
    for i in range(len(crops)):
        print(f"Indice[{i}] - Cultura: {crops[i]}, Área: {areas[i]:.2f} m², Insumos: {inputs[i]:.2f} kg ou L")

def display_menu() -> None:
    """
    Displays the main menu of options.
    """
    print("\nMenu de Opções:")
    print("1. Entrada de dados")
    print("2. Saída de dados")
    print("3. Atualizar dados")
    print("4. Deletar dados")
    print("5. Sair do programa")

def main() -> None:
    """
    Main function that runs the agricultural management system.
    """
    crops = []
    areas = []
    inputs = []
    
    while True:
        display_menu()
        option = validate_input("Escolha uma opção: ", valid_options=["1", "2", "3", "4", "5"])

        if option == "1":
            crop = choose_crop()
            area = calculate_crop_area(crop)
            input_quantity, input_type = calculate_inputs(area, crop)
            
            crops.append(crop)
            areas.append(area)
            inputs.append(input_quantity)
            print(f"Para a cultura {crop}, dentro da área de {area:.2f} m², você precisará de {input_quantity:.2f} L (litros) de {input_type}.")

        elif option == "2":
            display_data(crops, areas, inputs)
        
        elif option == "3":
            if not crops:
                print("Não há dados disponíveis para atualizar.")
                continue

            print("\nDados disponíveis para atualização:")
            display_data(crops, areas, inputs)
            
            index = validate_input("Digite o índice do dado que deseja atualizar: ", is_numeric=True, min_value=0)
            index = int(index)
            if 0 <= index < len(crops):
                new_crop = choose_crop()
                new_area = calculate_crop_area(new_crop)
                new_input = calculate_inputs(new_area, new_crop)
                
                crops[index] = new_crop
                areas[index] = new_area
                inputs[index] = new_input
                print("Dados atualizados com sucesso!")
            else:
                print("Índice inválido.")
        
        elif option == "4":
            if not crops:
                print("Não há dados disponíveis para deletar.")
                continue

            print("\nDados disponíveis para exclusão:")
            display_data(crops, areas, inputs)
            
            index = validate_input("Digite o índice do dado que deseja deletar: ", is_numeric=True, min_value=0)
            index = int(index)
            if 0 <= index < len(crops):
                del crops[index]
                del areas[index]
                del inputs[index]
                print("Dados deletados com sucesso!")
            else:
                print("Índice inválido.")
        
        elif option == "5":
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
