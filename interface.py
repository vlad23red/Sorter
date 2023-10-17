import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import functools


class LogSorter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Log Sorter')
        self.menus = []

        self.folder_path = tk.StringVar()
        self.save_folder_path = tk.StringVar()

        self.canvas = tk.Canvas(self)
        self.scrollbar = ttk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.canvas.config(xscrollcommand=self.scrollbar.set)
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
        lbl.pack(padx=100, pady=5)

        query_entry = tk.Entry(self, width=50)
        query_entry.pack(padx=10, pady=5)

        menus_config = [
            {
                "button_text": "Сортировка папок с логами по содержимому файлов",
                "label_text": "Настройка формата сохранения 1:",
                "entry_width": 50,
                "progressbar_length": 300,
                "is_expanded": False
            },
            {
                "button_text": "Сортировка папок с логами по названию файлов",
                "label_text": "Настройка формата сохранения 2:",
                "entry_width": 30,
                "progressbar_length": 200,
                "is_expanded": False
            },
            {
                "button_text": "Сортировка папок с логами по названию папок",
                "label_text": "Настройка формата сохранения 2:",
                "entry_width": 30,
                "progressbar_length": 200,
                "is_expanded": False
            },
            {
                "button_text": "Сортировка папок с логами по датам файлов.",
                "label_text": "Настройка формата сохранения 2:",
                "entry_width": 30,
                "progressbar_length": 200,
                "is_expanded": False
            },
            {
                "button_text": "Сортировка файлов и логов по содержимому файлов",
                "label_text": "Настройка формата сохранения 2:",
                "entry_width": 30,
                "progressbar_length": 200,
                "is_expanded": False
            },
            {
                "button_text": "Сортировка файлов и логов по названию файлов",
                "label_text": "Настройка формата сохранения 2:",
                "entry_width": 30,
                "progressbar_length": 200,
                "is_expanded": False
            },
            {
                "button_text": " Сортировка папок из логов по названию папок",
                "label_text": "Настройка формата сохранения 2:",
                "entry_width": 30,
                "progressbar_length": 200,
                "is_expanded": False
            },
            {
                "button_text": "Сортировка паролей из логов",
                "label_text": "Настройка формата сохранения 2:",
                "entry_width": 30,
                "progressbar_length": 200,
                "is_expanded": False
            },
            {
                "button_text": "Нормализатор паролей из логов",
                "label_text": "Настройка формата сохранения 2:",
                "entry_width": 30,
                "progressbar_length": 200,
                "is_expanded": False
            },
            {
                "button_text": "Нормализатор почт (mail:pass) из логов",
                "label_text": "Настройка формата сохранения 2:",
                "entry_width": 30,
                "progressbar_length": 200,
                "is_expanded": False
            },
            {
                "button_text": "Сортировка куков из логов",
                "label_text": "Настройка формата сохранения 2:",
                "entry_width": 30,
                "progressbar_length": 200,
                "is_expanded": False
            },
            {
                "button_text": "Сортировка строк в файлах из логов",
                "label_text": "Настройка формата сохранения 2:",
                "entry_width": 30,
                "progressbar_length": 200,
                "is_expanded": False
            },
            {
                "button_text": "Сортировка папок с логами по названию файлов",
                "label_text": "Настройка формата сохранения 2:",
                "entry_width": 30,
                "progressbar_length": 200,
                "is_expanded": False
            },
            {
                "button_text": "Экстрактор ссылок из логов с паролями",
                "label_text": "Настройка формата сохранения 2:",
                "entry_width": 30,
                "progressbar_length": 200,
                "is_expanded": False
            },
            {
                "button_text": "Очистка логов от файлов по расширению (.exe ...)",
                "label_text": "Настройка формата сохранения 2:",
                "entry_width": 30,
                "progressbar_length": 200,
                "is_expanded": False
            }

        ]

        # Упаковка canvas и scrollbar перед циклом
        self.canvas.pack(side="top", fill="both", expand=True, padx=10, pady=10)
        self.scrollbar.pack(side="bottom", fill="x")

        # Привязка движения канваса к скроллбару
        self.canvas.config(xscrollcommand=self.scrollbar.set)
        # Привязка движения скроллбара к канвасу
        self.scrollbar.config(command=self.canvas.xview)

        # Основной frame, который будет содержать все ваши меню
        content_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=content_frame, anchor="nw")

        x_position = 0
        for menu in menus_config:
            frame = tk.Frame(content_frame)
            button = tk.Button(frame, text=menu["button_text"],
                               command=functools.partial(self.show_sort_ui, menu, frame))

            button.grid(row=0, column=0, padx=10, pady=5)

            menu["frame"] = frame
            self.menus.append(menu)
            frame.grid(row=0, column=x_position, padx=10, pady=5)
            x_position += 1

            # Обновление области прокрутки после добавления всех виджетов
            content_frame.update_idletasks()
            self.canvas.config(scrollregion=self.canvas.bbox("all"))

            self.bind("<Configure>", self.update_scrollregion)
        x_position += 1

    def show_sort_ui(self, menu, frame):
        # Collapse all other menus
        for m in self.menus:
            for widget in m["frame"].winfo_children():
                if widget != m["frame"].winfo_children()[0]:  # This will ensure the button remains
                    widget.grid_forget()
            m["is_expanded"] = False

        # Expand the clicked menu
        if not menu["is_expanded"]:
            label = tk.Label(frame, text=menu["label_text"])
            label.grid(row=1, column=0, padx=10, pady=5)

            entry = tk.Entry(frame, width=menu["entry_width"])
            entry.grid(row=2, column=0, padx=10, pady=5)

            progressbar = ttk.Progressbar(frame, orient=tk.HORIZONTAL, length=menu["progressbar_length"],
                                          mode='determinate')
            progressbar.grid(row=3, column=0, padx=10, pady=5)

            start_button = tk.Button(frame, text="Начать сортировку", command=self.start_sorting)
            start_button.grid(row=4, column=0, padx=10, pady=5)

            menu["is_expanded"] = True
    def start_sorting(self):
        # Your sorting logic here
        pass


    def choose_folder(self):
        folder_selected = filedialog.askdirectory()
        self.folder_path.set(folder_selected)

    def choose_save_folder(self):
        folder_selected = filedialog.askdirectory()
        self.save_folder_path.set(folder_selected)

    def update_scrollregion(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


