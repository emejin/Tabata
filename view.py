import tkinter as tk


class View:
    def __init__(self, t, num_sets, num_cycles):
        self.root = tk.Tk()
        self.frame_t = tk.Frame(self.root, width=600, height=200, background="white").grid(row=0, column=0, columnspan=2)
        self.frame_t_label = tk.Frame(self.root, width=600, height=20, background="white").grid(row=1, column=0, columnspan=2)
        self.frame_s = tk.Frame(self.root, width=300, height=200, background="white").grid(row=2, column=0, columnspan=1)
        self.frame_c = tk.Frame(self.root, width=300, height=200, background="white").grid(row=2, column=1, columnspan=1)
        self.frame_s_label = tk.Frame(self.root, width=300, height=20, background="white").grid(row=3, column=0, columnspan=1)
        self.frame_c_label = tk.Frame(self.root, width=300, height=20, background="white").grid(row=3, column=1,
                                                                                           columnspan=1)


        self.timer = tk.StringVar(value=t)
        tk.Label(self.frame_t, textvariable=self.timer, borderwidth=10, font=("Arial", 164, "bold")).grid(row=0, column=0, columnspan=2)

        self.exercise_rest_label = tk.StringVar(value="Exercise")
        tk.Label(self.frame_t_label, textvariable=self.timer, borderwidth=10, font=("Arial", 54, "bold")).grid(row=1, column=0, columnspan=2)

        self.sets = tk.StringVar(value=num_sets)
        tk.Label(self.frame_s, textvariable=self.sets, borderwidth=1, font=("Arial", 96, "bold")).grid(row=2, column=0, columnspan=1)

        self.cycles = tk.StringVar(value=num_cycles)
        tk.Label(self.frame_c, textvariable=self.cycles, borderwidth=1, font=("Arial", 96, "bold")).grid(row=2, column=1, columnspan=1)

        tk.Label(self.frame_s_label, text="Set", borderwidth=1, font=("Arial", 44, "bold")).grid(row=3, column=0,
                                                                                                 columnspan=1)

        tk.Label(self.frame_c_label, text="Cycle", borderwidth=1, font=("Arial", 44, "bold")).grid(row=3, column=1,
                                                                                             columnspan=1)
    # Obj is instance of StringVar.
    def update(self, obj, text):
        obj.set(text)
        self.root.update()
        print("Updated: ", obj, " to: ", text)

    def test(self):
        self.root.mainloop()


def main():
    view = View(1, 2, 3)
    view.test()


if __name__ == "__main__":
    main()
