import os
from tkinter import END, messagebox
import re

from controller import Controller

class Import:

    def import_data(self, text_ranking):
        """
        Importiert Ranking-Daten aus einer Textdatei und zeigt sie im übergebenen Text-Widget an.

        :param text_ranking: Das Text-Widget, in das die importierten Daten eingefügt werden sollen.
        """
        # Pfad zum 'data' Ordner und der Datei 'ranking_export.txt' wird generiert.
        data_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
        filename = os.path.join(data_directory, 'ranking_export.txt')

        # Überprüfe, ob die Datei existiert und führe den Import durch.
        if os.path.exists(filename):
            text_ranking.delete('1.0', END)  # Lösche aktuellen Inhalt im Text-Widget.
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()  # Lese den Inhalt der Datei.
                text_ranking.insert(END, content)  # Füge den Inhalt in das Text-Widget ein.
            messagebox.showinfo("Import Erfolgreich", "Alle Daten wurden erfolgreich importiert.")
        else:
            messagebox.showwarning("Importfehler", "Keine Datei für den Import gefunden.")

    def handle_import(self, text_ranking, ranking):
        """
        Verarbeitet den Import von Daten, parst den Inhalt und aktualisiert das übergebene Ranking-Dictionary.

        :param text_ranking: Das Text-Widget, aus dem die Daten gelesen werden.
        :param ranking: Das Dictionary, das aktualisiert wird, basierend auf den importierten und geparsten Daten.
        """
        controller = Controller()
        self.import_data(text_ranking)  # Führt den Importprozess durch.

        # Parsen des Textinhalts und Extrahieren der relevanten Daten.
        content = text_ranking.get('1.0', 'end-1c')
        lines = content.split('\n')
        for line in lines:
            parts = line.split(':')
            if len(parts) == 2:
                algo_name_with_number = parts[0].strip()
                # Entferne Nummerierung vor Algorithmennamen.
                algo_name = re.sub(r"^\d+\.\s*", "", algo_name_with_number)
                steps = parts[1].strip().replace('Schritte', '').strip()  # Entferne das Wort "Schritte" und whitespace.
                # Aktualisiere das Ranking-Dictionary mit den extrahierten Daten.
                if algo_name not in ranking:
                    ranking[algo_name] = [int(steps)]
                else:
                    ranking[algo_name].append(int(steps))
        controller.update_ranking(text_ranking, ranking)  # Aktualisiere das UI basierend auf dem neuen Ranking.
