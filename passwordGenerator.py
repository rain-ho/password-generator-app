import customtkinter
import webbrowser
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1020x550")
        self.root.title("Password Generator")

        self.frame = customtkinter.CTkFrame(master=root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.password = ""
        self.password_size = 4
        self.darkMode = "dark"
        self.colorMode = "dark-blue"
        self.create_gui()

    def create_gui(self):

        self.lightMode(self.darkMode, self.colorMode)
        # customtkinter.set_appearance_mode("dark")
        # customtkinter.set_default_color_theme("dark-blue")

        label = customtkinter.CTkLabel(master=self.frame, text="PASSWORD GENERATOR", font=("Roboto", 20))
        label.pack(pady=12, padx=10)

        self.upperCase = customtkinter.StringVar(value=0)
        self.lowerCase = customtkinter.StringVar(value=0)
        self.numbers = customtkinter.StringVar(value=0)
        self.specials = customtkinter.StringVar(value=0)

        checkboxes = [
            ("INCLUDE UPPERCASE LETTERS", self.upperCase),
            ("INCLUDE LOWERCASE LETTERS", self.lowerCase),
            ("INCLUDE NUMBERS", self.numbers),
            ("INCLUDE SPECIAL CHARACTERS", self.specials)
        ]

        for text, var in checkboxes:
            checkbox = customtkinter.CTkCheckBox(master=self.frame, text=text, command=self.generate_password, variable=var, onvalue=1, offvalue=0)
            checkbox.pack(pady=15, padx=50)

        self.password_size_label = customtkinter.CTkLabel(master=self.frame, text=f"Password Size = {self.password_size}", font=("Roboto", 15))
        self.password_size_label.pack()

        self.slider = customtkinter.CTkSlider(master=self.frame, from_=4, to=100, command=self.slider_value)
        self.slider.pack(pady=15, padx=50)

        self.password_label = customtkinter.CTkLabel(master=self.frame, text=self.password, font=("Roboto", 15))
        self.password_label.pack()

        self.copy_button = customtkinter.CTkButton(master=self.frame, text="Copy Password", command=self.copy_password)
        self.copy_button.pack(pady=15, padx=50)

        self.lightModeButton = customtkinter.CTkButton(master=self.frame, text="Light Mode", command=self.toggleMode)
        self.lightModeButton.pack(pady=15, padx=50)

        developed_by_label = customtkinter.CTkLabel(master=self.frame, text="Developed by Rainho\ngithub.com/rain-ho", font=("Roboto", 12), cursor="hand2")
        developed_by_label.pack(side="bottom", pady=20)
        developed_by_label.bind("<Button-1>", self.open_github)
    
    def toggleMode(self):
        if self.darkMode == "dark":
            self.darkMode = "light"
            self.colorMode = "green"
            
        else:
            self.darkMode = "dark"
            self.colorMode = "dark-blue"
        self.lightMode(self.darkMode, self.colorMode)

    def lightMode(self, mode, color):
        customtkinter.set_appearance_mode(mode)
        customtkinter.set_default_color_theme(color)

    def getValues(self):
        uppercase = int(self.upperCase.get())
        lowercase = int(self.lowerCase.get())
        nums = int(self.numbers.get())
        special = int(self.specials.get())
        return uppercase, lowercase, nums, special

    def generate_password(self):
        include_lower = bool(int(self.lowerCase.get()))
        include_upper = bool(int(self.upperCase.get()))
        include_digits = bool(int(self.numbers.get()))
        include_specials = bool(int(self.specials.get()))

        size = self.slider.get()
        self.password_size = int(size)

        characters = ""
        if include_lower:
            characters += string.ascii_lowercase
        if include_upper:
            characters += string.ascii_uppercase
        if include_digits:
            characters += string.digits
        if include_specials:
            characters += string.punctuation

        if not characters:
            self.password = "Please select at least one character set."
        else:
            self.password = ''.join(random.choice(characters) for _ in range(int(size)))

        self.password_size_label.configure(text=f"Password Size = {self.password_size}")
        self.password_label.configure(text=self.password)

    def slider_value(self, value):
        self.generate_password()

    def copy_password(self):
        pyperclip.copy(self.password)

    def open_github(self, event):
        github_url = "https://github.com/rain-ho"
        webbrowser.open_new(github_url)

def main():
    root = customtkinter.CTk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
