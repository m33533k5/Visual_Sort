class UIComponents:
    def __init__(self, canvas, window, label_algorithm, algo_menu, label_speed, speed_menu, label_size, size_entry,
                 label_steps, size_steps, label_ranking, text_ranking, button_generate, button_sort,
                 button_german_translation, button_english_translation):
        """
        Initialisiert ein UIComponents-Objekt, das alle wesentlichen UI-Elemente der Anwendung hält.

        :param canvas: Das Canvas-Widget für die Zeichnungen und Visualisierungen.
        :param window: Das Hauptfenster der Anwendung.
        :param label_algorithm: Label für die Anzeige des Algorithmusnamens.
        :param algo_menu: Dropdown-Menü zur Auswahl des Sortieralgorithmus.
        :param label_speed: Label für die Anzeige der Geschwindigkeitseinstellung.
        :param speed_menu: Dropdown-Menü zur Auswahl der Visualisierungsgeschwindigkeit.
        :param label_size: Label für die Anzeige der Größeneinstellung des Arrays.
        :param size_entry: Eingabefeld für die Größe des zu sortierenden Arrays.
        :param label_steps: Label für die Anzeige der Anzahl der Sortierschritte.
        :param size_steps: Eingabefeld/Anzeigefeld für die Anzahl der Schritte während des Sortierprozesses.
        :param label_ranking: Label für die Anzeige der Rangordnungsinformation.
        :param text_ranking: Textfeld für detaillierte Rangordnungsinformationen.
        :param button_generate: Button zum Generieren eines neuen Arrays.
        :param button_sort: Button zum Starten des Sortierprozesses.
        :param button_german_translation: Button zur Anwendung der deutschen Sprache in der UI.
        :param button_english_translation: Button zur Anwendung der englischen Sprache in der UI.
        """
        self.canvas = canvas
        self.window = window
        self.label_algorithm = label_algorithm
        self.algo_menu = algo_menu
        self.label_speed = label_speed
        self.speed_menu = speed_menu
        self.label_size = label_size
        self.size_entry = size_entry
        self.label_steps = label_steps
        self.size_steps = size_steps
        self.label_ranking = label_ranking
        self.text_ranking = text_ranking
        self.button_generate = button_generate
        self.button_sort = button_sort
        self.button_german_translation = button_german_translation
        self.button_english_translation = button_english_translation

