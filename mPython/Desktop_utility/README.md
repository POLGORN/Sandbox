## A desktop utility with a GUI designed to work with .xml/.xlsx files
- Division into modules
- Rebuilding to the MVC pattern
- All kinds of tests
- Simple input & output
- Simple template for future
## File structure
```
.../
├── tests/
│   ├── test_controller.py
│   ├── test_model.py
│   └── test_view.py
├── main.py 
│   # The main file for launching the application
├── model.py
│   # The model will store the data and logic of the application
├── view.py
│   # The view will be responsible for displaying the interface
└── controller.py
    # The controller will link the model and the view
```