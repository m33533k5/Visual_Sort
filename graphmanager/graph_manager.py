from abc import ABC, abstractmethod
from typing import List

from graphmanager.observer import Observer


class Manager(ABC):
    """
    Definiert eine abstrakte Basisklasse für das Subject im Observer-Entwurfsmuster.

    Im Rahmen des Observer-Musters dient das Subject dazu, eine Liste von Observers zu verwalten,
    die über Zustandsänderungen informiert werden. Diese Klasse stellt eine Schnittstelle zur Verfügung,
    um Observer zu registrieren, zu entfernen und zu benachrichtigen.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Registriert einen Observer beim Subject.

        :param observer: Der zu registrierende Observer.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Entfernt einen Observer aus der Beobachtungsliste des Subjects.

        :param observer: Der zu entfernende Observer.
        """
        pass

    @abstractmethod
    def notify(self, data, color_array, time_tick) -> None:
        """
        Benachrichtigt alle registrierten Observer über eine Zustandsänderung.

        :param data: Die geänderten Daten, die den Observers übermittelt werden.
        :param color_array: Eine Liste von Farben, die mit den Daten assoziiert sind.
        :param time_tick: Die Verzögerung, die für die Visualisierung verwendet wird.
        """
        pass


class GraphManager(Manager):
    """
    Konkrete Implementierung eines Subjects, das wichtige Zustandsinformationen hält
    und Observer über Änderungen dieses Zustands benachrichtigt.
    """

    def __init__(self):
        """
        Initialisiert eine neue Instanz des GraphManagers.
        """
        self.data = []  # Der Zustand des Subjects, wichtig für alle Observer.
        self.color_array = []  # Zusätzliche Zustandsinformationen, wie Farbinformationen.
        self.time_tick = None  # Verzögerung für die Visualisierung.
        self.observers: List[Observer] = []  # Liste der registrierten Observer.

    def attach(self, observer: Observer) -> None:
        """
        Fügt einen neuen Observer zur Beobachtungsliste hinzu.

        :param observer: Der Observer, der hinzugefügt wird.
        """
        self.observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """
        Entfernt einen Observer aus der Beobachtungsliste.

        :param observer: Der Observer, der entfernt wird.
        """
        self.observers.remove(observer)

    def notify(self, data, color_array) -> None:
        """
        Benachrichtigt alle Observer über Zustandsänderungen, indem die `update`-Methode jedes Observers aufgerufen wird.

        :param data: Die geänderten Daten.
        :param color_array: Die Liste der Farben assoziiert mit den Daten.
        """
        # Aktualisiert den internen Zustand vor der Benachrichtigung.
        self.data = data
        self.color_array = color_array

        # Ruft die `update`-Methode jedes registrierten Observers auf.
        for observer in self.observers:
            observer.update(data, color_array)
