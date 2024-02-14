from graphmanager.observer import Observer


class Graph(Observer):
    """
    Eine konkrete Implementierung eines Observers, der für die Visualisierung von Daten
    auf einem Canvas verantwortlich ist. Als Teil des Observer-Musters reagiert diese Klasse
    auf Benachrichtigungen über Datenänderungen, indem sie die neuen Daten visualisiert.

    Dies ermöglicht eine lose Kopplung zwischen der Datenquelle (dem Subject) und der
    Datenvisualisierung (dem Observer), wodurch der Visualisierungskomponente ermöglicht wird,
    auf Änderungen der Daten dynamisch zu reagieren, ohne direkt mit der Datenquelle verbunden zu sein.
    """

    def __init__(self, canvas, window):
        """
        Initialisiert eine neue Instanz der Graph-Klasse.

        :param canvas: Das Canvas-Widget, auf dem die Daten visualisiert werden.
        :param window: Das Fenster, in dem das Canvas-Widget enthalten ist. Wird verwendet,
                       um das Fenster bei Datenaktualisierungen zu aktualisieren.
        """
        self.canvas = canvas  # Das Canvas-Widget für die Zeichnung
        self.window = window  # Das Fenster, das das Canvas-Widget enthält

    def update(self, data, color_array) -> None:
        """
        Wird vom Subject aufgerufen, um den Observer über eine Änderung der Daten zu informieren.
        Visualisiert die übergebenen Daten als Balkendiagramm auf dem Canvas.

        :param data: Die zu visualisierenden Daten als Liste von Zahlen.
        :param color_array: Eine Liste von Farben, die jedem Balken zugeordnet werden,
                            entsprechend der Position im Datenarray.
        """
        self.canvas.delete("all")  # Löscht vorherige Zeichnungen vom Canvas
        canvas_width = 800
        canvas_height = 425
        x_width = canvas_width / (len(data) + 1)  # Berechnet die Breite jedes Balkens
        offset = 4  # Randabstand
        spacing = 2  # Abstand zwischen den Balken
        normalized_data = [i / max(data) for i in data]  # Normalisiert die Daten für die Visualisierung

        # Zeichnet Balken für jeden Dateneintrag
        for i, height in enumerate(normalized_data):
            # Berechnet Koordinaten für jeden Balken
            x0 = i * x_width + offset + spacing
            y0 = canvas_height - height * 425  # Skaliert die Balkenhöhe
            x1 = (i + 1) * x_width + offset
            y1 = canvas_height
            # Erzeugt den Balken auf dem Canvas mit der entsprechenden Farbe
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])

        self.window.update_idletasks()  # Aktualisiert das Fenster, um die neuen Zeichnungen anzuzeigen
