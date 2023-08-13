import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os
import shutil

def open_input_ui():
    input_window = tk.Toplevel(root)
    input_window.title("Input Window")

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

    def save_to_file():
        try:
            file_path = "input_data.txt"
            with open(file_path, "w") as file:
                for entry in entry_list:
                    data = entry.get()
                    file.write(data + "\n")

            messagebox.showinfo("Success", f"{len(entry_list)} inputs saved to {file_path}")
            input_window.destroy()  # Close the input window after saving
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    num_inputs_label = tk.Label(input_window, text="Enter the number of inputs:")
    num_inputs_label.grid(row=0, column=0, padx=10, pady=5)

    entry = tk.Entry(input_window)
    entry.grid(row=0, column=1, padx=10, pady=5)

    create_button = tk.Button(input_window, text="Create Input Fields", command=create_input_fields)
    create_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    input_frame = tk.Frame(input_window)
    input_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    save_button = tk.Button(input_window, text="Save to File", command=save_to_file)

    entry_list = []

def run_script(script_name):
    try:
        script_path = os.path.join(os.path.dirname(__file__), script_name)
        subprocess.run(["python", script_path], check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred while running the script: {e}")
    except FileNotFoundError:
        messagebox.showerror("Error", f"Script not found: {script_name}")

def copy_file_to_input_folder():
    try:
        # Prompt the user to select a file
        file_path = filedialog.askopenfilename()
        if not file_path:
            return

        # Determine the destination folder (input folder in the root directory)
        destination_folder = os.path.join(os.path.dirname(__file__), "input")

        # Make sure the destination folder exists
        os.makedirs(destination_folder, exist_ok=True)

        # Copy the selected file to the destination folder
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.copy(file_path, destination_path)

        messagebox.showinfo("Success", f"File '{file_name}' copied to the input folder.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

root = tk.Tk()
root.title("Extract Papers")

# Add a button to copy a file to the input folder
copy_file_button = tk.Button(root, text="Select Paper File", command=copy_file_to_input_folder)
copy_file_button.pack(pady=5)

add_input_button = tk.Button(root, text="Add new prompts for reports (Optional)", command=open_input_ui)
add_input_button.pack(pady=20)

run_chat_button = tk.Button(root, text="Start chat", command=lambda: run_script("chat.py"))
run_chat_button.pack(pady=5)

run_generate_reports_button = tk.Button(root, text="Create report", command=lambda: run_script("generate_multiple_reports.py"))
run_generate_reports_button.pack(pady=5)

run_render_report_button = tk.Button(root, text="Save html report", command=lambda: run_script("render_report.py"))
run_render_report_button.pack(pady=5)

root.mainloop()