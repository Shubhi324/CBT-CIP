import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email: {self.email}"

class ContactMasterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ContactMaster")
        self.contacts = []

        # GUI elements
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.display_button = tk.Button(root, text="Display All Contacts", command=self.display_contacts)
        self.display_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.contact_listbox = tk.Listbox(root, width=50, height=10)
        self.contact_listbox.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone_number = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()

        if name and phone_number and email:
            contact = Contact(name, phone_number, email)
            self.contacts.append(contact)
            self.contact_listbox.insert(tk.END, str(contact))
            messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

    def delete_contact(self):
        name = self.name_entry.get().strip()
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                self.refresh_contact_listbox()
                messagebox.showinfo("Deleted", f"Contact '{name}' deleted.")
                return
        messagebox.showerror("Error", "Contact not found.")

    def search_contact(self):
        name = self.name_entry.get().strip()
        found_contacts = [str(contact) for contact in self.contacts if name.lower() in contact.name.lower()]

        if found_contacts:
            messagebox.showinfo("Contacts Found", "\n".join(found_contacts))
        else:
            messagebox.showwarning("No Results", "No contacts found.")

    def display_contacts(self):
        if self.contacts:
            self.refresh_contact_listbox()
        else:
            messagebox.showinfo("Contact List", "No contacts to display.")

    def refresh_contact_listbox(self):
        self.contact_listbox.delete(0, tk.END)  # Clear the listbox
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, str(contact))  # Add updated contacts

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactMasterApp(root)
    root.mainloop()
