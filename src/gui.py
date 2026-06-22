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

