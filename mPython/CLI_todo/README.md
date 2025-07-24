## Console to-do list 
- The program is organized according to the MVC principle
- Using only command line interface, packages, modules
- Easy to expand
- Easy to read
---
## File structure
```  
.../
├── controllers/            # A module for processing logic
│   ├── __init__.py
│   └── task_controller.py  # Task controller
├── models/                 # A module for working with data
│   ├── __init__.py
│   └── task.py             # Task model
├── views/                  # A module for the user interface
│   ├── __init__.py
│   └── cli_view.py         # Representation for the console interface
└── main.py

```
