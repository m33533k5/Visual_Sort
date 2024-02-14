import time

from algorithms.sort_strategie import SortAlgorithm
from constants import BLUE, YELLOW, PURPLE, DARK_BLUE
from graphmanager.graph_manager import GraphManager


class QuickSort(SortAlgorithm):
    """
    Implementiert den Quick-Sort-Algorithmus als eine spezifische Strategie des Sort_Algorithm.

    QuickSort ist ein effizienter, vergleichsbasierter, rekursiver Sortieralgorithmus, der
    das Prinzip des Teile-und-Herrsche (Divide-and-Conquer) verwendet. Der Algorithmus wählt
    ein "Pivot"-Element aus und sortiert dann die Elemente so um, dass alle Elemente kleiner
    als das Pivot vor diesem und alle Elemente größer als das Pivot dahinter stehen.
    """

    def __init__(self, time_tick):
        """
        Initialisiert eine neue Instanz der QuickSort-Klasse.

        :param time_tick: Die Zeitverzögerung zwischen den Visualisierungsschritten des Sortierprozesses.
        """
        super().__init__(time_tick) # Ruft den Konstruktor der Basisklasse auf
        self.steps = 0  # Zählt die Anzahl der durchgeführten Operationen während des Sortierens

    def partition(self, data, start, end):
        """
        Hilfsfunktion zum Aufteilen des Arrays um ein Pivot-Element.

        :param data: Die zu sortierenden Daten.
        :param start: Der Startindex des zu sortierenden Bereichs.
        :param end: Der Endindex des zu sortierenden Bereichs.
        :return: Die neue Position des Pivot-Elements und die aktualisierte Anzahl der Schritte.
        """
        i = start + 1
        pivot = data[start]  # Wählt das erste Element als Pivot
        self.steps += 1  # Zählt die Initialisierung des Pivots

        # Vergleicht jedes Element mit dem Pivot und ordnet es entsprechend um
        for j in range(start + 1, end + 1):
            self.steps += 1  # Zählt jeden Vergleich
            if data[j] < pivot:
                data[i], data[j] = data[j], data[i]  # Tauscht Elemente
                i += 1
                self.steps += 1  # Zählt jede Vertauschung
        data[start], data[i - 1] = data[i - 1], data[start]  # Setzt das Pivot-Element an die richtige Position
        self.steps += 1  # Zählt die letzte Vertauschung des Pivots
        return i - 1, self.steps

    def sort(self, graph_manager: GraphManager):
        """
        Führt den Quick-Sort-Algorithmus aus und visualisiert den Prozess.

        :param graph_manager: Der GraphManager, der für die Visualisierung des Sortiervorgangs verwendet wird.
        :return: Die Anzahl der durchgeführten Schritte während des Sortierprozesses.
        """
        self.steps = self.quick_sort_helper(self.data, 0, len(self.data) - 1, graph_manager)
        return self.steps

    def quick_sort_helper(self, data, start, end, graph_manager):
        """
        Rekursive Hilfsfunktion für den Quick-Sort-Algorithmus.

        :param data: Die zu sortierenden Daten.
        :param start: Der Startindex des zu sortierenden Bereichs.
        :param end: Der Endindex des zu sortierenden Bereichs.
        :param graph_manager: Der GraphManager für die Visualisierung.
        :return: Die aktualisierte Anzahl der durchgeführten Schritte.
        """
        if start < end:
            pivot_position, self.steps = self.partition(data, start, end)
            self.steps = self.quick_sort_helper(data, start, pivot_position - 1, graph_manager)
            self.steps = self.quick_sort_helper(data, pivot_position + 1, end, graph_manager)

            # Visualisiert den aktuellen Zustand des Arrays mit Farbcodierung
            graph_manager.notify(self.data,
                                 [PURPLE if start <= x < pivot_position else YELLOW if x == pivot_position
                                 else DARK_BLUE if pivot_position < x <= end else BLUE for x in
                                  range(len(self.data))])
            time.sleep(self.time_tick)

        graph_manager.notify(self.data, [BLUE for x in range(len(self.data))])  # Endgültige Visualisierung
        return self.steps
