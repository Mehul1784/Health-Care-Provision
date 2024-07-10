import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import pickle
import numpy as np

with open('disease_model.pkl', 'rb') as file:
    model = pickle.load(file)
with open('label_encoder.pkl', 'rb') as file:
    label_encoder = pickle.load(file)

disease_precautions = {
    "Diabetes": "Monitor blood sugar levels, maintain a healthy diet, exercise regularly.",
    "Heart Problems": "Avoid smoking, maintain a healthy weight, get regular exercise.",
    "Respiratory Ailments": "Avoid smoking, stay away from pollutants, get vaccinated against flu.",
    "Cancer": "Avoid tobacco, maintain a healthy diet, get regular screenings.",
    "Depression": "Stay connected with loved ones, maintain a regular routine, avoid alcohol and drugs.",
    "Alzheimer's": "Stay mentally active, get regular physical exercise, maintain a healthy diet."
}

disease_remedies = {
    "Diabetes": "Stay hydrated, eat high-fiber foods, manage stress effectively.",
    "Heart Problems": "Eat a heart-healthy diet, manage stress, take medications as prescribed.",
    "Respiratory Ailments": "Use a humidifier, practice breathing exercises, take prescribed medications.",
    "Cancer": "Stay hydrated, manage stress, follow prescribed treatment plans.",
    "Depression": "Engage in physical activity, practice mindfulness, seek professional help if needed.",
    "Alzheimer's": "Engage in social activities, establish a routine, take prescribed medications."
}

def get_user_details():
    name = name_entry.get()
    age = int(age_entry.get())
    contact_no = contact_entry.get()
    gender = gender_var.get()
    return name, age, contact_no, gender

def get_disease():
    disease = disease_var.get()
    return disease

def submit_form():
    name, age, contact_no, gender = get_user_details()
    disease = get_disease()

    if not name or not age or not contact_no or not gender or not disease:
        messagebox.showerror("Error", "All fields are required.")
        return

    precautions = disease_precautions[disease]
    remedies = disease_remedies[disease]

    # Modify solutions based on age (example logic)
    if age < 18:
        solutions = "As a minor, ensure to follow these remedies under parental guidance."
    elif 18 <= age <= 60:
        solutions = "Maintain a balanced lifestyle with these remedies."
    else:
        solutions = "As a senior, regular checkups and adhering to these remedies are crucial."

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"Disease: {disease}\n")
    result_text.insert(tk.END, f"Precautions: {precautions}\n")
    result_text.insert(tk.END, f"Remedies: {remedies}\n")
    result_text.insert(tk.END, f"Additional Advice: {solutions}\n")

    save_to_excel(name, contact_no, gender, disease)
    messagebox.showinfo("Success", f"{name}'s contact details have been saved for further assistance by NGOs or regional healthcare providers.")

def save_to_excel(name, contact_no, gender, disease):
    df = pd.DataFrame([[contact_no, name, gender, disease]], columns=["Contact Number", "Name", "Gender", "Disease Suffering"])
    try:
        existing_data = pd.read_excel("user_data.xlsx")
        df = pd.concat([existing_data, df], ignore_index=True)
    except FileNotFoundError:
        pass
    df.to_excel("user_data.xlsx", index=False)

root = tk.Tk()
root.title("Health Advisor")
root.geometry("500x600")

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Age:").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Label(root, text="Contact Number:").pack()
contact_entry = tk.Entry(root)
contact_entry.pack()

tk.Label(root, text="Gender:").pack()
gender_var = tk.StringVar(value="M")
tk.Radiobutton(root, text="Male", variable=gender_var, value="M").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="F").pack()

tk.Label(root, text="Disease:").pack()
disease_var = tk.StringVar()
disease_menu = ttk.Combobox(root, textvariable=disease_var)
disease_menu['values'] = list(disease_precautions.keys())
disease_menu.pack()

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack()

result_text = tk.Text(root, height=10, wrap=tk.WORD)
result_text.pack()

funding_label = tk.Label(root, text="Funding for this initiative is provided by government trusts, elderly care NGOs, and other similar organizations.", wraplength=450, justify="center")
funding_label.pack()

root.mainloop()