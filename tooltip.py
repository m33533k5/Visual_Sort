from tkinter import LEFT, SOLID, Label, Toplevel


class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def show_tip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _, _, = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 25
        y = y + self.widget.winfo_rooty() + 20
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hide_tip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
            
# Funktion, um den Tooltip an ein Widget anzuhängen
def create_tooltip(widget, text):
    tooltip = ToolTip(widget)
    def enter(event):
        tooltip.show_tip(text)
    def leave(event):
        tooltip.hide_tip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)
