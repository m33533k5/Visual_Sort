import time

from algorithms.sort_strategie import SortAlgorithm
from constants import BLUE, YELLOW
from graphmanager.graph_manager import GraphManager


class BubbleSort(SortAlgorithm):
    """
    Implementiert den Bubble-Sort-Algorithmus als eine konkrete Strategie des Sort_Algorithm.
    BubbleSort ist ein einfacher Sortieralgorithmus, der wiederholt über die Liste läuft,
    benachbarte Elemente vertauscht, wenn sie in der falschen Reihenfolge sind.
    """

    def __init__(self, time_tick):
        """
        Initialisiert eine neue Instanz der BubbleSort-Klasse.

        :param time_tick: Die Zeitverzögerung zwischen den Sortierschritten für die Visualisierung.
        """
        self.time_tick = time_tick

    def sort(self, graph_manager: GraphManager):
        """
        Führt den Bubble-Sort-Algorithmus aus und visualisiert jeden Sortierschritt.

        :param graph_manager: Der GraphManager, der für die Visualisierung des Sortierprozesses verwendet wird.
        :return: Die Anzahl der durchgeführten Sortierschritte.
        """
        size = len(self.data)  # Bestimmt die Größe der zu sortierenden Datenliste
        steps = 0  # Initialisiert den Schrittzähler

        # Durchläuft die Datenliste und führt Vertauschungen durch, wo nötig
        for i in range(size - 1):
            for j in range(size - i - 1):
                # Überprüft, ob das aktuelle Element größer ist als das nächste Element
                if self.data[j] > self.data[j + 1]:
                    # Vertauscht die Elemente
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    # Benachrichtigt den GraphManager, um die Vertauschung zu visualisieren
                    graph_manager.notify(self.data,
                                         [YELLOW if x == j or x == j + 1 else BLUE for x in range(len(self.data))])
                    steps += 1  # Erhöht den Schrittzähler
                    time.sleep(self.time_tick)  # Wartet für die Visualisierung

        # Benachrichtigt den GraphManager, um das Ende des Sortiervorgangs zu signalisieren
        graph_manager.notify(self.data, [BLUE for _ in range(len(self.data))])
        return steps  # Gibt die Anzahl der durchgeführten Schritte zurück
