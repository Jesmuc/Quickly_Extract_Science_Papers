import tkinter as tk
from tkinter import messagebox

def save_to_file():
    try:
        num_inputs = int(entry.get())
        if num_inputs <= 0:
            messagebox.showerror("Error", "Please enter a valid number greater than 0.")
            return

        file_path = "input_data.txt"
        with open(file_path, "w") as file:
            for i in range(num_inputs):
                data = entry_list[i].get()
                file.write(data + "\n")

        messagebox.showinfo("Success", f"{num_inputs} inputs saved to {file_path}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def create_input_fields():
    try:
        num_inputs = int(entry.get())
        if num_inputs <= 0:
            messagebox.showerror("Error", "Please enter a valid number greater than 0.")
            return

        # Clear existing input fields
        for widget in input_frame.winfo_children():
            widget.destroy()

        entry_list.clear()

        # Create new input fields
        for i in range(num_inputs):
            input_label = tk.Label(input_frame, text=f"Input {i + 1}:")
            input_label.grid(row=i, column=0, padx=10, pady=5)
            entry_list.append(tk.Entry(input_frame))
            entry_list[i].grid(row=i, column=1, padx=10, pady=5)

        save_button.grid(row=num_inputs + 1, column=0, columnspan=2, padx=10, pady=10)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

root = tk.Tk()
root.title("Text Input and Save")

num_inputs_label = tk.Label(root, text="Enter the number of inputs:")
num_inputs_label.grid(row=0, column=0, padx=10, pady=5)

entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=5)

create_button = tk.Button(root, text="Create Input Fields", command=create_input_fields)
create_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

input_frame = tk.Frame(root)
input_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

save_button = tk.Button(root, text="Save to File", command=save_to_file)

entry_list = []

root.mainloop()