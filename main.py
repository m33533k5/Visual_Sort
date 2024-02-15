import tkinter  # Importiert das tkinter Modul für die GUI
import i18n  # Importiert das i18n Modul für die Internationalisierung

# Importiert verschiedene Komponenten und Algorithmen
from constants import *
from controller import Controller
from algorithms.bubble_sort import BubbleSort
from algorithms.counting_sort import CountingSort
from algorithms.heap_sort import HeapSort
from algorithms.insertion_sort import InsertionSort
from algorithms.merge_sort import MergeSort
from algorithms.quick_sort import QuickSort
from algorithms.selection_sort import SelectionSort
from graphmanager.graph import Graph
from graphmanager.graph_manager import GraphManager
from ui_components import UIComponents

def main():
    # Konfiguriert den Pfad und die Einstellungen für die Internationalisierung
    i18n.load_path.append(".\\locales")
    i18n.set("file_format", "yml")
    i18n.set("filename_format", "{namespace}.{format}")
    i18n.set("skip_locale_root_data", True)
    i18n.set("use_locale_dirs", True)
    i18n.set('fallback', 'en')
    i18n.set('locale', 'de')

    # Initialisiert tkinter Variablen und Datenstrukturen
    algorithm_name = tkinter.StringVar()  # Hält die Auswahl des Sortieralgorithmus
    array_size = tkinter.IntVar(value=100)  # Standardgröße des zu sortierenden Arrays
    steps = tkinter.IntVar(value=0)  # Zählt die Anzahl der Sortierschritte
    ranking = {}  # Dient zur Speicherung von Ranginformationen

    # Initialisiert die UI-Komponenten
    ui_components = UIComponents()

    # Initialisiert die Liste der Sortieralgorithmen und deren Namen
    algo_list, algo_names = initialize_algo_list()
    ui_components.set_list(algo_list)
    ui_components.setup_gui(algorithm_name, algo_names, steps, ranking, algo_list, array_size)

    # Erstellt und konfiguriert das Graph-Objekt für die Visualisierung
    graph_manager = GraphManager()
    graph = Graph(ui_components.canvas, ui_components.window)
    graph_manager.attach(graph)  # Verbindet das Graph-Objekt mit dem GraphManager

    # Startet die tkinter Event-Schleife
    ui_components.window.mainloop()

def initialize_algo_list():
    # Erstellt Instanzen der Sortieralgorithmen
    bubble_sort = BubbleSort()
    counting_sort = CountingSort()
    heap_sort = HeapSort()
    insertion_sort = InsertionSort()
    merge_sort = MergeSort()
    quick_sort = QuickSort()
    selection_sort = SelectionSort()

    # Erstellt eine Liste mit den Algorithmen und deren Namen für die UI
    algo_list = [{BUBBLE_SORT: bubble_sort},
                 {COUNTING_SORT: counting_sort},
                 {HEAP_SORT: heap_sort},
                 {INSERTION_SORT: insertion_sort},
                 {MERGE_SORT: merge_sort},
                 {QUICK_SORT: quick_sort},
                 {SELECTION_SORT: selection_sort}]
    algo_names = [list(d.keys())[0] for d in algo_list]  # Extrahiert die Namen der Algorithmen

    return algo_list, algo_names

if __name__ == '__main__':
    main()
