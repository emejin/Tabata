import tkinter as tk
from controller import ProperController
from tabata import Tabata

class View(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.controller = None
        self.model = Tabata()

        self.frame = SettingsFrame(self)
        self.frame.grid()

    def change(self, frame, **kwargs):
        self.frame.grid_forget()
        self.frame = frame(self, **kwargs)
        self.frame.grid()

    def update_text(self, obj, text):
        obj.set(text)
        self.update()

        # Obj is instance of tk.Label. Color is a string.

    def change_color(self, obj, color):
        obj.configure(fg=color)
        self.update()

class SettingsFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

        master.title("Settings")
        self.frame_00 = tk.Frame(self, width=300, height=200)
        self.frame_00.grid(row=0, column=0, columnspan=1)
        self.frame_01 = tk.Frame(self, width=300, height=200)
        self.frame_01.grid(row=0, column=1, columnspan=1)
        self.frame_10 = tk.Frame(self, width=300, height=20)
        self.frame_10.grid(row=1, column=0, columnspan=1)
        self.frame_11 = tk.Frame(self, width=300, height=20)
        self.frame_11.grid(row=1, column=1, columnspan=1)
        self.frame_20 = tk.Frame(self, width=300, height=200)
        self.frame_20.grid(row=2, column=0, columnspan=1)
        self.frame_21 = tk.Frame(self, width=300, height=200)
        self.frame_21.grid(row=2, column=1, columnspan=1)
        self.frame_30 = tk.Frame(self, width=300, height=20)
        self.frame_30.grid(row=3, column=0, columnspan=1)
        self.frame_31 = tk.Frame(self, width=300, height=20)
        self.frame_31.grid(row=3, column=1, columnspan=1)
        self.frame4 = tk.Frame(self, width=600, height=20)
        self.frame4.grid(row=4, column=0, columnspan=2)

        vcmd = (self.register(self.isnumber))
        self.exercise = tk.StringVar(value='30')
        tk.Entry(self, textvariable=self.exercise, validate='all', validatecommand=(vcmd, '%P')).grid(row=0, column=0)
        self.rest = tk.StringVar(value='15')
        tk.Entry(self, textvariable=self.rest, validate='all', validatecommand=(vcmd, '%P')).grid(row=0, column=1)
        tk.Label(self, text="Exercise (s)").grid(row=1, column=0)
        tk.Label(self, text="Rest (s)").grid(row=1, column=1)

        self.sets = tk.StringVar(value='8')
        tk.Entry(self, textvariable=self.sets, validate='all', validatecommand=(vcmd, '%P')).grid(row=2, column=0)
        self.cycles = tk.StringVar(value='5')
        tk.Entry(self, textvariable=self.cycles, validate='all', validatecommand=(vcmd, '%P')).grid(row=2, column=1)
        tk.Label(self, text="Number of sets").grid(row=3, column=0)
        tk.Label(self, text="Number of cycles").grid(row=3, column=1)

        self.b = tk.Button(self, text="Ready", command=self.start)
        self.b.grid(row=4, column=0, columnspan=2)

    def isnumber(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False

    def start(self):
        self.master.model.set_num_cycles(int(self.cycles.get()))
        self.master.model.set_num_sets(int(self.sets.get()))
        self.master.model.set_exercise_time(int(self.exercise.get()))
        self.master.model.set_rest_time(int(self.rest.get()))

        self.master.change(WorkoutFrame)


class WorkoutFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Settings")

        master.geometry("600x660")
        master.title("Tabata Timer")

        self.frame_t = tk.Frame(self, width=600, height=200)
        self.frame_t.grid(row=0, column=0, columnspan=2)

        self.frame_t_label = tk.Frame(self, width=600, height=20)
        self.frame_t_label.grid(row=1, column=0, columnspan=2)

        self.frame_s = tk.Frame(self, width=300, height=200)
        self.frame_s.grid(row=2, column=0, columnspan=1)

        self.frame_c = tk.Frame(self, width=300, height=200)
        self.frame_c.grid(row=2, column=1, columnspan=1)

        self.frame_s_label = tk.Frame(self, width=300, height=20)
        self.frame_s_label.grid(row=3, column=0, columnspan=1)

        self.frame_c_label = tk.Frame(self, width=300, height=20)
        self.frame_c_label.grid(row=3, column=1, columnspan=1)

        self.frame4 = tk.Frame(self, width=600, height=20)
        self.frame4.grid(row=4, column=0, columnspan=2)

        mins, secs = divmod(self.master.model.get_exercise_t(), 60)
        duration = '{:02d}:{:02d}'.format(mins, secs)

        self.timer = tk.StringVar(value=duration)
        self.timer_label = tk.Label(self.frame_t, textvariable=self.timer, borderwidth=10, font=("Arial", 164, "bold"))
        self.timer_label.grid(row=0, column=0, columnspan=2)

        self.exercise_rest = tk.StringVar(value="Exercise")
        tk.Label(self, textvariable=self.exercise_rest, borderwidth=10, font=("Arial", 54, "bold")) \
            .grid(row=1, column=0, columnspan=2)

        self.sets = tk.StringVar(value=self.master.model.get_num_sets())
        tk.Label(self, textvariable=self.sets, borderwidth=1, font=("Arial", 96, "bold")).grid(row=2, column=0,
        columnspan = 1)

        self.cycles = tk.StringVar(value=self.master.model.get_num_cycles())
        tk.Label(self, textvariable=self.cycles, borderwidth=1, font=("Arial", 96, "bold")).grid(row=2, column=1,
        columnspan = 1)

        tk.Label(self, text="Set", borderwidth=1, font=("Arial", 44, "bold")).grid(row=3, column=0, columnspan=1)

        tk.Label(self, text="Cycle", borderwidth=1, font=("Arial", 44, "bold")).grid(row=3, column=1, columnspan=1)
        # Obj is instance of StringVar.

        self.b = tk.Button(self, text="Start Exercise", command=self.run)
        self.b.grid(row=4, column=0, columnspan=2, pady=(20, 0))

        #self.run()

    def run(self):
        self.b.destroy()
        self.master.controller = ProperController(self.master.model, self.master)
        self.master.controller.run()

        num_cycles = self.master.model.get_num_cycles()
        num_sets = self.master.model.get_num_sets()
        exercise_t = self.master.model.get_exercise_t()

        mins, secs = divmod(num_cycles*num_sets*exercise_t, 60)
        duration = '{:02d}:{:02d}'.format(mins, secs)
        self.master.change(SummaryFrame, {"duration": duration})

class SummaryFrame(tk.Tk):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Workout summary")
        duration = kwargs["duration"]
        print(duration)

        self.frame1 = tk.Frame(self, width=600, height=20, background="white")
        self.frame1.grid(row=0, column=0)
        tk.Label(self, text="Workout duration", font=("Arial", 54, "bold")).grid(row=0, column=0, pady=(100, 10))

        self.frame2 = tk.Frame(self, width=600, height=100, background="white")
        self.frame2.grid(row=1, column=0)
        tk.Label(self, text=duration, font=("Arial", 144, "bold")).grid(row=1, column=0, pady=(10, 100))


def main():
    view = View()
    view.mainloop()


if __name__ == "__main__":
    main()
