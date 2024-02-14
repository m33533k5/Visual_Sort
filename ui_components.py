import tkinter
from tkinter import ttk

import constants
from controller import Controller
from translation import Translations
from data.import_data import ImportData
from data.export_data import ExportData


class UIBase(type):
    """
    Initialisiert alle wesentlichen UI-Elemente der Anwendung.

    canvas: Das Canvas-Widget für die Zeichnungen und Visualisierungen.
    window: Das Hauptfenster der Anwendung.
    label_algorithm: Label für die Anzeige des Algorithmusnamens.
    algo_menu: Dropdown-Menü zur Auswahl des Sortieralgorithmus.
    label_speed: Label für die Anzeige der Geschwindigkeitseinstellung.
    speed_menu: Dropdown-Menü zur Auswahl der Visualisierungsgeschwindigkeit.
    label_size: Label für die Anzeige der Größeneinstellung des Arrays.
    size_entry: Eingabefeld für die Größe des zu sortierenden Arrays.
    label_steps: Label für die Anzeige der Anzahl der Sortierschritte.
    size_steps: Eingabefeld/Anzeigefeld für die Anzahl der Schritte während des Sortierprozesses.
    label_ranking: Label für die Anzeige der Rangordnungsinformation.
    text_ranking: Textfeld für detaillierte Rangordnungsinformationen.
    button_generate: Button zum Generieren eines neuen Arrays.
    button_sort: Button zum Starten des Sortierprozesses.
    button_german_translation: Button zur Anwendung der deutschen Sprache in der UI.
    button_english_translation: Button zur Anwendung der englischen Sprache in der UI.
    """

    instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls.instances:
            instance = super().__call__(*args, **kwargs)
            cls.instances[cls] = instance
        return cls.instances[cls]


class UIComponents(metaclass=UIBase):
    window = tkinter.Tk()
    canvas = tkinter.Canvas(window, width=800, height=425,
                            bg=constants.YELLOW)  # Zeichenfläche für die Visualisierung
    ui_frame = tkinter.Frame(window, width=400, height=425, bg=constants.PINK)

    speed_menu = None
    label_algorithm = tkinter.Label(ui_frame)
    algo_menu = None
    label_speed = tkinter.Label(ui_frame)
    label_size = tkinter.Label(ui_frame)
    size_entry = None
    label_steps = tkinter.Label(ui_frame)
    size_steps = None
    label_ranking = tkinter.Label(ui_frame)
    text_ranking = tkinter.Text(ui_frame, height=10, width=35)
    button_generate = None
    button_sort = None
    button_german_translation = None
    button_english_translation = None
    button_import = None
    button_export = None

    def setup_gui(self, speed_name, speed_list, algorithm_name, algo_names, steps, ranking, algo_list, array_size):
        controller = Controller()
        translation = Translations()
        export_data = ExportData()
        import_data = ImportData()

        # Hauptfenster-Einstellungen
        self.window.config(bg=constants.LIGHT_GREEN)  # Hintergrundfarbe des Hauptfensters

        # Einrichtung der Benutzeroberfläche
        self.canvas.grid(row=0, column=0, padx=10, pady=5)

        # UI-Frame für Steuerelemente und Informationen
        self.ui_frame.grid(row=0, column=1, padx=10, pady=5)

        # Konfiguration der Dropdown-Menüs für Algorithmusauswahl und Geschwindigkeit
        self.speed_menu = ttk.Combobox(self.ui_frame, textvariable=speed_name, values=speed_list)
        self.speed_menu.place(x=220, y=45, width=150, height=25)
        self.speed_menu.current(0)  # Standardauswahl

        # UI-Komponenten für die Anzeige und Interaktion
        self.algo_menu = ttk.Combobox(self.ui_frame, textvariable=algorithm_name, values=algo_names)
        self.algo_menu.place(x=220, y=10, width=150, height=25)
        self.algo_menu.current(4)

        self.label_algorithm.place(x=10, y=10, width=150, height=25)
        self.label_speed.place(x=10, y=45, width=150, height=25)
        self.label_size.place(x=10, y=80, width=150, height=25)
        self.label_steps.place(x=10, y=115, width=150, height=25)
        self.label_ranking.place(x=10, y=190, width=150, height=25)

        self.button_generate = tkinter.Button(self.ui_frame,
                                              command=lambda: controller.generate(self.canvas, self.window, array_size))
        self.button_generate.place(x=10, y=155, width=100, height=30)
        self.button_sort = tkinter.Button(self.ui_frame,
                                          command=lambda: controller.sort(self, steps, ranking, algo_list))
        self.button_sort.place(x=120, y=155, width=100, height=30)
        self.button_german_translation = tkinter.Button(self.ui_frame,
                                                        command=lambda: translation.set_language(constants.LANGUAGE_DE,
                                                                                                 self))
        self.button_german_translation.place(x=270, y=155, width=100, height=30)
        self.button_english_translation = tkinter.Button(self.ui_frame,
                                                         command=lambda: translation.set_language(constants.LANGUAGE_EN,
                                                                                                  self))
        self.button_english_translation.place(x=270, y=190, width=100, height=30)

        self.size_entry = tkinter.Entry(self.ui_frame, textvariable=array_size)
        self.size_entry.place(x=220, y=80, width=150, height=25)
        self.size_steps = tkinter.Entry(self.ui_frame, textvariable=steps, state=constants.STATE_READONLY)
        self.size_steps.place(x=220, y=115, width=150, height=25)
        self.text_ranking.place(x=10, y=225, width=360, height=150)
        self.button_import = tkinter.Button(self.ui_frame,
                                            command=lambda: import_data.handle_import(self.text_ranking, ranking),
                                            text=constants.BUTTON_TEXT_IMPORT, bg=constants.LIGHT_GRAY)
        self.button_import.place(x=10, y=385, width=100, height=30)
        self.button_export = tkinter.Button(self.ui_frame, command=lambda: export_data.export_data(self.text_ranking),
                                            text=constants.BUTTON_TEXT_EXPORT, bg=constants.LIGHT_GRAY)
        self.button_export.place(x=120, y=385, width=100, height=30)
