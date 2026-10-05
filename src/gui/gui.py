from re import search as re_search 
import os

import tkinter as tk

state = {"success": None, "msg": ""}

class TemporalTidesLunaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Temporal Tides Luna")
        self.model = self.TemporalTidesModel()
        self.view = self.TemporalTidesView(self, self.model, self.load_files)
        self.controller = self.TemporalTidesController(self.model, self.view)

    def load_files(self):
        self.controller.on_submit()

    # Model
    class TemporalTidesModel:
        """
            Logic here. We will keep lejaren imports at a minimum, and do that work in separate files.

            Functions:
            
                init = constructor
        """
        def __init__(self):

            #ingested file array
            self._ingested_files = []

            #grace note data
            self._grace_note_gui_bool = tk.BooleanVar()
            self._grace_note_flag = False
            #tuplet flag and max
            self._tuplet_gui_bool = tk.BooleanVar()
            self._tuplet_flag = False
            self._tuplet_gui_max = tk.IntVar()
            self._tuplet_max = 1 #TODO: must be int, verify
            #


    #View
    class TemporalTidesView(tk.Frame):
        """
            Display GUI from here. No logic, no storage.

            Functions:
            
                init = constructor

                _show_display = show the gui
                    args: none
        """
        def __init__(self, root, model, load_callback):
            super().__init__(root)
            self.model = model

            model._ingested_files = tk.Button(root, text="Load files in /input directory", command=load_callback)
            model._ingested_files.pack()

            self.grace_note_toggle = tk.Checkbutton(root, text="Grace Notes On/Off", variable=model._grace_note_gui_bool)
            self.grace_note_toggle.pack()

            self.tuplet_toggle = tk.Checkbutton(root, text="Tuplets On (see Max)", variable=model._tuplet_gui_bool)
            self.tuplet_toggle.pack()

            self.max_tuplet_val_label = tk.Label(root, text="Max Tuplets (3)")
            self.max_tuplet_val_label.pack()
            self.max_tuplet_val = tk.Entry(root, width=1)
            self.max_tuplet_val.pack()

            quit_button = tk.Button(root, text="Quit Application", command=root.destroy)
            quit_button.pack()

            self.presenter = None

            self._show_display()

        def _show_display(self):
            pass
    

    # Controller
    class TemporalTidesController:
        """
            We will put bindings here to link the GUI (view) to the Logic (Model).

            Functions:
                init = constructor
        """
        def __init__(self, model, view): 
            self.model = model
            self.view = view
            self.infile = "/input"

        def on_submit(self):
            # Perform your operational check
            path = "./input" #local to app directory only
            pattern = r'input\/[\w ]*\.musicxml'
            matching_files = [
                filename for filename in os.listdir(path) 
                if re_search(pattern, filename) and os.path.isfile(os.path.join(path, filename))
            ]
            if matching_files:
                for file in matching_files:
                    print(file)
            else:
                print("No Files")
        def check_result(self, state):
            return state
        
        # return nothing; simply update on call (helper function)
        def _get_grace_note_flag(self):
            """
                Helper function to get active grace note toggle.

                Args:
                    self: (the Controller)

                Returns:
                    None -> should be updated if we need to pass value instead
            """
            self.model._grace_note_flag = self.model._grace_note_gui_bool.get()

app = TemporalTidesLunaApp()
app.mainloop()