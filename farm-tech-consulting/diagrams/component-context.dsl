workspace {

    model {
        system = softwareSystem "Agricultural Management System" {
            container = container "Application" "Python" "The core application handling user input and performing calculations." {
                
                validate_input = component "Input Validation" "Python function" "Validates user inputs based on certain criteria."
                choose_crop = component "Choose Crop" "Python function" "Presents a list of crops and allows the user to choose one."
                
                calculate_crop_area = component "Calculate Crop Area" "Python function" "Calculates the area based on the crop type (Rectangle: length × width, Circle: π × radius²)."
                
                calculate_inputs = component "Calculate Inputs" "Python function" "Calculates input quantity (Inseticida: area × 0.02 L/m², Herbicida: area × 0.03 L/m²)."
                
                display_data = component "Display Data" "Python function" "Displays all stored data."
                display_menu = component "Display Menu" "Python function" "Displays the main menu of options."
                main_function = component "Main Function" "Python function" "Coordinates the flow of the application and user interaction."

                validate_input -> choose_crop "Called by"
                validate_input -> calculate_crop_area "Called by"
                validate_input -> calculate_inputs "Called by"
                validate_input -> display_data "Called by"
                validate_input -> display_menu "Called by"
                
                choose_crop -> validate_input "Validates user choice"
                calculate_crop_area -> validate_input "Validates dimensions"
                calculate_inputs -> calculate_crop_area "Uses crop area"
                display_data -> main_function "Displays results"
                display_menu -> main_function "Displays options"
                main_function -> display_menu "Shows menu options"
                main_function -> choose_crop "Allows user to choose crop"
                main_function -> calculate_crop_area "Calculates area based on crop"
                main_function -> calculate_inputs "Calculates inputs based on area"
                main_function -> display_data "Displays data"
            }
        }
    }

    views {
        component container {
            include *
            autolayout lr
            title "Component Diagram - Agricultural Management System"
        }
        theme default
    }
}
