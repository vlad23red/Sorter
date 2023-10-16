import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class LogSorter(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Log Sorter')
        self.widgets_visible = False  # флаг видимости виджетов
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

        # Кнопка сортировки
        sort_btn = tk.Button(self, text="Сортировка папок с логами по содержимому файлов", command=self.toggle_sort_ui)
        sort_btn.pack(padx=10, pady=10)

        # Настройка формата сохранения
        self.format_lbl = tk.Label(self, text="Настройка формата сохранения:")
        self.format_entry = tk.Entry(self, width=50)

        # Прогрессбар
        self.progress = ttk.Progressbar(self, orient=tk.HORIZONTAL, length=300, mode='determinate')

        # Кнопка начала сортировки
        def start_sorting():
            pass  # Ваша логика сортировки

        self.start_sort_btn = tk.Button(self, text="Начать сортировку", command=start_sorting)

    def toggle_sort_ui(self):
        if self.widgets_visible:
            self.format_lbl.pack_forget()
            self.format_entry.pack_forget()
            self.progress.pack_forget()
            self.start_sort_btn.pack_forget()
        else:
            self.format_lbl.pack(padx=10, pady=5)
            self.format_entry.pack(padx=10, pady=5)
            self.progress.pack(padx=10, pady=10)
            self.start_sort_btn.pack(padx=10, pady=10)

        self.widgets_visible = not self.widgets_visible

    def choose_folder(self):
        folder_selected = filedialog.askdirectory()
        self.folder_path.set(folder_selected)

    def choose_save_folder(self):
        folder_selected = filedialog.askdirectory()
        self.save_folder_path.set(folder_selected)


