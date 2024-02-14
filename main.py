import tkinter

from controller import Controller as controller
from algorithms.bubble_sort import BubbleSort
from algorithms.counting_sort import CountingSort
from algorithms.heap_sort import HeapSort
from algorithms.insertion_sort import InsertionSort
from algorithms.merge_sort import MergeSort
from algorithms.quick_sort import QuickSort
from algorithms.selection_sort import SelectionSort
import constants
from graphmanager.graph import Graph
from graphmanager.graph_manager import GraphManager
from translation import Translations
from ui_components import UIComponents


def main():
    # Initialisierung der Steuerelemente für die Benutzeroberfläche
    algorithm_name = tkinter.StringVar()  # Auswahl des Sortieralgorithmus
    speed_name = tkinter.StringVar()  # Geschwindigkeit der Visualisierung
    array_size = tkinter.IntVar(value=100)  # Größe des zu sortierenden Arrays
    steps = tkinter.IntVar(value=0)  # Anzahl der durchgeführten Schritte
    ranking = {}  # Speichert Ranginformationen, z.B. für Vergleichszwecke
    speed_list = [constants.SPEED_MENU_FAST, constants.SPEED_MENU_MEDIUM,
                  constants.SPEED_MENU_SLOW]  # Geschwindigkeitsoptionen

    ui_components = UIComponents()

    # Zeitintervall basierend auf der ausgewählten Geschwindigkeit
    time_tick = controller.set_speed(ui_components.speed_menu)
    algo_list, algo_names = initialize_algo_list(time_tick)
    ui_components.setup_gui(speed_name, speed_list, algorithm_name, algo_names, steps, ranking, algo_list, array_size)

    # Erstellung und Konfiguration des Graph-Objekts zur Visualisierung
    graph_manager = GraphManager()
    graph = Graph(ui_components.canvas, ui_components.window)
    graph_manager.attach(graph)  # Verknüpfung des Graph-Objekts mit dem GraphManager

    # Einrichtung der Übersetzungsfunktionen und Datenimport/-export
    translations = Translations()

    # Setzt die Standardsprache
    translations.set_language(constants.LANGUAGE_EN, ui_components)

    ui_components.window.mainloop()


def initialize_algo_list(time_tick):
    # Initialisierung der Sortieralgorithmen mit dem eingestellten Zeitintervall
    bubble_sort = BubbleSort(time_tick=time_tick)
    counting_sort = CountingSort(time_tick=time_tick)
    heap_sort = HeapSort(time_tick=time_tick)
    insertion_sort = InsertionSort(time_tick=time_tick)
    merge_sort = MergeSort(time_tick=time_tick)
    quick_sort = QuickSort(time_tick=time_tick)
    selection_sort = SelectionSort(time_tick=time_tick)

    # Mapping der Algorithmusnamen zu den entsprechenden Objekten
    algo_list = [{constants.BUBBLE_SORT: bubble_sort},
                 {constants.COUNTING_SORT: counting_sort},
                 {constants.HEAP_SORT: heap_sort},
                 {constants.INSERTION_SORT: insertion_sort},
                 {constants.MERGE_SORT: merge_sort},
                 {constants.QUICK_SORT: quick_sort},
                 {constants.SELECTION_SORT: selection_sort}]
    algo_names = [list(d.keys())[0] for d in algo_list]  # Extraktion der Namen für die UI

    return algo_list, algo_names


main()
