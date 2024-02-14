import time

from algorithms.sort_strategie import SortAlgorithm
from constants import BLUE
from graphmanager.graph_manager import GraphManager


class CountingSort(SortAlgorithm):
    """
    Implementiert den Counting-Sort-Algorithmus, einen nicht-vergleichsbasierten Sortieralgorithmus,
    als eine konkrete Strategie des Sort_Algorithm.

    Counting-Sort zählt die Häufigkeit jedes einzigartigen Elements innerhalb eines bestimmten Bereichs
    und nutzt diese Zählungen, um die Elemente in sortierter Reihenfolge anzulegen. Dieser Algorithmus ist
    effizient, wenn der maximale Wert des Arrays relativ klein ist im Vergleich zur Länge des Arrays.
    """

    def __init__(self, time_tick):
        """
        Initialisiert eine neue Instanz der CountingSort-Klasse.

        :param time_tick: Die Zeitverzögerung zwischen den Visualisierungsschritten.
        """
        self.time_tick = time_tick

    def sort(self, graph_manager: GraphManager):
        """
        Führt den Counting-Sort-Algorithmus aus und visualisiert den Prozess.

        :param graph_manager: Der GraphManager, der für die Visualisierung des Sortiervorgangs verwendet wird.
        :return: Die Anzahl der durchgeführten Schritte während des Sortierprozesses.
        """
        steps = 0  # Initialisiert den Schrittzähler
        n = max(self.data) + 1  # Bestimmt den maximalen Wert im Array für die Größe des Zählarrays
        count = [0] * n  # Initialisiert das Zählarray

        # Zählt die Häufigkeit jedes Elements im Array
        for item in self.data:
            count[item] += 1
            steps += 1  # Zählt jeden Durchgang als einen Schritt

        k = 0  # Hilfsindex für das Zurückschreiben der sortierten Elemente
        # Geht durch das Zählarray und schreibt jedes Element entsprechend seiner Häufigkeit zurück ins Originalarray
        for i in range(n):
            for j in range(count[i]):
                self.data[k] = i
                graph_manager.notify(self.data,
                                     [BLUE for _ in range(len(self.data))])  # Visualisiert den aktuellen Schritt
                k += 1
                steps += 1  # Zählt die Schritte des Zurückschreibens
                time.sleep(self.time_tick)  # Wartet für die Visualisierung

        graph_manager.notify(self.data, [BLUE for _ in range(len(self.data))])  # Endgültige Visualisierung
        return steps  # Gibt die Gesamtzahl der Schritte zurück
