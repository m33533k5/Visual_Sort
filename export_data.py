import os
from tkinter import END, messagebox


class Export:
    def export_data(self, text_ranking):
        """
        Exportiert die im Text-Widget angezeigten Daten in eine Textdatei.

        :param text_ranking: Das Text-Widget, aus dem die Daten exportiert werden.
        """
        # Generiere den Pfad zum 'data' Ordner relativ zum Skriptverzeichnis.
        data_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

        # Erstelle den 'data' Ordner, falls er noch nicht existiert.
        if not os.path.exists(data_directory):
            os.makedirs(data_directory)

        # Der Dateiname, unter dem die exportierten Daten gespeichert werden.
        filename = os.path.join(data_directory, 'ranking_export.txt')

        # Extrahiere den Text aus dem Text-Widget für den Export.
        text_to_export = text_ranking.get('1.0', END)

        # Entferne alle Leerzeilen, um den exportierten Inhalt zu bereinigen.
        lines = text_to_export.split('\n')
        non_empty_lines = [line for line in lines if line.strip() != ""]
        text_to_export = "\n".join(non_empty_lines)

        try:
            # Schreibe den bereinigten Text in die Exportdatei.
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(text_to_export + "\n")
            # Zeige eine Bestätigungsnachricht an, um den erfolgreichen Export zu signalisieren.
            messagebox.showinfo("Export Erfolgreich", "Die Rangliste wurde erfolgreich exportiert.")
        except Exception as e:
            # Zeige eine Fehlermeldung, wenn der Exportprozess fehlschlägt.
            messagebox.showerror("Export Fehlgeschlagen",
                                 "Beim Exportieren der Rangliste ist ein Fehler aufgetreten.\n" + str(e))
