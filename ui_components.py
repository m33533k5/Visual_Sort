import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo

import i18n

import tooltip
from constants import *
import constants
from controller import Controller
from data.import_data import ImportData
from data.export_data import ExportData


class UIBase(type):
    """
    UIBase dient als Metaklasse für UIComponents. Eine Metaklasse in Python ist eine Klasse von einer Klasse,
    die das Erstellen und Verwalten von Klassen in Python steuert. Hier wird sie verwendet, um das Singleton-Designmuster
    zu implementieren, d.h., es wird sichergestellt, dass von der Klasse UIComponents nur eine Instanz erstellt wird,
    unabhängig davon, wie oft sie instanziiert wird.
    """

    instances = {}  # Ein Klassenattribut, das alle Instanzen speichert.

    def __call__(cls, *args, **kwargs):
        """
        Überschreibt den __call__-Operator der Metaklasse. Diese Methode wird aufgerufen, wenn eine Instanz der Klasse,
        die UIBase als Metaklasse hat, erstellt wird. Sie überprüft, ob bereits eine Instanz der Klasse existiert,
        und gibt diese zurück, anstatt eine neue zu erstellen, um das Singleton-Verhalten zu gewährleisten.
        """
        if cls not in cls.instances:
            instance = super().__call__(*args, **kwargs)  # Erstellt eine neue Instanz, wenn keine vorhanden ist.
            cls.instances[cls] = instance
        return cls.instances[cls]


class UIComponents(metaclass=UIBase):
    """
    UIComponents ist verantwortlich für die Erstellung und Verwaltung aller Benutzeroberflächenkomponenten
    der Anwendung. Sie definiert das Hauptfenster, das Canvas für Zeichnungen, Labels, Buttons und weitere
    UI-Elemente. Diese Klasse verwendet UIBase als Metaklasse, was bedeutet, dass von ihr nur eine Instanz
    erstellt werden kann (Singleton-Designmuster).
    """

    # Initialisierung der grundlegenden UI-Komponenten als Klassenvariablen.
    window = tkinter.Tk()
    canvas = tkinter.Canvas(window, width=800, height=425, bg=constants.WHITE)
    ui_frame = tkinter.Frame(window, width=400, height=425, bg=constants.LIGHT_GRAY)
    # Weitere UI-Komponenten als Platzhalter initialisiert, werden später konfiguriert.
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
    algo_list = []

    def set_list(self, list):
        self.algo_list = list

    def set_language(self, language):
        i18n.set('locale', language)
        self.update_ui_with_translations()

    def setup_gui(self, algorithm_name, algo_names, steps, ranking, algo_list, array_size):
        """
        Konfiguriert und platziert alle UI-Komponenten im Hauptfenster. Diese Methode nimmt Parameter entgegen,
        um die Dropdown-Menüs für Geschwindigkeit und Algorithmus, Eingabefelder und andere interaktive Elemente
        entsprechend zu initialisieren und einzurichten.

        :param algorithm_name: Textvariable für das Algorithmus-Dropdown.
        :param algo_names: Liste der Optionen für das Algorithmus-Dropdown.
        :param steps: Textvariable für das Eingabefeld der Schrittzahl.
        :param ranking: Textvariable für das Ranglisten-Textfeld.
        :param algo_list: Liste der verfügbaren Algorithmen für die Sortierung.
        :param array_size: Textvariable für das Eingabefeld der Arraygröße.
        """

        # Instanzen von Hilfsklassen für die Funktionalität der UI-Elemente
        controller = Controller()
        export_data = ExportData()
        import_data = ImportData()

        # Hauptfenster-Einstellungen
        self.window.config(bg=constants.WHITE)  # Hintergrundfarbe des Hauptfensters

        # Einrichtung der Benutzeroberfläche
        self.canvas.grid(row=0, column=0, padx=10, pady=5)

        # UI-Frame für Steuerelemente und Informationen
        self.ui_frame.grid(row=0, column=1, padx=10, pady=5)

        # UI-Komponenten für die Anzeige und Interaktion
        self.algo_menu = ttk.Combobox(self.ui_frame, textvariable=algorithm_name, values=algo_names)
        self.algo_menu.place(x=220, y=10, width=150, height=25)
        self.algo_menu.current(4)

        self.label_algorithm.place(x=10, y=10, width=150, height=25)
        self.label_speed.place(x=10, y=45, width=150, height=25)
        self.label_size.place(x=10, y=80, width=150, height=25)
        self.label_steps.place(x=10, y=115, width=150, height=25)
        self.label_ranking.place(x=10, y=190, width=150, height=25)

        # Konfiguration der Dropdown-Menüs für Algorithmusauswahl und Geschwindigkeit
        self.speed_menu = ttk.Combobox(self.ui_frame, values=i18n.t('main.speeds', count=3)[:])
        # self.speed_menu.bind('<<ComboboxSelected>>', controller.set_speed(algo_list, self.speed_menu))
        self.speed_menu.bind('<<ComboboxSelected>>', self.set_speed)
        self.speed_menu.config(textvariable=i18n.t('main.speeds', count=3)[self.speed_menu.current()])
        self.speed_menu.place(x=220, y=45, width=150, height=25)
        self.speed_menu.current(0)  # Standardauswahl

        self.button_generate = tkinter.Button(self.ui_frame,
                                              command=lambda: controller.generate(self.canvas, self.window, array_size))
        self.button_generate.place(x=10, y=155, width=100, height=30)
        self.button_sort = tkinter.Button(self.ui_frame,
                                          command=lambda: controller.sort(self, steps, ranking, algo_list))
        self.button_sort.place(x=120, y=155, width=100, height=30)
        self.button_german_translation = tkinter.Button(self.ui_frame,
                                                        command=lambda: self.set_language(constants.LANGUAGE_DE))
        self.button_german_translation.place(x=270, y=155, width=100, height=30)
        self.button_english_translation = tkinter.Button(self.ui_frame,
                                                         command=lambda: self.set_language(constants.LANGUAGE_EN))
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

        self.set_language(LANGUAGE_DE)

    def set_speed(self, event):
        """
        Bestimmt die Geschwindigkeit der Visualisierung basierend auf der Benutzerauswahl.

        :param speed_menu: Das Dropdown-Menü, aus dem die Geschwindigkeit ausgewählt wird.
        :return: Die gewählte Geschwindigkeit als Verzögerung zwischen den Sortierschritten.
        """
        algo_list = [list(element.values())[0] for element in self.algo_list]  # Extraktion der Namen für die UI
        # Auswahl der Geschwindigkeit basierend auf der Menüauswahl

        if self.speed_menu is None:
            [element.set_time_tick(0.001) for element in algo_list]
            return
        if self.speed_menu.current() == 2:
            [element.set_time_tick(0.3) for element in algo_list]
        elif self.speed_menu.current() == 1:
            [element.set_time_tick(0.01) for element in algo_list]
        else:
            [element.set_time_tick(0.001) for element in algo_list]


    def update_ui_with_translations(self):
        """
        Aktualisiert die UI-Komponenten mit den entsprechenden Übersetzungen.

        :param translations: Das configparser Objekt mit den geladenen Übersetzungen.
        :param ui_components: Ein Objekt, das die UI-Komponenten enthält, die aktualisiert werden sollen.
        """
        # Aktualisiere den Titel des Fensters mit der übersetzten Zeichenkette.
        self.window.title(i18n.t("main.window_title"))

        # Aktualisiere Texte und Tooltips für jede UI-Komponente.
        # Für jede Komponente wird der Text aus den Übersetzungen geladen und als Tooltip hinzugefügt.
        self.label_algorithm.config(text=i18n.t('main.label_algorithm'), bg=WHITE)
        tooltip.ToolTip.create_tooltip(self.label_algorithm, i18n.t('main.tooltip_label_algorithm'))
        tooltip.ToolTip.create_tooltip(self.algo_menu, i18n.t('main.tooltip_field_algorithm'))

        self.label_speed.config(text=i18n.t('main.label_speed'), bg=WHITE)
        tooltip.ToolTip.create_tooltip(self.label_speed, i18n.t('main.tooltip_label_speed'))
        tooltip.ToolTip.create_tooltip(self.speed_menu, i18n.t('main.tooltip_field_speed'))
        position = self.speed_menu.current()
        self.speed_menu.config(values=i18n.t('main.speeds', count=3)[:])
        self.speed_menu.current(position)

        self.label_size.config(text=i18n.t('main.label_size'), bg=WHITE)
        tooltip.ToolTip.create_tooltip(self.label_size, i18n.t('main.tooltip_label_size'))
        tooltip.ToolTip.create_tooltip(self.size_entry, i18n.t('main.tooltip_field_size'))

        self.label_steps.config(text=i18n.t('main.label_steps'), bg=WHITE)
        tooltip.ToolTip.create_tooltip(self.label_steps, i18n.t('main.tooltip_label_steps'))
        tooltip.ToolTip.create_tooltip(self.size_steps, i18n.t('main.tooltip_field_steps'))

        self.label_ranking.config(text=i18n.t('main.label_ranking'), bg=WHITE)
        tooltip.ToolTip.create_tooltip(self.label_ranking, i18n.t('main.tooltip_label_ranking'))
        tooltip.ToolTip.create_tooltip(self.text_ranking, i18n.t('main.tooltip_field_ranking'))

        self.button_generate.config(text=i18n.t('main.button_generate'), bg=LIGHT_GRAY)
        tooltip.ToolTip.create_tooltip(self.button_generate, i18n.t('main.tooltip_button_generate'))

        self.button_sort.config(text=i18n.t('main.button_sort'), bg=LIGHT_GRAY)
        tooltip.ToolTip.create_tooltip(self.button_sort, i18n.t('main.tooltip_button_sort'))

        self.button_german_translation.config(text=i18n.t('main.button_german_translation'), bg=LIGHT_GRAY)
        self.button_english_translation.config(text=i18n.t('main.button_english_translation'), bg=LIGHT_GRAY)
