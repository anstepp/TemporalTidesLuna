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
        self.infile = tk.StringVar()
        self.view = self.TemporalTidesView()
        self.model = self.TemporalTidesModel()
        self.controller = self.TemporalTidesController()

    #View
    class TemporalTidesView:
        """
            Display GUI from here. No logic, no storage.

            Functions:
            
                init = constructor

                _show_display = show the gui
                    args: none
        """
        def __init__(self):
            super().__init__()

            self.presenter = None

            self._show_display()

        def _show_display(self):
            pass
    
    # Model
    class TemporalTidesModel:
        """
            Logic here. We will keep lejaren imports at a minimum, and do that work in separate files.

            Functions:
            
                init = constructor
        """
        def __init__(self):
            pass

    # Controller
    class TemporalTidesController:
        """
            We will put bindings here to link the GUI (view) to the Logic (Model).

            Functions:
                init = constructor
        """
        def __init__(self):
            self.var = 1
            self.remove_short_rests = tk.BooleanVar()
            self.simplify_tuplets = tk.BooleanVar()
            self.replace_grace_notes = tk.BooleanVar()
            self.tie_redundant_notes = tk.BooleanVar()

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
        def button_check(self):
             r = {self.remove_short_rests, self.simplify_tuplets, 
                  self.replace_grace_notes, self.tie_redundant_notes}
             return r
            
        def check_result(self, state):
            return state

