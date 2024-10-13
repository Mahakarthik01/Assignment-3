#python -m venv .venv #Starting a virtual environment
#.\.venv\Scripts\Activate to activate the virtual environment
import tkinter as tk
from tkinter import ttk  # For nicer dropdown menus
from googletrans import Translator  # Install with pip: pip install googletrans==4.0.0-rc1


# Base class for Tkinter GUI
class BaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translation App")

    # A method to start the GUI loop
    def start(self):
        self.root.mainloop()


# Translator class that uses Google API - separate class for logic
class TranslationService:
    def __init__(self):
        self.translator = Translator()

    # This method performs the actual translation
    def translate(self, text, src_lang, target_lang):
        try:
            translation = self.translator.translate(text, src=src_lang, dest=target_lang)
            return translation.text
        except Exception as e:
            return f"Error: {str(e)}"


# Multiple inheritance - combining GUI and logic handling
class TranslationApp(BaseApp, TranslationService):
    def __init__(self, root):
        BaseApp.__init__(self, root)  # Inheriting BaseApp's Tkinter setup
        TranslationService.__init__(self)  # Inheriting TranslationService for API
        self.create_widgets()

    # Encapsulation: keeping all widget creation inside the class
    def create_widgets(self):
        # Input Textbox
        self.input_label = tk.Label(self.root, text="Enter text to translate:")
        self.input_label.pack()
        self.input_text = tk.Text(self.root, height=10, width=50)
        self.input_text.pack()

        # Dropdown for source language
        self.src_lang_label = tk.Label(self.root, text="Source language (e.g., 'en' for English):")
        self.src_lang_label.pack()
        self.src_lang_entry = tk.Entry(self.root)
        self.src_lang_entry.pack()

        # Dropdown for target language
        self.target_lang_label = tk.Label(self.root, text="Target language (e.g., 'fr' for French):")
        self.target_lang_label.pack()
        self.target_lang_entry = tk.Entry(self.root)
        self.target_lang_entry.pack()

        # Button to trigger translation
        self.translate_button = tk.Button(self.root, text="Translate", command=self.on_translate_click)
        self.translate_button.pack()

        # Output Textbox
        self.output_label = tk.Label(self.root, text="Translated text:")
        self.output_label.pack()
        self.output_text = tk.Text(self.root, height=10, width=50)
        self.output_text.pack()

    # This method gets called when the "Translate" button is clicked
    def on_translate_click(self):
        # Polymorphism: translating different types of text based on user input
        text = self.input_text.get("1.0", tk.END).strip()  # Get the input text
        src_lang = self.src_lang_entry.get().strip()  # Get source language
        target_lang = self.target_lang_entry.get().strip()  # Get target language

        # Calling the translate method from TranslationService
        translation = self.translate(text, src_lang, target_lang)

        # Clear the output box and display the translation
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, translation)


# Decorator to log function calls (Extra feature for assignment)
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} was called.")
        return func(*args, **kwargs)
    return wrapper


# Child class that overrides the translation method to add logging (Method Overriding)
class LoggedTranslationApp(TranslationApp):
    # Overriding the translate method to add logging functionality
    @log_function_call  # Using a decorator to log translation requests
    def translate(self, text, src_lang, target_lang):
        return super().translate(text, src_lang, target_lang)


# Entry point for running the application
if __name__ == "__main__":
    root = tk.Tk()  # Tkinter root window

    # Using the child class with method overriding and logging
    app = LoggedTranslationApp(root)

    # Start the application
    app.start()
