workspace {

    model {
        user = person "User" "The person who interacts with the agricultural management system."

        system = softwareSystem "Agricultural Management System" {
            container = container "Application" "Python" "The core application handling user input and performing calculations."
        }

        user -> container "Interacts with"
    }

    views {
        container system {
            include *
            autolayout lr
            title "Container Diagram - Agricultural Management System"
        }
        theme default
    }
}
