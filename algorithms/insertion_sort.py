import time

from algorithms.sort_strategie import SortAlgorithm
from constants import BLUE, YELLOW
from graphmanager.graph_manager import GraphManager


class InsertionSort(SortAlgorithm):
    """
    Implementiert den Insertion-Sort-Algorithmus als eine spezifische Strategie des Sort_Algorithm.

    Insertion-Sort ist ein einfacher, aber effizienter Sortieralgorithmus für kleinere Datensätze.
    Er baut die sortierte Liste Element für Element auf, indem jedes neue Element an die entsprechende
    Position in der bereits sortierten Liste eingefügt wird.
    """

    def __init__(self, time_tick):
        """
        Initialisiert eine neue Instanz der InsertionSort-Klasse.

        :param time_tick: Die Zeitverzögerung zwischen den Visualisierungsschritten des Sortierprozesses.
        """
        super().__init__(time_tick) # Ruft den Konstruktor der Basisklasse auf

    def sort(self, graph_manager: GraphManager):
        """
        Führt den Insertion-Sort-Algorithmus aus und visualisiert jeden Schritt des Sortierprozesses.

        :param graph_manager: Der GraphManager, der für die Visualisierung des Sortierprozesses verwendet wird.
        :return: Die Anzahl der durchgeführten Schritte während des Sortierprozesses.
        """
        steps = 0  # Zählt die Anzahl der durchgeführten Operationen

        # Durchläuft das Array, um jedes Element zu sortieren
        for i in range(len(self.data)):
            temp = self.data[i]  # Speichert das aktuelle Element zum Einfügen
            k = i
            # Verschiebt Elemente der sortierten Sequenz, die größer als das aktuelle Element sind,
            # eine Position nach rechts, um Platz für das Einfügen des aktuellen Elements zu schaffen
            while k > 0 and temp < self.data[k - 1]:
                self.data[k] = self.data[k - 1]  # Verschiebt das Element eine Position nach rechts
                k -= 1  # Geht zum vorherigen Element
                steps += 1  # Zählt den Schritt
            self.data[k] = temp  # Fügt das aktuelle Element an der richtigen Position ein
            # Visualisiert den aktuellen Zustand des Arrays
            graph_manager.notify(self.data, [YELLOW if x == k or x == i else BLUE for x in range(len(self.data))])
            time.sleep(self.time_tick)  # Wartet für die Visualisierung

        # Benachrichtigt den GraphManager nach dem vollständigen Sortieren
        graph_manager.notify(self.data, [BLUE for _ in range(len(self.data))])
        return steps  # Gibt die Gesamtzahl der Schritte zurück
