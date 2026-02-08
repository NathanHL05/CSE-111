import tkinter as tk
from tkinter import ttk
"""
This program is a simple circuit analysis tool
This tool will ask for a given variable, current or voltage,
then will ask for information of the pieces of the circuit, whether they are parallel or series, and the 
resistances
with this it will calculate the current, voltage, and resistance on each section and of the total circuit
"""

# make window
root = tk.Tk()         
root.title("Simple Circuit Analysis")
root.geometry("600x600")  

# made scroll for it gets too big
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

canvas = tk.Canvas(main_frame)
scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

def _on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", _on_frame_configure)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

#calculation functions
def get_total_voltage(current, total_resistance):
    voltage = total_resistance * current
    return voltage

def get_current(voltage, resistance):
    return voltage / resistance

def get_parallel_res(resistances):
    inv_sum = 0.0
    for r in resistances:
        inv_sum += 1.0 / r
    return (1.0 / inv_sum) 

def series_res(resistances):
    return sum(resistances)

# voltage/current given variable
IV_label = tk.Label(scrollable_frame, text="Is voltage or current given for your circuit?")
IV_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

IV_options = ["Voltage", "Current"]
IV_dropdown = ttk.Combobox(scrollable_frame, values=IV_options, state="readonly")
IV_dropdown.grid(row=1, column=0, padx=5, pady=5, sticky="w")
IV_dropdown.set("Voltage")

given_label = tk.Label(scrollable_frame, text="Enter voltage on circuit:")
given_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

circuit_value = tk.Entry(scrollable_frame)
circuit_value.grid(row=2, column=1, padx=5, pady=5, sticky="w")

def on_IV_change(event=None):
    val = IV_dropdown.get()
    if val == "Voltage":
        given_label.config(text="Enter voltage on circuit:")
    else:
        given_label.config(text="Enter current on circuit:")

IV_dropdown.bind('<<ComboboxSelected>>', on_IV_change)

# get sections in the circuit
sections_label = tk.Label(scrollable_frame, text="How many sections are in the circuit?(pieces of series/parallel combinations)")
sections_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="w")

sections_dropdown = ttk.Combobox(scrollable_frame, values=[str(i) for i in range(1, 6)], state="readonly")
sections_dropdown.grid(row=4, column=0, padx=5, pady=5, sticky="w")
sections_dropdown.set("1")

sections_frame = tk.Frame(scrollable_frame)
sections_frame.grid(row=6, column=0, columnspan=3, padx=5, pady=10, sticky="w")

#   record the sections w/ info to save results for calculations
section_records = []

def create_sections():
    # Clear previous 
    for widget in sections_frame.winfo_children():
        widget.destroy()
    section_records.clear()

    try:
        num_sections = int(sections_dropdown.get())
    except ValueError:
        return

    for i in range(num_sections):
        row_base = i * 3

        section_label = tk.Label(sections_frame, text=f"Section {i+1}:")
        section_label.grid(row=row_base, column=0, sticky="w", padx=5, pady=5)
        #which type of circuit
        type_dropdown = ttk.Combobox(sections_frame, values=["Series", "Parallel"], state="readonly")
        type_dropdown.grid(row=row_base, column=1, padx=5, pady=5, sticky="w")
        type_dropdown.set("Series")

        resist_frame = tk.Frame(sections_frame)
        resist_frame.grid(row=row_base+1, column=0, columnspan=3, padx=5, pady=5, sticky="w")

        result_label = tk.Label(sections_frame, text="Results: ")
        result_label.grid(row=row_base, column=2, padx=10, pady=5, sticky="w")

        record = {
            "type_cb": type_dropdown,
            "container": resist_frame,
            "branch_entries": [],
            "single_entry": None,
            "result_label": result_label
        }
        section_records.append(record)

        def render_fields(event=None, rec=record):
            # Clear container
            for w in rec["container"].winfo_children():
                w.destroy()
            rec["branch_entries"].clear()
            rec["single_entry"] = None

            if rec["type_cb"].get() == "Series":
                tk.Label(rec["container"], text="Resistance (Ω):").grid(row=0, column=0, padx=5, pady=5, sticky="w")
                entry = tk.Entry(rec["container"])
                entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
                rec["single_entry"] = entry
            else:
                tk.Label(rec["container"], text="Number of branches:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
                branches_entry = tk.Entry(rec["container"], width=10)
                branches_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

                def create_branches():
                    # Remove any previous branches 
                    for w in rec["container"].grid_slaves():
                        if int(w.grid_info().get("row", 0)) >= 1:
                            w.destroy()
                    rec["branch_entries"].clear()

                    try:
                        nb = int(branches_entry.get())
                        if nb <= 0:
                            return
                    except ValueError:
                        return

                    for b in range(nb):
                        tk.Label(rec["container"], text=f"Branch {b+1} Resistance (Ω):").grid(row=b+1, column=0, padx=5, pady=5, sticky="w")
                        entry = tk.Entry(rec["container"])
                        entry.grid(row=b+1, column=1, padx=5, pady=5, sticky="w")
                        rec["branch_entries"].append(entry)

                tk.Button(rec["container"], text="Set Branches", command=create_branches).grid(row=0, column=2, padx=5, pady=5, sticky="w")

        type_dropdown.bind('<<ComboboxSelected>>', render_fields)
        render_fields()

def calculate():
    
    try:
        given_val =float(circuit_value.get())
    except ValueError:
        # highlight error
        circuit_value.configure(bg="#ffdddd")
        return
    else:
        circuit_value.configure(bg="white")

    # make list of resistances of each section
    section_R = []
    for rec in section_records:
        stype = rec["type_cb"].get()
        try:
            if stype == "Series":
                if rec["single_entry"] is None:
                    raise ValueError("Missing series resistance")
                r = float(rec["single_entry"].get())
                if r < 0:
                    raise ValueError("Negative resistance")
                R_eq = series_res([r])
            else:
                if not rec["branch_entries"]:
                    raise ValueError("Set branches for parallel section")
                branch_values = [float(e.get()) for e in rec["branch_entries"]]
                if any(r <= 0 for r in branch_values):
                    raise ValueError("Branch resistances must be positive")
                R_eq = get_parallel_res(branch_values)
        except ValueError:
            # mark with red
            rec["container"].configure(bg="#ffdddd")
            return
        else:
            rec["container"].configure(bg="white")
            section_R.append(R_eq)

    total_R = series_res(section_R)

    # totalt current/ voltage
    if total_R == 0:
        total_I = 0.0
        total_V = 0.0
    else:
        if IV_dropdown.get() == "Voltage":
            total_V = given_val
            total_I = get_current(total_V, total_R)
        else:
            total_I = given_val
            total_V= get_total_voltage(total_I, total_R)
           

    # results for each section
    for idx, rec in enumerate(section_records):
        R = section_R[idx]
        I_section = total_I  
        Vdrop = I_section * R
        rec["result_label"].config(text=f"Results: R={R:.4g} Ω | I={I_section:.4g} A | Vdrop={Vdrop:.4g} V")

    # totals
    if not hasattr(calculate, "_total_label"):
        calculate._total_label = tk.Label(scrollable_frame)
        calculate._total_label.grid(row=1, column=1, padx=10, pady=0, sticky="e")
    calculate._total_label.config(
        text=f"Total Circuit → R={total_R:.4g} Ω | I={total_I:.4g} A | V={total_V:.4g} V"
    )

tk.Button(scrollable_frame, text="Create Sections", command=create_sections).grid(row=5, column=0, padx=5, pady=10, sticky="w")
tk.Button(scrollable_frame, text="Calculate", command=calculate).grid(row=0, column=1, padx=5, pady=10, sticky="w")


create_sections()
on_IV_change()

root.mainloop()