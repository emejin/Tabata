import tkinter as tk
from controller import Controller
from tabata import Tabata


class View:
    def __init__(self):
        self.model = Tabata()
        self.controller = None

        self.root = tk.Tk()
        self.root.title("Settings")
        self.frame_00 = tk.Frame(self.root, width=300, height=200)
        self.frame_00.grid(row=0, column=0, columnspan=1)
        self.frame_01 = tk.Frame(self.root, width=300, height=200)
        self.frame_01.grid(row=0, column=1, columnspan=1)
        self.frame_10 = tk.Frame(self.root, width=300, height=20)
        self.frame_10.grid(row=1, column=0, columnspan=1)
        self.frame_11 = tk.Frame(self.root, width=300, height=20)
        self.frame_11.grid(row=1, column=1, columnspan=1)
        self.frame_20 = tk.Frame(self.root, width=300, height=200)
        self.frame_20.grid(row=2, column=0, columnspan=1)
        self.frame_21 = tk.Frame(self.root, width=300, height=200)
        self.frame_21.grid(row=2, column=1, columnspan=1)
        self.frame_30 = tk.Frame(self.root, width=300, height=20)
        self.frame_30.grid(row=3, column=0, columnspan=1)
        self.frame_31 = tk.Frame(self.root, width=300, height=20)
        self.frame_31.grid(row=3, column=1, columnspan=1)
        self.frame4 = tk.Frame(self.root, width=600, height=20)
        self.frame4.grid(row=4, column=0, columnspan=2)

        vcmd = (self.root.register(self.isnumber))
        self.exercise = tk.StringVar(value='30')
        tk.Entry(self.root, textvariable=self.exercise, validate='all', validatecommand=(vcmd, '%P')).grid(row=0, column=0)
        self.rest = tk.StringVar(value='15')
        tk.Entry(self.root, textvariable=self.rest, validate='all', validatecommand=(vcmd, '%P')).grid(row=0, column=1)
        tk.Label(self.root, text="Exercise (s)").grid(row=1, column=0)
        tk.Label(self.root, text="Rest (s)").grid(row=1, column=1)

        self.sets = tk.StringVar(value='8')
        tk.Entry(self.root, textvariable=self.sets, validate='all', validatecommand=(vcmd, '%P')).grid(row=2, column=0)
        self.cycles = tk.StringVar(value='5')
        tk.Entry(self.root, textvariable=self.cycles, validate='all', validatecommand=(vcmd, '%P')).grid(row=2, column=1)
        tk.Label(self.root, text="Number of sets").grid(row=3, column=0)
        tk.Label(self.root, text="Number of cycles").grid(row=3, column=1)

        self.b = tk.Button(self.root, text="Start Exercise", command=self.start)
        self.b.grid(row=4, column=0, columnspan=2)

    def isnumber(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False

    def start(self):
        num_cycles = self.model.set_num_cycles(int(self.cycles.get()))
        num_sets = self.model.set_num_sets(int(self.sets.get()))
        exercise_t = self.model.set_exercise_time(int(self.exercise.get()))
        rest_t = self.model.set_rest_time(int(self.rest.get()))

        self.root.wm_state('iconic')

        newWindow = tk.Toplevel(self.root)
        wv = WorkoutView(newWindow, exercise_t, num_sets, num_cycles)

        self.controller = Controller(self.model, wv)
        self.controller.run()
        self.open_summary()

    def open_summary(self):
        num_cycles = self.model.get_num_cycles()
        num_sets = self.model.get_num_sets()
        exercise_t = self.model.get_exercise_t()

        mins, secs = divmod(num_cycles*num_sets*exercise_t, 60)
        duration = '{:02d}:{:02d}'.format(mins, secs)

        newWindow = tk.Toplevel(self.root)
        SummaryView(newWindow, duration)

        self.root.mainloop()

class WorkoutView:
    def __init__(self, root, t, num_sets, num_cycles):
        self.root = root
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

    # Obj is instance of tk.Label. Color is a string.
    def change_color(self, color):
        self.timer_label.configure(fg=color)
        self.root.update()

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
    view = View()
    view.root.mainloop()


if __name__ == "__main__":
    main()

