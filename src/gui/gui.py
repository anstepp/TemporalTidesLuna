from re import search as re_search 
import os

import tkinter as tk

try:
    from . import lejaren_hooks as lh
except ImportError:
    print("Lejaren failed to Import... Quitting")
    raise SystemExit(1)

class TemporalTidesLunaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Temporal Tides Luna")
        self.model = self.TemporalTidesModel()
        self.view = self.TemporalTidesView(self, self.model, self.load_files, self.write_files)
        self.controller = self.TemporalTidesController(self.model, self.view)

    def load_files(self):
        self.controller.on_submit()

    def write_files(self):
        self.controller.write_files()

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
            # multiply note value
            self._note_multiplier_gui_bool = tk.BooleanVar()
            self._note_multiplier_flag = False
            self._note_multiplier_gui_val = tk.DoubleVar()
            self._note_multiplier_val = 1 #Multiple by 1 to maintain please
            self._note_multiplier_gui_range_min = tk.IntVar()
            self._note_multiplier_gui_range_max = tk.IntVar()
            self._note_multiplier_range_min = 0
            self._note_multiplier_range_max = 1 # set to max measure on default?


    #View
    class TemporalTidesView(tk.Frame):
        """
            Display GUI from here. No logic, no storage.

            Functions:
            
                init = constructor

                _show_display = show the gui
                    args: none
        """
        def __init__(self, root, model, load_callback, write_callback):
            super().__init__(root)
            self.model = model

            #input
            self._ingested_files = tk.Button(root, text="Load files in /input directory", command=load_callback)
            self._ingested_files.grid(row=0,column=0)

            #Grace Notes
            self.grace_note_toggle = tk.Checkbutton(root, text="Grace Notes On/Off", variable=model._grace_note_gui_bool)
            self.grace_note_toggle.grid(row=1,column=0)

            #Tuplet Toggle
            self.tuplet_toggle = tk.Checkbutton(root, text="Tuplets On (see Max)", variable=model._tuplet_gui_bool)
            self.tuplet_toggle.grid(row=2,column=0)

            #Tuplets
            self.max_tuplet_val_label = tk.Label(root, text="Max Tuplets (3)")
            self.max_tuplet_val_label.grid(row=3,column=0)
            self.max_tuplet_val = tk.Entry(root, width=1, textvariable=self.model._tuplet_gui_max)
            self.max_tuplet_val.grid(row=3,column=1)

            #Note multiplier
            self.max_tuplet_val_label = tk.Label(root, text="Note Multiplier")
            self.max_tuplet_val_label.grid(row=4,column=0)
            self.max_tuplet_val_label = tk.Label(root, text="Multiplier Value:")
            self.max_tuplet_val_label.grid(row=5,column=0)
            self.multiper_val = tk.Entry(root, width=3, textvariable=self.model._note_multiplier_gui_val)
            self.multiper_val.grid(row=5,column=1)
            self.max_tuplet_val_label = tk.Label(root, text="Measure Range (Min)")
            self.max_tuplet_val_label.grid(row=6,column=0)
            self.multiper_val_range_min = tk.Entry(root, width=3, textvariable=self.model._note_multiplier_gui_range_min)
            self.multiper_val_range_min.grid(row=6,column=1)
            self.max_tuplet_val_label = tk.Label(root, text="Measure Range (Max)")
            self.max_tuplet_val_label.grid(row=7,column=0)
            self.multiper_val_range_max = tk.Entry(root, width=3, textvariable=self.model._note_multiplier_gui_range_max)
            self.multiper_val_range_max.grid(row=7,column=1)

            #Quit
            output_button = tk.Button(root, text="Write Files", command=write_callback)
            output_button.grid(row=8,column=0)

            #Quit
            quit_button = tk.Button(root, text="Quit Application", command=root.destroy)
            quit_button.grid(row=9,column=0)

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
            self.infile = "./input" #Don't change to keep things sane
            self.outfile = "./output" #ditto to above line
            self.hooks = lh.LejarenHooks()

        def on_submit(self) -> None:
            """
                Pulls files from input directory, loads them into app-wide
                list.

                args: None
                returns: None (adjusts list)
            """
            path = self.infile #local to app directory only
            pattern = r'[\w ]*\.musicxml'
            matching_files = [
                filename for filename in os.listdir(path) 
                if re_search(pattern, filename) and os.path.isfile(os.path.join(path, filename))
            ]
            if matching_files:
                for file in matching_files:
                    self.model._ingested_files.append(file)
                    
            else:
                print("No Files")
            self._load_to_lejaren()

        def _load_to_lejaren(self):
            self.hooks.create_output(self.infile, self.model._ingested_files)

        def write_files(self):
            self.hooks.write_output(self.outfile)

        
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

# app = TemporalTidesLunaApp()
# app.mainloop()