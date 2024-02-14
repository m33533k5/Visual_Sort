from tkinter import *
from tkinter import ttk
import random
from colors import *

# Importing algorithms
from backup.algorithms.bubbleSort import bubble_sort
from backup.algorithms.selectionSort import selection_sort
from backup.algorithms.insertionSort import insertion_sort
from backup.algorithms.mergeSort import merge_sort
from backup.algorithms.quickSort import quick_sort
from backup.algorithms.heapSort import heap_sort
from backup.algorithms.countingSort import counting_sort
from tooltip import create_tooltip

# Main window
window = Tk()
window.title("Sorting Algorithms Visualization")
window.config(bg = LIGHT_GREEN)

algorithm_name = StringVar()
speed_name = StringVar()
array_size = IntVar()
steps = IntVar(value=0)
ranking = {}
data = []
algo_list = ['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort', 'Counting Sort']
speed_list = ['Fast', 'Medium', 'Slow']

# Drawing the numerical array as bars
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()

# Randomly generate array
def generate():
    global data
    size = array_size.get()

    # Erzeugt eine Liste einzigartiger Zahlen von 1 bis 'size'
    data = random.sample(range(1, size+1), size)

    drawData(data, [BLUE for x in range(len(data))])

def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.3
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.001

def sort():
    global data, ranking
    timeTick = set_speed()
    step_count = 0

    algo_name = algo_menu.get()

    if algo_name == 'Bubble Sort':
        step_count = bubble_sort(data, drawData, timeTick)
    elif algo_name == 'Selection Sort':
        step_count = selection_sort(data, drawData, timeTick)
    elif algo_name == 'Insertion Sort':
        step_count = insertion_sort(data, drawData, timeTick)
    elif algo_name == 'Merge Sort':
        step_count = merge_sort(data, 0, len(data)-1, drawData, timeTick)
    elif algo_name == 'Quick Sort':
        step_count = quick_sort(data, 0, len(data)-1, drawData, timeTick)
    elif algo_name == 'Heap Sort':
        step_count = heap_sort(data, drawData, timeTick)
    else:
        step_count = counting_sort(data, drawData, timeTick)

    steps.set(step_count)
    
    # Prüfe, ob der Algorithmus bereits im Dictionary ist, und füge die Schritte hinzu
    if algo_name not in ranking:
        ranking[algo_name] = [step_count]
    else:
        ranking[algo_name].append(step_count)

    update_ranking()  # Aktualisiere die Anzeige der Rangliste

def update_ranking():
    text_ranking.delete('1.0', END)  # Lösche den aktuellen Inhalt des Text-Widgets
    
    # Erstelle eine flache Liste aller Schritte
    alle_schritte = []
    for algorithmus, schritte_liste in ranking.items():
        for schritte in schritte_liste:
            alle_schritte.append((algorithmus, schritte))
    
    # Sortiere die Liste der Schritte
    sortierte_schritte = sorted(alle_schritte, key=lambda x: x[1])
    
    # Zeige die sortierten Schritte mit Platzierung an
    position = 1
    for algorithmus, schritte in sortierte_schritte:
        text_ranking.insert(END, f"{position}. {algorithmus}: {schritte} Schritte\n")
        position = position + 1

# User interface setup
canvas = Canvas(window, width=800, height=400, bg=YELLOW)
canvas.grid(row=0, column=0, padx=10, pady=5)
create_tooltip(canvas, "Area for the visualized representation")

# UI Frame in dem die nachfolgenden Elemente platziert werden
UI_frame = Frame(window, width=400, height=400, bg=PINK)
UI_frame.grid(row=0, column=1, padx=10, pady=5)

# Auswahl Algorithmus
label_algorithm = Label(UI_frame, text="Algorithm: ", bg=WHITE)
label_algorithm.place(x=10, y=10, width=150, height=25)
create_tooltip(label_algorithm, "Selection of the algorithms")

algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.place(x=220, y=10, width=150, height=25)
create_tooltip(algo_menu, "Algorithms available for selection") 
algo_menu.current(0)

# Auswahl Geschwindigkeit
label_speed = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
label_speed.place(x=10, y=45, width=150, height=25)
create_tooltip(label_speed, "Selection of the speed") 

speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.place(x=220, y=45, width=150, height=25)
create_tooltip(speed_menu, "Speed available for selection") 
speed_menu.current(0)

# Größe des Feldes 
label_size = Label(UI_frame, text="Array Size: ", bg=WHITE)
label_size.place(x=10, y=80, width=150, height=25)
create_tooltip(label_size, "Size of the field that is sorted") 

size_entry = Entry(UI_frame, textvariable=array_size)
size_entry.place(x=220, y=80, width=150, height=25)
create_tooltip(size_entry, "Field for adjusting the field size") 
array_size.set(100)  # Standardgröße

# Schritte Widget
label_steps = Label(UI_frame, text="Steps: ", bg=WHITE)
label_steps.place(x=10, y=115, width=150, height=25)
create_tooltip(label_steps, "Number of steps required to sort the field") 

size_steps = Entry(UI_frame, textvariable=steps, state='readonly')
size_steps.place(x=220, y=115, width=150, height=25)
create_tooltip(size_steps, "Number of steps required to sort the field") 

# Button Erzeugung Daten
bbutton_generate = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_GRAY)
bbutton_generate.place(x=10, y=155, width=100, height=30)
create_tooltip(bbutton_generate, "Button for creating an array with randomly generated values") 

# Button Sortierung
button_sort = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_GRAY)
button_sort.place(x=120, y=155, width=100, height=30)
create_tooltip(button_sort, "Button to start the sorting process") 

# Rangliste Text-Widget
label_ranking = Label(UI_frame, text="Ranking: ", bg=WHITE)
label_ranking.place(x=10, y=190, width=150, height=25)
create_tooltip(label_ranking, "Ranking list for algorithms")

text_ranking = Text(UI_frame, height=10, width=35)
text_ranking.place(x=10, y=225, width=375, height=150)
create_tooltip(text_ranking, "Ranking list values") 

window.mainloop()