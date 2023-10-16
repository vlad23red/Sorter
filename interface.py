import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class LogSorter(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Log Sorter')
        self.current_menu = None  # текущее всплывающее меню
        self.menus = []

        self.folder_path = tk.StringVar()
        self.save_folder_path = tk.StringVar()

        self.create_ui()

    def create_ui(self):
        # Выбор папки с логами
        folder_lbl = tk.Label(self, text="Выбор папки с логами:")
        folder_lbl.pack(padx=10, pady=5)

        self.folder_path = tk.StringVar()
        folder_entry = tk.Entry(self, textvariable=self.folder_path, width=50)
        folder_entry.pack(padx=10, pady=5)

        folder_btn = tk.Button(self, text="Выбрать папку", command=self.choose_folder)
        folder_btn.pack(padx=10, pady=5)

        # Выбор папки для сохранения
        save_folder_lbl = tk.Label(self, text="Выбор папки для сохранения:")
        save_folder_lbl.pack(padx=10, pady=5)

        self.save_folder_path = tk.StringVar()
        save_folder_entry = tk.Entry(self, textvariable=self.save_folder_path, width=50)
        save_folder_entry.pack(padx=10, pady=5)

        save_folder_btn = tk.Button(self, text="Выбрать папку для сохранения", command=self.choose_save_folder)
        save_folder_btn.pack(padx=10, pady=5)

        # Запрос для поиска в логах
        lbl = tk.Label(self, text="Введите запрос для поиска в логах:")
        lbl.pack(padx=10, pady=5)

        query_entry = tk.Entry(self, width=50)
        query_entry.pack(padx=10, pady=5)

        menus_config = [
            {
                "button_text": "Сортировка папок с логами по содержимому файлов",
                "label_text": "Настройка формата сохранения 1:",
                "entry_width": 50,
                "progressbar_length": 300
            },
            {
                "button_text": "Сортировка папок с логами по названию файлов",
                "label_text": "Настройка формата сохранения 2:",
                "entry_width": 30,
                "progressbar_length": 200
            }
            # ... добавьте другие меню по аналогии
        ]

        for menu in menus_config:
            button = tk.Button(self, text=menu["button_text"], command=lambda m=menu: self.toggle_sort_ui(m))
            button.pack(padx=10, pady=5)

            menu["widgets"] = {
                "label": tk.Label(self, text=menu["label_text"]),
                "entry": tk.Entry(self, width=menu["entry_width"]),
                "progressbar": ttk.Progressbar(self, orient=tk.HORIZONTAL, length=menu["progressbar_length"], mode='determinate'),
                "start_button": tk.Button(self, text="Начать сортировку", command=self.start_sorting)
            }

            self.menus.append(menu)

    def toggle_sort_ui(self, menu):
        if self.current_menu:
            for widget in self.current_menu["widgets"].values():
                widget.pack_forget()

        for widget in menu["widgets"].values():
            widget.pack(padx=10, pady=5)

        self.current_menu = menu

    def start_sorting(self):
        # Здесь ваша логика сортировки
        pass

    def choose_folder(self):
        folder_selected = filedialog.askdirectory()
        self.folder_path.set(folder_selected)

    def choose_save_folder(self):
        folder_selected = filedialog.askdirectory()
        self.save_folder_path.set(folder_selected)

