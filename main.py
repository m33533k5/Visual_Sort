import tkinter
from tkinter import ttk

from controller import Controller
from import_data import Import
from algorithms.bubble_sort import BubbleSort
from algorithms.counting_sort import CountingSort
from algorithms.heap_sort import HeapSort
from algorithms.insertion_sort import InsertionSort
from algorithms.merge_sort import MergeSort
from algorithms.quick_sort import QuickSort
from algorithms.selection_sort import SelectionSort
import constants
import export_data
from graphmanager.graph import Graph
from graphmanager.graph_manager import GraphManager
from translation import Translations
from ui_components import UIComponents


# Hauptfenster-Einstellungen
window = tkinter.Tk()
window.config(bg=constants.LIGHT_GREEN)  # Hintergrundfarbe des Hauptfensters

# Einrichtung der Benutzeroberfläche
canvas = tkinter.Canvas(window, width=800, height=425, bg=constants.YELLOW)  # Zeichenfläche für die Visualisierung
canvas.grid(row=0, column=0, padx=10, pady=5)

# UI-Frame für Steuerelemente und Informationen
ui_frame = tkinter.Frame(window, width=400, height=425, bg=constants.PINK)
ui_frame.grid(row=0, column=1, padx=10, pady=5)

# Initialisierung der Steuerelemente für die Benutzeroberfläche
algorithm_name = tkinter.StringVar()  # Auswahl des Sortieralgorithmus
speed_name = tkinter.StringVar()  # Geschwindigkeit der Visualisierung
array_size = tkinter.IntVar(value=100)  # Größe des zu sortierenden Arrays
steps = tkinter.IntVar(value=0)  # Anzahl der durchgeführten Schritte
ranking = {}  # Speichert Ranginformationen, z.B. für Vergleichszwecke
speed_list = [constants.SPEED_MENU_FAST, constants.SPEED_MENU_MEDIUM,
              constants.SPEED_MENU_SLOW]  # Geschwindigkeitsoptionen

# Konfiguration der Dropdown-Menüs für Algorithmusauswahl und Geschwindigkeit
speed_menu = ttk.Combobox(ui_frame, textvariable=speed_name, values=speed_list)
speed_menu.place(x=220, y=45, width=150, height=25)
speed_menu.current(0)  # Standardauswahl

# Erstellung und Konfiguration des Graph-Objekts zur Visualisierung
graph = Graph(canvas, window)
graph_manager = GraphManager()
graph_manager.attach(graph)  # Verknüpfung des Graph-Objekts mit dem GraphManager

# Controller für die Verwaltung von Aktionen wie Generieren und Sortieren
controller = Controller()

# Zeitintervall basierend auf der ausgewählten Geschwindigkeit
time_tick = controller.set_speed(speed_menu)

# Initialisierung der Sortieralgorithmen mit dem eingestellten Zeitintervall
bubble_sort = BubbleSort(time_tick)
counting_sort = CountingSort(time_tick)
heap_sort = HeapSort(time_tick)
insertion_sort = InsertionSort(time_tick)
merge_sort = MergeSort(time_tick)
quick_sort = QuickSort(time_tick)
selection_sort = SelectionSort(time_tick)

# Mapping der Algorithmusnamen zu den entsprechenden Objekten
algo_list = [{constants.BUBBLE_SORT: bubble_sort},
             {constants.COUNTING_SORT: counting_sort},
             {constants.HEAP_SORT: heap_sort},
             {constants.INSERTION_SORT: insertion_sort},
             {constants.MERGE_SORT: merge_sort},
             {constants.QUICK_SORT: quick_sort},
             {constants.SELECTION_SORT: selection_sort}]
algo_names = [list(d.keys())[0] for d in algo_list] # Extraktion der Namen für die UI

# Einrichtung der Übersetzungsfunktionen und Datenimport/-export
translations = Translations()
handle_import = Import()
handle_export = export_data.Export()

# UI-Komponenten für die Anzeige und Interaktion
label_algorithm = tkinter.Label(ui_frame)
label_algorithm.place(x=10, y=10, width=150, height=25)
label_speed = tkinter.Label(ui_frame)
label_speed.place(x=10, y=45, width=150, height=25)
label_size = tkinter.Label(ui_frame)
label_size.place(x=10, y=80, width=150, height=25)
label_steps = tkinter.Label(ui_frame)
label_steps.place(x=10, y=115, width=150, height=25)
label_ranking = tkinter.Label(ui_frame)
label_ranking.place(x=10, y=190, width=150, height=25)
algo_menu = ttk.Combobox(ui_frame, textvariable=algorithm_name, values=algo_names)
algo_menu.place(x=220, y=10, width=150, height=25)
algo_menu.current(0)
button_generate = tkinter.Button(ui_frame, command=lambda: controller.generate(canvas, window, array_size))
button_generate.place(x=10, y=155, width=100, height=30)
button_sort = tkinter.Button(ui_frame, command=lambda: controller.sort(ui_components, steps, ranking, algo_list))
button_sort.place(x=120, y=155, width=100, height=30)
button_german_translation = tkinter.Button(ui_frame, command=lambda: translations.set_language(constants.LANGUAGE_DE, ui_components))
button_german_translation.place(x=270, y=155, width=100, height=30)
button_english_translation = tkinter.Button(ui_frame, command=lambda: translations.set_language(constants.LANGUAGE_EN, ui_components))
button_english_translation.place(x=270, y=190, width=100, height=30)
size_entry = tkinter.Entry(ui_frame, textvariable=array_size)
size_entry.place(x=220, y=80, width=150, height=25)
size_steps = tkinter.Entry(ui_frame, textvariable=steps, state=constants.STATE_READONLY)
size_steps.place(x=220, y=115, width=150, height=25)
text_ranking = tkinter.Text(ui_frame, height=10, width=35)
text_ranking.place(x=10, y=225, width=360, height=150)
button_import = tkinter.Button(ui_frame, command=lambda: handle_import.handle_import(text_ranking, ranking),
                               text=constants.BUTTON_TEXT_IMPORT, bg=constants.LIGHT_GRAY)
button_import.place(x=10, y=385, width=100, height=30)
button_export = tkinter.Button(ui_frame, command=lambda: handle_export.export_data(text_ranking),
                               text=constants.BUTTON_TEXT_EXPORT, bg=constants.LIGHT_GRAY)
button_export.place(x=120, y=385, width=100, height=30)

# Erstellung der UIComponents-Instanz für vereinfachte Parameterübergabe
ui_components = UIComponents(canvas, window, label_algorithm, algo_menu, label_speed, speed_menu, label_size,
                             size_entry, label_steps, size_steps, label_ranking, text_ranking, button_generate,
                             button_sort, button_german_translation, button_english_translation)

# Setzt die Standardsprache
translations.set_language(constants.LANGUAGE_EN, ui_components)

window.mainloop()

#if __name__ == '__main__':
    # Der Block wird ausgeführt, wenn das Skript direkt aufgerufen wird,
    # und nicht, wenn es als Modul in einem anderen Skript importiert wird.

    #profile_filename = 'program.prof'  # Name der Datei, in der die Profilergebnisse gespeichert werden.

    # Führt die Hauptfunktion 'main()' unter Verwendung von cProfile aus, um die Leistung zu analysieren.
    # Die Ergebnisse werden in der Datei 'program.prof' gespeichert.
    #cProfile.run('main()', profile_filename)

    # Verwendet das subprocess-Modul, um snakeviz zu starten, ein Tool zur Visualisierung der Profilergebnisse.
    # Dies ermöglicht eine detaillierte Analyse der Programmausführung und Leistung.
    #process = subprocess.run(['snakeviz', profile_filename])

    # python -m cProfile -o program.prof main.py
    # python -m snakeviz program.prof
