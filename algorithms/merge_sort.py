import time

from algorithms.sort_strategie import SortAlgorithm
from constants import *
from graphmanager.graph_manager import GraphManager


class MergeSort(SortAlgorithm):
    """
    Implementiert den Merge-Sort-Algorithmus als eine spezifische Strategie des Sort_Algorithm.

    Merge-Sort ist ein effizienter, vergleichsbasierter, rekursiver Sortieralgorithmus, der auf dem
    Prinzip des Teile-und-Herrsche (Divide-and-Conquer) basiert. Der Algorithmus teilt das Array
    in Hälften, sortiert diese rekursiv und führt sie dann in einem Merge-Schritt zusammen.
    """

    def __init__(self, time_tick):
        """
        Initialisiert eine neue Instanz der MergeSort-Klasse.

        :param time_tick: Die Zeitverzögerung zwischen den Visualisierungsschritten des Sortierprozesses.
        """
        super().__init__(time_tick) # Ruft den Konstruktor der Basisklasse auf
        self.steps = 0  # Zählt die Anzahl der durchgeführten Operationen während des Sortierens

    def merge(self, data, start, mid, end):
        """
        Führt zwei Teile eines Arrays zusammen, wobei angenommen wird, dass beide Teile sortiert sind.

        :param data: Die zu sortierenden Daten.
        :param start: Der Startindex des zu sortierenden Bereichs.
        :param mid: Der Mittelpunkt des zu sortierenden Bereichs.
        :param end: Der Endindex des zu sortierenden Bereichs.
        :return: Die aktualisierte Anzahl der durchgeführten Schritte.
        """
        p = start
        q = mid + 1
        temp_array = []  # Hilfsarray zum Zusammenführen

        # Vergleicht Elemente der beiden Hälften und fügt das kleinere Element zum Hilfsarray hinzu
        for i in range(start, end + 1):
            self.steps += 1
            if p > mid:  # Wenn linke Hälfte komplett hinzugefügt wurde
                temp_array.append(data[q])
                q += 1
            elif q > end:  # Wenn rechte Hälfte komplett hinzugefügt wurde
                temp_array.append(data[p])
                p += 1
            elif data[p] < data[q]:
                temp_array.append(data[p])
                p += 1
            else:
                temp_array.append(data[q])
                q += 1

        # Kopiert die sortierten Elemente zurück ins Originalarray
        for p in range(len(temp_array)):
            self.steps += 1
            data[start] = temp_array[p]
            start += 1
        return self.steps

    def sort(self, graph_manager: GraphManager):
        """
        Führt den Merge-Sort-Algorithmus aus und visualisiert den Prozess.

        :param graph_manager: Der GraphManager, der für die Visualisierung des Sortiervorgangs verwendet wird.
        :return: Die Anzahl der durchgeführten Schritte während des Sortierprozesses.
        """
        self.steps = self.merge_sort_helper(self.data, 0, len(self.data) - 1, graph_manager)
        graph_manager.notify(self.data, [BLUE for _ in range(len(self.data))])  # Endgültige Visualisierung
        return self.steps

    def merge_sort_helper(self, data, start, end, graph_manager):
        """
        Hilfsfunktion für den rekursiven Ablauf des Merge-Sort-Algorithmus.

        :param data: Die zu sortierenden Daten.
        :param start: Der Startindex des zu sortierenden Bereichs.
        :param end: Der Endindex des zu sortierenden Bereichs.
        :param graph_manager: Der GraphManager für die Visualisierung.
        :return: Die aktualisierte Anzahl der durchgeführten Schritte.
        """
        if start < end:
            mid = (start + end) // 2
            self.merge_sort_helper(data, start, mid, graph_manager)  # Sortiert linke Hälfte
            self.merge_sort_helper(data, mid + 1, end, graph_manager)  # Sortiert rechte Hälfte
            self.steps = self.merge(data, start, mid, end)  # Führt beide Hälften zusammen

            # Visualisiert den aktuellen Zustand des Arrays
            graph_manager.notify(data, [PURPLE if start <= x <= mid else DARK_BLUE if mid < x <= end else BLUE for x in
                                        range(len(data))])
            time.sleep(self.time_tick)
        return self.steps