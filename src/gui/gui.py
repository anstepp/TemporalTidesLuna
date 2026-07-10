from re import search as re_search 

import tkinter as tk

global root
root = tk.Tk()

state = {"success": None, "msg": ""}

class TemporalTidesLunaApp(tk.Tk):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Temporal Tides Luna")
        self.model = self.TemporalTidesModel()
        self.view = self.TemporalTidesView(self.model)
        self.controller = self.TemporalTidesController(self.model, self.view)

    # Model
    class TemporalTidesModel:
        """
            Logic here. We will keep lejaren imports at a minimum, and do that work in separate files.

            Functions:
            
                init = constructor
        """
        def __init__(self):

            #grace note data
            self._grace_note_gui_bool = tk.BooleanVar()
            self._grace_note_flag = False

    #View
    class TemporalTidesView:
        """
            Display GUI from here. No logic, no storage.

            Functions:
            
                init = constructor

                _show_display = show the gui
                    args: none
        """
        def __init__(self, model):
            super().__init__()

            self.model = model

            self.grace_note_toggle = tk.Checkbutton(root, text="Grace Notes On/Off", variable=model._grace_note_gui_bool)

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
            self.var = 1
            self.model = model
            self.view = view

        def on_submit(self, result_container):
            # Perform your operational check
            if isinstance(self.infile.get(), str):
                if re_search(r'*\.musicxml', self.infile.get()):
                    result_container["success"] = True
                    result_container["msg"] = "Actual Music XML File"
                    root.destroy() 
            else:
                result_container["success"] = False
                result_container["msg"] = "Not String"
                # Keep GUI open for another attempt

        def check_result(self, state):
            return state
        
        def is_this_one(self, add_int=0) -> int:
            return self.var + add_int
        
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

