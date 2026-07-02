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
            self.remove_short_rests = tk.BooleanVar()
            self.simplify_tuplets = tk.BooleanVar()
            self.replace_rests = tk.BooleanVar()
            self.combine_redundant_notes = tk.BooleanVar()
            pass

        def on_start(self, controller):
            replace_rests = controller.get_replace_rests_bool(self)
            simplify_tuplets = controller.get_simplify_tuplets_bool(self)
            remove_short_rests = controller.get_simplify_tuplets_bool(self)
            if replace_rests:
                #for note in .xml
                    #if note should be a rest:
                        #note.make_rest()
                pass
            return replace_rests and simplify_tuplets and remove_short_rests
            
            # Not sure if I have the right idea here, as it is supposed to run on "submitting" the whole GUI, but I am not sure if this is right

    # Controller
    class TemporalTidesController:
        """
            We will put bindings here to link the GUI (view) to the Logic (Model).

            Functions:
                init = constructor
        """
        def __init__(self):
            self.var = 1
            self.remove_short_rests_cont = False
        
        def get_short_rest_bool(self, model):
            self.remove_short_rests_cont = model.remove_short_rests.get()
            return self.remove_short_rests_cont

        def get_replace_rests_bool(self, model):
            replace = model.replace_rests.get() 
            return replace 
            
        def get_simplify_tuplets_bool(self, model):
            simplify = model.simplify_tuplets.get()
            return simplify
            
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
            pass
            
        def check_result(self, state):
            return state

