from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Definiert eine abstrakte Basisklasse für Observer im Observer-Entwurfsmuster.

    Das Observer-Muster ist ein Software-Entwurfsmuster, bei dem ein Objekt, bekannt als Subject,
    eine Liste von Abhängigkeiten, den sogenannten Observers, verwaltet. Wann immer der Zustand
    des Subjects sich ändert, werden alle seine Observer darüber benachrichtigt und automatisch aktualisiert.

    Diese Klasse dient als abstrakte Basisklasse für alle Observer, die über Änderungen informiert
    werden müssen. Jeder konkrete Observer muss diese Klasse erben und die `update`-Methode implementieren.
    """

    @abstractmethod
    def update(self, data, color_array) -> None:
        """
        Wird aufgerufen, um den Observer über Änderungen zu informieren.

        Jeder konkrete Observer muss diese Methode implementieren, um auf Änderungen reagieren zu können,
        die vom Subject gemeldet werden. Diese Methode wird typischerweise vom Subject aufgerufen,
        um den Observer über Änderungen im Zustand des Subjects zu informieren.

        :param data: Die Daten, die vom Subject gesendet werden. Die genaue Bedeutung und Struktur
                     der Daten hängt vom spezifischen Anwendungsfall ab.
        :param color_array: Ein Array oder eine Liste von Farben, die zur Visualisierung oder weiteren
                            Verarbeitung der Daten verwendet werden können.
        """
        pass
