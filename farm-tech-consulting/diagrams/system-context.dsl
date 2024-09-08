workspace {

    model {
        user = person "User" "The person who interacts with the agricultural management system."

        system = softwareSystem "Agricultural Management System" "A console-based application for managing crop data."

        user -> system "Uses"
    }

    views {
        systemContext system {
            include *
            autolayout lr
            title "Context Diagram - Agricultural Management System"
        }
        theme default
    }
}
