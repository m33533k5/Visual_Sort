import random

from constants import CANVAS_ALL, BLUE, SPEED_MENU_SLOW, SPEED_MENU_MEDIUM, END
from graphmanager.graph import Graph
from graphmanager.graph_manager import GraphManager


class Controller:

    def __init__(self):
        self.data = []

    def drawData(self, data, color_array, canvas, window):
        """
        Visualisiert die Daten als Balkendiagramm auf dem Canvas.

        :param data: Die zu visualisierenden Daten als Liste von Zahlen.
        :param color_array: Eine Liste von Farben, die jedem Balken zugeordnet werden.
        :param canvas: Das Canvas-Widget, auf dem gezeichnet wird.
        :param window: Das Fenster, in dem das Canvas-Widget enthalten ist.
        """
        canvas.delete(CANVAS_ALL)  # Löscht frühere Zeichnungen
        canvas_width = 800
        canvas_height = 425
        x_width = canvas_width / (len(data) + 1)  # Breite eines Balkens
        offset = 4  # Randabstand
        spacing = 2  # Abstand zwischen den Balken
        normalized_data = [i / max(data) for i in data]  # Normalisiere die Daten zur Höhenanpassung

        # Zeichnet Balken für jeden Dateneintrag
        for i, height in enumerate(normalized_data):
            # Berechnet Koordinaten für jeden Balken
            x0 = i * x_width + offset + spacing
            y0 = canvas_height - height * 425  # Skaliert die Balkenhöhe
            x1 = (i + 1) * x_width + offset
            y1 = canvas_height
            # Erzeugt den Balken auf dem Canvas
            canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])

        window.update_idletasks()  # Aktualisiert das Fenster, um die neuen Zeichnungen anzuzeigen

    # Randomly generate array
    def generate(self, canvas, window, array_size):
        """
        Generiert eine zufällige Liste von Zahlen und visualisiert diese.

        :param canvas: Das Canvas-Widget, auf dem die Daten visualisiert werden.
        :param window: Das Fenster, in dem das Canvas-Widget enthalten ist.
        :param array_size: Die Größe der zu generierenden Datenliste.
        """
        size = array_size.get()  # Größe der zu generierenden Liste
        self.data = random.sample(range(1, size + 1), size)  # Erzeugt eine Liste einzigartiger Zahlen
        self.drawData(self.data, [BLUE for x in range(len(self.data))], canvas,
                      window)  # Visualisiert die generierte Liste

    def set_speed(self, speed_menu=None):
        """
        Bestimmt die Geschwindigkeit der Visualisierung basierend auf der Benutzerauswahl.

        :param speed_menu: Das Dropdown-Menü, aus dem die Geschwindigkeit ausgewählt wird.
        :return: Die gewählte Geschwindigkeit als Zeitverzögerung zwischen den Sortierschritten.
        """
        # Auswahl der Geschwindigkeit basierend auf der Menüauswahl

        if speed_menu is None:
            return 0.001
        if speed_menu.get() == SPEED_MENU_SLOW:
            return 0.3
        elif speed_menu.get() == SPEED_MENU_MEDIUM:
            return 0.1
        else:
            return 0.001

    def sort(self, ui_components, steps, ranking, algo_list):
        """
        Führt den gewählten Sortieralgorithmus aus und aktualisiert das Ranking basierend auf der Anzahl der Schritte.

        :param ui_components: UI-Komponenten, die für die Visualisierung und Steuerung benötigt werden.
        :param steps: Variable, die die Anzahl der Sortierschritte speichert.
        :param ranking: Dictionary, das das Ranking der Algorithmen hält.
        :param algo_list: Liste der verfügbaren Sortieralgorithmen.
        """
        step_count = 0  # Initialisiert die Zählung der Schritte für den aktuellen Sortiervorgang.

        # Initialisiert Graph- und GraphManager-Instanzen für die Visualisierung.
        graph = Graph(ui_components.canvas, ui_components.window)
        graph_manager = GraphManager()
        graph_manager.attach(graph)  # Verknüpft den GraphManager mit dem Graphen für die Visualisierung.

        algo_name = ui_components.algo_menu.get()  # Holt den Namen des ausgewählten Algorithmus aus dem Dropdown-Menü.

        # Durchläuft die Liste der Algorithmen und führt den ausgewählten Algorithmus aus.
        for algorithm in algo_list:
            if algo_name == list(algorithm.keys())[0]:  # Prüft, ob der Algorithmus der ausgewählte ist.
                list(algorithm.values())[0].set_data(self.data)  # Setzt die Daten für den Algorithmus.
                step_count = list(algorithm.values())[0].sort(graph_manager)  # Führt den Sortiervorgang aus.

        steps.set(step_count)  # Aktualisiert die Anzeige der Schrittzahl im UI.

        # Aktualisiert das Ranking-Dictionary mit den Ergebnissen des Sortiervorgangs.
        if algo_name not in ranking:
            ranking[algo_name] = [step_count]  # Fügt neue Algorithmen mit ihrer Schrittzahl hinzu.
        else:
            ranking[algo_name].append(step_count)  # Fügt weitere Schrittzahlen zu bestehenden Algorithmen hinzu.

        # Aktualisiert die Anzeige des Rankings im Text-Widget.
        self.update_ranking(ui_components.text_ranking, ranking)

    def update_ranking(self, text_ranking, ranking):
        """
        Aktualisiert das Text-Widget mit einer sortierten Liste von Algorithmen basierend auf ihrer Leistung.

        :param text_ranking: Das Text-Widget, in dem das Ranking angezeigt wird.
        :param ranking: Ein Dictionary, das Algorithmen als Schlüssel und Listen ihrer Leistung (Schritte) als Werte enthält.
        """
        position = 1  # Startposition für das Ranking.
        # Löscht den bisherigen Inhalt im Text-Widget, um es für die Aktualisierung vorzubereiten.
        text_ranking.delete('1.0', END)

        # Kompiliert eine Liste aller durchgeführten Schritte aller Algorithmen.
        alle_schritte = []
        for algorithmus, schritte_liste in ranking.items():
            for schritte in schritte_liste:
                alle_schritte.append(
                    (algorithmus, schritte))  # Erstellt ein Tuple aus Algorithmusname und Schrittanzahl.

        # Sortiert die Liste der Schritte aufsteigend nach der Schrittanzahl.
        sortierte_schritte = sorted(alle_schritte, key=lambda x: x[1])

        # Durchläuft die sortierte Liste und fügt jede Platzierung ins Text-Widget ein.
        for algorithmus, schritte in sortierte_schritte:
            text_ranking.insert(END, f"{position}. {algorithmus}: {schritte} Schritte\n")  # Fügt die Platzierung hinzu.
            position += 1  # Erhöht die Platzierungsnummer für den nächsten Eintrag.
