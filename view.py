import tkinter as tk

class View:
    def __init__(self, t, num_sets, num_cycles):
        self.root = tk.Tk()
        self.frame_t = tk.Frame(self.root, width=600, height=320, background="red").grid(row=0, column=0, columnspan=2)
        self.frame_s = tk.Frame(self.root, width=300, height=320, background="blue").grid(row=1, column=0, columnspan=1)
        self.frame_c = tk.Frame(self.root, width=300, height=320, background="green").grid(row=1, column=1, columnspan=1)

        self.timer = tk.StringVar(value=t)
        tk.Label(self.frame_t, textvariable=self.timer, borderwidth=1).grid(row=0, column=0, columnspan=2)

        self.sets = tk.StringVar(value=num_sets)
        tk.Label(self.frame_s, textvariable=self.sets, borderwidth=1).grid(row=1, column=0, columnspan=1)

        self.cycles = tk.StringVar(value=num_cycles)
        tk.Label(self.frame_c, textvariable=self.cycles, borderwidth=1).grid(row=1, column=1, columnspan=1)

        self.root.mainloop()

    def update(self, t, num_sets, num_cycles):
        self.timer.set(t)
        self.sets.set(num_sets)
        self.cycles.set(num_cycles)

def main():
    view = View(1, 2, 3)

if __name__ == "__main__":
    main()
