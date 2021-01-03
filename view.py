import tkinter as tk


class View:
    def __init__(self, t, num_sets, num_cycles):
        self.root = tk.Tk()
        self.root.geometry("600x660")
        self.root.title("Tabata Timer")

        self.frame_t = tk.Frame(self.root, width=600, height=200)
        self.frame_t.grid(row=0, column=0, columnspan=2)

        self.frame_t_label = tk.Frame(self.root, width=600, height=20)
        self.frame_t_label.grid(row=1, column=0, columnspan=2)

        self.frame_s = tk.Frame(self.root, width=300, height=200)
        self.frame_s.grid(row=2, column=0, columnspan=1)

        self.frame_c = tk.Frame(self.root, width=300, height=200)
        self.frame_c.grid(row=2, column=1, columnspan=1)

        self.frame_s_label = tk.Frame(self.root, width=300, height=20)
        self.frame_s_label.grid(row=3, column=0, columnspan=1)

        self.frame_c_label = tk.Frame(self.root, width=300, height=20)
        self.frame_c_label.grid(row=3, column=1, columnspan=1)

        mins, secs = divmod(t, 60)
        duration = '{:02d}:{:02d}'.format(mins, secs)

        self.timer = tk.StringVar(value=duration)
        self.timer_label = tk.Label(self.frame_t, textvariable=self.timer, borderwidth=10, font=("Arial", 164, "bold"))
        self.timer_label.grid(row=0, column=0, columnspan=2)

        self.exercise_rest = tk.StringVar(value="Exercise")
        tk.Label(self.root, textvariable=self.exercise_rest, borderwidth=10, font=("Arial", 54, "bold"))\
            .grid(row=1, column=0, columnspan=2)

        self.sets = tk.StringVar(value=num_sets)
        tk.Label(self.root, textvariable=self.sets, borderwidth=1, font=("Arial", 96, "bold")).grid(row=2, column=0,
                                                                                                    columnspan=1)

        self.cycles = tk.StringVar(value=num_cycles)
        tk.Label(self.root, textvariable=self.cycles, borderwidth=1, font=("Arial", 96, "bold")).grid(row=2, column=1,
                                                                                                      columnspan=1)

        tk.Label(self.root, text="Set", borderwidth=1, font=("Arial", 44, "bold")).grid(row=3, column=0, columnspan=1)

        tk.Label(self.root, text="Cycle", borderwidth=1, font=("Arial", 44, "bold")).grid(row=3, column=1, columnspan=1)
    # Obj is instance of StringVar.
    def update(self, obj, text):
        obj.set(text)
        self.root.update()

    #Obj is instance of tk.Label. Color is a string.
    def change_color(self, color):
        self.timer_label.configure(fg=color)
        self.root.update()

    def workout_summary(self, duration):
        summary_root = tk.Toplevel(self.root)
        SummaryView(summary_root, duration)



class SummaryView:
    def __init__(self, root, duration):
        self.root = root
        self.root.title("Workout Summary")
        self.frame1 = tk.Frame(root, width=600, height=20, background="white")
        self.frame1.grid(row=0, column=0)
        tk.Label(self.root, text="Workout duration", font=("Arial", 54, "bold")).grid(row=0, column=0, pady=(100, 10))

        self.frame2 = tk.Frame(root, width=600, height=100, background="white")
        self.frame2.grid(row=1, column=0)
        tk.Label(self.root, text=duration, font=("Arial", 144, "bold")).grid(row=1, column=0, pady=(10, 100))


def main():
    view = View(1, 2, 3)
    view.workout_summary("15:00")
    view.root.mainloop()


if __name__ == "__main__":
    main()

