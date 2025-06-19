from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
import random

class MainApp(MDApp):
    def build(self):
        # Character set for password
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,./;'[]=-1234567890!@#$%^&*(){}|:"
        
        # Ask for password length in console before running GUI
        length = int(input("Enter length: "))
        password = ""
        for _ in range(length):
            password += random.choice(chars)
        
        # Display the password in the KivyMD label
        return MDLabel(
            text=f"Generated Password:\n{password}",
            halign="center",
            theme_text_color="Custom",
            text_color=(0, 0, 0, 1),
            font_style="H5"
        )

if __name__ == '__main__':
    MainApp().run()
