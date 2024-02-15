import tkinter
import i18n

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
    i18n.load_path.append(".\\locales")
    i18n.set("file_format", "yml")
    i18n.set("filename_format", "{namespace}.{format}")
    i18n.set("skip_locale_root_data", True)
    i18n.set("use_locale_dirs", True)
    i18n.set('fallback', 'en')
    i18n.set('locale', 'de')

    # Initialisierung der Steuerelemente für die Benutzeroberfläche
    algorithm_name = tkinter.StringVar()  # Auswahl des Sortieralgorithmus
    array_size = tkinter.IntVar(value=100)  # Größe des zu sortierenden Arrays
    steps = tkinter.IntVar(value=0)  # Anzahl der durchgeführten Schritte
    ranking = {}  # Speichert Ranginformationen, z.B. für Vergleichszwecke

    ui_components = UIComponents()

    # Zeitintervall basierend auf der ausgewählten Geschwindigkeit
    algo_list, algo_names = initialize_algo_list()
    ui_components.set_list(algo_list)
    ui_components.setup_gui(algorithm_name, algo_names, steps, ranking, algo_list, array_size)

    # Erstellung und Konfiguration des Graph-Objekts zur Visualisierung
    graph_manager = GraphManager()
    graph = Graph(ui_components.canvas, ui_components.window)
    graph_manager.attach(graph)  # Verknüpfung des Graph-Objekts mit dem GraphManager

    ui_components.window.mainloop()


def initialize_algo_list():
    # Initialisierung der Sortieralgorithmen mit dem eingestellten Zeitintervall
    bubble_sort = BubbleSort()
    counting_sort = CountingSort()
    heap_sort = HeapSort()
    insertion_sort = InsertionSort()
    merge_sort = MergeSort()
    quick_sort = QuickSort()
    selection_sort = SelectionSort()

    # Mapping der Algorithmusnamen zu den entsprechenden Objekten
    algo_list = [{BUBBLE_SORT: bubble_sort},
                 {COUNTING_SORT: counting_sort},
                 {HEAP_SORT: heap_sort},
                 {INSERTION_SORT: insertion_sort},
                 {MERGE_SORT: merge_sort},
                 {QUICK_SORT: quick_sort},
                 {SELECTION_SORT: selection_sort}]
    algo_names = [list(d.keys())[0] for d in algo_list]  # Extraktion der Namen für die UI


    return algo_list, algo_names


if __name__ == '__main__':
    main()
