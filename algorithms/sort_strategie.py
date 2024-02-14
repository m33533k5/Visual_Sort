from abc import abstractmethod

from graphmanager.graph_manager import GraphManager

class Sort_Algorithm():
    """
    Eine abstrakte Basisklasse, die das Strategy-Designmuster für Sortieralgorithmen implementiert,
    sowie das Prototype-Pattern für die Initialisierung mit Daten.

    Das Strategy-Pattern ermöglicht die Definition einer Familie von Algorithmen, kapselt jeden
    Algorithmus und macht sie austauschbar. Sort_Algorithm definiert das Interface für die
    Sortieralgorithmen, die im Kontext der Anwendung genutzt werden können.

    Gleichzeitig verwendet die Klasse das Prototype-Pattern, indem sie eine Vorlage für die
    Initialisierung der Algorithmen mit Daten bietet, die sortiert werden sollen, und ermöglicht
    das Zurücksetzen der Daten auf ihren ursprünglichen Zustand.
    """

    def __init__(self, time_tick):
        """
        Initialisiert ein Sort_Algorithm-Objekt mit einer Zeitverzögerung für die Visualisierung.

        :param time_tick: Die Zeitverzögerung zwischen den Sortierschritten.
        """
        self.time_tick = time_tick  # Zeitverzögerung für die Visualisierung
        self.data = []  # Die zu sortierenden Daten
        self.data_orig = []  # Kopie der Originaldaten zur Wiederherstellung

    @abstractmethod
    def sort(self, graph_manager: GraphManager, data):
        """
        Abstrakte Methode, die von konkreten Sortieralgorithmen implementiert werden muss.

        :param graph_manager: Der GraphManager, der für die Visualisierung des Sortiervorgangs verwendet wird.
        :param data: Die zu sortierenden Daten.
        """
        pass

    def set_data(self, data):
        """
        Initialisiert den Sortieralgorithmus mit Daten.

        :param data: Die zu sortierenden Daten.
        """
        self.data = data
        self.data_orig = list(data)  # Erstellt eine Kopie der Originaldaten

    def reset(self):
        """
        Setzt die Daten auf ihren ursprünglichen Zustand zurück, basierend auf der Kopie der Originaldaten.
        """
        self.data = list(self.data_orig)  # Stellt die Originaldaten wieder her

    def set_time_tick(self, time_tick):
        """
        Aktualisiert die Zeitverzögerung für die Visualisierung des Sortiervorgangs.

        :param time_tick: Die neue Zeitverzögerung zwischen den Sortierschritten.
        """
        self.time_tick = time_tick
