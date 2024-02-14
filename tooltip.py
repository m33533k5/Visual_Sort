from tkinter import LEFT, SOLID, Label, Toplevel


class ToolTip(object):
    def __init__(self, widget):
        """
        Initialisiert eine neue Instanz der ToolTip-Klasse.

        :param widget: Das Widget, an das dieser Tooltip angehängt wird.
        """
        self.widget = widget
        self.top_window = None
        self.id = None
        self.x = self.y = 0

    def show_tip(self, text):
        """
        Zeigt den Tooltip mit dem gegebenen Text an.

        :param text: Der anzuzeigende Text im Tooltip.
        """
        self.text = text
        if self.top_window or not self.text:  # Verhindert die Anzeige eines leeren Tooltips oder das erneute Öffnen
            return
        x, y, _, _, = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 25  # Berechnet die X-Position für den Tooltip
        y = y + self.widget.winfo_rooty() + 20  # Berechnet die Y-Position für den Tooltip
        self.top_window = tw = Toplevel(self.widget)  # Erstellt ein neues Toplevel-Fenster für den Tooltip
        tw.wm_overrideredirect(True)  # Entfernt die Fensterdekoration
        tw.wm_geometry("+%d+%d" % (x, y))  # Setzt die Position des Tooltip-Fensters
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))  # Erstellt das Label mit dem Tooltip-Text
        label.pack(ipadx=1)  # Packt das Label in das Toplevel-Fenster

    def hide_tip(self):
        """
        Versteckt den aktuell angezeigten Tooltip.
        """
        tw = self.top_window
        self.top_window = None
        if tw:  # Überprüft, ob ein Tooltip-Fenster existiert und zerstört es
            tw.destroy()

    # Funktion, um den Tooltip an ein Widget anzuhängen
    def create_tooltip(widget, text):
        """
        Erstellt und bindet einen Tooltip an das gegebene Widget.

        :param widget: Das Widget, an das der Tooltip gebunden wird.
        :param text: Der Text, der im Tooltip angezeigt wird.
        """
        tooltip = ToolTip(widget)  # Erstellt eine neue Tooltip-Instanz

        def enter(event):
            tooltip.show_tip(text)  # Zeigt den Tooltip beim Hovern über das Widget

        def leave(event):
            tooltip.hide_tip()  # Versteckt den Tooltip, wenn der Mauszeiger das Widget verlässt

        widget.bind('<Enter>', enter)  # Bindet das Mouse-Enter-Ereignis
        widget.bind('<Leave>', leave)  # Bindet das Mouse-Leave-Ereignis
