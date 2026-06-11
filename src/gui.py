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

    def on_submit(result_container):
        # Perform your operational check
        if isinstance(entry.get(), str):
            if re_search(r'*\.musicxml', entry.get()):
                result_container["success"] = True
                result_container["msg"] = "Actual Music XML File"
                root.destroy() # Close GUI upon success
        else:
            result_container["success"] = False
            result_container["msg"] = "Not String"
            # Keep GUI open for another attempt

    def check_result(self, state):

        global entry
        entry = tk.Entry(root)
        entry.pack()
        
        # Pass a mutable dict into the lambda
        btn = tk.Button(root, text="Submit", command=lambda: self.on_submit(state))
        btn.pack()
        
        root.mainloop()
        return state

