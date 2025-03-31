import sys
import os
import customtkinter as ctk
import importlib
from pathlib import Path

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Настройки окна
        self.title("PC Tools v1.0.1")
        self.geometry("600x400")
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # Загрузка модулей
        self.load_tools()

    def load_tools(self):
        modules = []
        # Ищем все .py файлы в папке tools (кроме __init__.py)
        for file in Path("tools").glob("*.py"):
            if file.name == "__init__.py":
                continue
            module_name = file.stem
            try:
                module = importlib.import_module(f"tools.{module_name}")
                modules.append(module.setup_tool)
            except Exception as e:
                print(f"Ошибка: {e}")

        # Создаём кнопки для каждого модуля
        for tool in modules:
            button = tool(self)
            button.pack(pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()