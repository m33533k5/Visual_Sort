import time
from algorithms.sort_strategie import SortAlgorithm
from constants import YELLOW, BLUE
from graphmanager.graph_manager import GraphManager


class SelectionSort(SortAlgorithm):
    """
    Implementiert den Selection-Sort-Algorithmus als eine spezifische Strategie des Sort_Algorithm.

    Selection-Sort ist ein einfacher, vergleichsbasierter Sortieralgorithmus. Der Algorithmus teilt das
    Array in zwei Teile: den sortierten Teil am Anfang und den unsortierten Teil am Rest des Arrays.
    Er wiederholt das Finden des kleinsten Elements aus dem unsortierten Teil und tauscht es mit dem
    ersten unsortierten Element.
    """

    def __init__(self, time_tick):
        """
        Initialisiert eine neue Instanz der SelectionSort-Klasse.

        :param time_tick: Die Zeitverzögerung zwischen den Visualisierungsschritten des Sortierprozesses.
        """
        super().__init__(time_tick) # Ruft den Konstruktor der Basisklasse auf

    def sort(self, graph_manager: GraphManager):
        """
        Führt den Selection-Sort-Algorithmus aus und visualisiert jeden Schritt des Sortierprozesses.

        :param graph_manager: Der GraphManager, der für die Visualisierung des Sortiervorgangs verwendet wird.
        :return: Die Anzahl der durchgeführten Schritte während des Sortierprozesses.
        """
        steps = 0  # Zählt die Anzahl der durchgeführten Operationen

        # Durchläuft das Array, um jedes Element zu sortieren
        for i in range(len(self.data) - 1):
            minimum = i  # Geht davon aus, dass das aktuelle Element das kleinste ist
            # Durchsucht den Rest des Arrays, um das tatsächlich kleinste Element zu finden
            for k in range(i + 1, len(self.data)):
                steps += 1  # Zählt den Vergleich
                if self.data[k] < self.data[minimum]:
                    minimum = k  # Aktualisiert das kleinste Element, wenn ein kleineres gefunden wird

            # Tauscht das kleinste gefundene Element mit dem ersten Element des unsortierten Teils
            if minimum != i:
                steps += 1  # Zählt den Tausch nur, wenn ein kleineres Element gefunden wurde
                self.data[minimum], self.data[i] = self.data[i], self.data[minimum]

            # Visualisiert den aktuellen Zustand des Arrays mit Farbcodierung
            graph_manager.notify(self.data, [YELLOW if x == minimum or x == i else BLUE for x in range(len(self.data))])
            time.sleep(self.time_tick)  # Wartet für die Visualisierung

        # Endgültige Visualisierung nach Abschluss des Sortiervorgangs
        graph_manager.notify(self.data, [BLUE for x in range(len(self.data))])
        return steps  # Gibt die Gesamtzahl der Schritte zurück
