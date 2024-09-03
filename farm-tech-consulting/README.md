
# Agricultural Management System

## Overview

This Python program is designed to assist in managing agricultural data for different crops. It allows users to input data about crop areas, calculate the required inputs (such as fertilizers or water), update existing data, delete data, and view the information stored. The program supports two crops: **sugarcane (cana-de-açúcar)** and **orange (laranja)**.

## Features

- **Data Entry:** Input information about the crop, area of the land, and calculate the required inputs based on the crop type.
- **Data Viewing:** Display all stored data, including the crop type, area, and calculated inputs.
- **Data Updating:** Modify existing data entries, including changing the crop type and recalculating the area and inputs.
- **Data Deletion:** Remove specific entries from the stored data.
- **Menu-driven Interface:** Navigate through the program's features using a simple menu interface.

## Installation

1. Ensure that Python is installed on your system. This program is compatible with Python 3.x.
2. Download the program file (e.g., `agricultural_management.py`).
3. Place the file in a directory of your choice.

## Usage

1. Run the program using the command:
   ```
   python agricultural_management.py
   ```
2. Follow the menu options displayed in the terminal to:
   - Enter new data.
   - View existing data.
   - Update or delete specific entries.
   - Exit the program.

### Menu Options

- **1. Entrada de dados:** Start by choosing the crop type, then enter the land dimensions. The program calculates the area and required inputs automatically.
- **2. Saída de dados:** View all stored data entries, each with an index, crop type, area, and input quantities.
- **3. Atualizar dados:** Update an existing data entry by selecting its index from the displayed list, then re-enter the new data.
- **4. Deletar dados:** Delete an existing data entry by selecting its index from the displayed list.
- **5. Sair do programa:** Exit the program.

### Example Usage

After starting the program, you'll be presented with a menu. Selecting option 1 ("Entrada de dados") will guide you through entering data for a crop. For example:

```
Escolha uma opção: 1
Escolha a cultura:
1. cana-de-açúcar
2. laranja
Digite o número correspondente à cultura: 1
Digite o comprimento do terreno (em metros): 100
Digite a largura do terreno (em metros): 100
Para a cultura cana-de-açúcar, dentro da área de 10000.00 m², você precisará de 200.00 L (litros) de Inseticida.
```

The program will calculate the area and required inputs based on the crop type and display the stored data using option 2.

## Customization

The program can be extended to support more crops or different types of input calculations by modifying the `choose_crop`, `calculate_crop_area`, and `calculate_inputs` functions.

## License

This project is licensed under the [MIT License](../LICENSE).
