import time

from algorithms.sort_strategie import SortAlgorithm
from constants import BLUE, YELLOW
from graphmanager.graph_manager import GraphManager


class HeapSort(SortAlgorithm):
    """
    Implementiert den Heap-Sort-Algorithmus als Teil der Sort_Algorithm-Strategie.

    HeapSort ist ein Vergleichsbasierter Sortieralgorithmus, der die Heap-Datenstruktur nutzt.
    Es wird ein Binärheap erstellt, um die Elemente in aufsteigender Reihenfolge zu sortieren.
    Ein Heap ist eine zumeist auf Bäumen basierende abstrakte Datenstruktur.
    """

    def __init__(self, time_tick):
        """
        Initialisiert eine neue Instanz der HeapSort-Klasse.

        :param time_tick: Die Zeitverzögerung zwischen den Visualisierungsschritten.
        """
        super().__init__(time_tick) # Ruft den Konstruktor der Basisklasse auf

    def heapify(self, data, n, i, steps):
        """
        Hilfsfunktion zum Umwandeln eines Arrays in einen Heap, beginnend mit dem Index i als Wurzel.

        :param data: Die zu sortierenden Daten.
        :param n: Die Größe des Heaps.
        :param i: Der Index der Wurzel des Heaps.
        :param steps: Die Anzahl der bisher durchgeführten Schritte.
        :return: Die aktualisierte Anzahl der Schritte.
        """
        largest = i  # Initialisiere largest als Wurzel
        left = 2 * i + 1  # linkes Kind
        right = 2 * i + 2  # rechtes Kind

        # Überprüfe, ob linkes Kind größer als Wurzel
        if left < n and data[i] < data[left]:
            largest = left
            steps += 1

        # Überprüfe, ob rechtes Kind größer als bisher größtes Element
        if right < n and data[largest] < data[right]:
            largest = right
            steps += 1

        # Wenn größtes Element nicht Wurzel, tausche und fortfahre Heapify
        if largest != i:
            data[i], data[largest] = data[largest], data[i]  # Tausche
            steps += 1
            steps = self.heapify(data, n, largest, steps)  # Rekursive Fortführung von Heapify
        return steps

    def sort(self, graph_manager: GraphManager):
        """
        Führt den Heap-Sort-Algorithmus aus und visualisiert den Prozess.

        :param graph_manager: Der GraphManager, der für die Visualisierung des Sortiervorgangs verwendet wird.
        :return: Die Anzahl der durchgeführten Schritte während des Sortierprozesses.
        """
        n = len(self.data)  # Größe der zu sortierenden Daten
        steps = 0  # Zähler für die Anzahl der Schritte

        # Erstelle einen Max-Heap
        for i in range(n - 1, -1, -1):
            steps = self.heapify(self.data, n, i, steps)

        # Extrahiere Elemente einzeln
        for i in range(n - 1, 0, -1):
            self.data[i], self.data[0] = self.data[0], self.data[i]  # Aktuelles Element mit der Wurzel tauschen
            steps += 1
            self.heapify(self.data, i, 0, steps)  # Heapify auf den reduzierten Heap anwenden
            graph_manager.notify(self.data, [YELLOW if x == i else BLUE for x in range(n)])  # Visualisierung
            time.sleep(self.time_tick)  # Wartezeit für die Visualisierung

        graph_manager.notify(self.data, [BLUE for _ in range(len(self.data))])  # Endgültige Visualisierung
        return steps  # Rückgabe der Gesamtschrittzahl
