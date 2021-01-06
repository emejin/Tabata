import time
from playsound import playsound
import tkinter as tk


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def _countdown(self, t):
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            self.view.update(self.view.timer, timer)
            if t < 4:
                self.view.change_color("red")
                playsound("sounds/beep-07.mp3")
                time.sleep(0.5)
            else:
                time.sleep(1)
            t -= 1

    def run(self):
        num_cycles = self.model.get_num_cycles()
        num_sets = self.model.get_num_sets()
        exercise_t = self.model.get_exercise_t()
        rest_t = self.model.get_rest_t()

        self._countdown(3)

        for curr_c in range(1, num_cycles+1):
            self.view.update(self.view.cycles, curr_c)

            for curr_s in range(1, num_sets+1):
                self.view.update(self.view.sets, curr_s)

                print("Start")
                self.view.change_color("black")
                playsound("sounds/Exercise.mp3")
                self.view.update(self.view.exercise_rest, "Exercise")
                self._countdown(exercise_t)  # Length of exercise MP3 is 1 sec
                playsound("sounds/Rest.mp3")
                print("Rest")
                self.view.update(self.view.exercise_rest, "Rest")
                self.view.change_color("black")
                self._countdown(rest_t)  # Length of rest MP3 is 1 sec

        print("Exercise finished!")
        playsound("sounds/completed.mp3")

        #self.view.root.mainloop()

    def start(self):
        num_cycles = self.model.set_num_cycles(int(self.view.cycles.get()))
        num_sets = self.model.set_num_sets(int(self.view.sets.get()))
        exercise_t = self.model.set_exercise_time(int(self.view.exercise.get()))
        rest_t = self.model.set_rest_time(int(self.view.rest.get()))

        newWindow = tk.Toplevel()
        self.view = WorkoutView(newWindow, exercise_t, num_sets, num_cycles)
        self.run()


class ProperController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def _countdown(self, t):
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            self.view.update_text(self.view.frame.timer, timer)
            if t < 4:
                self.view.change_color(self.view.frame.timer_label, "red")
                playsound("sounds/beep-07.mp3")
                time.sleep(0.5)
            else:
                time.sleep(1)
            t -= 1

    def run(self):
        num_cycles = self.model.get_num_cycles()
        num_sets = self.model.get_num_sets()
        exercise_t = self.model.get_exercise_t()
        rest_t = self.model.get_rest_t()

        self._countdown(3)

        for curr_c in range(1, num_cycles+1):
            self.view.update_text(self.view.frame.cycles, curr_c)

            for curr_s in range(1, num_sets+1):
                self.view.update_text(self.view.frame.sets, curr_s)

                print("Start")
                self.view.change_color(self.view.frame.timer_label, "black")
                playsound("sounds/Exercise.mp3")
                self.view.update_text(self.view.frame.exercise_rest, "Exercise")
                self._countdown(exercise_t)  # Length of exercise MP3 is 1 sec
                playsound("sounds/Rest.mp3")
                print("Rest")
                self.view.update_text(self.view.frame.exercise_rest, "Rest")
                self.view.change_color(self.view.frame.timer_label, "black")
                self._countdown(rest_t)  # Length of rest MP3 is 1 sec

        print("Exercise finished!")
        playsound("sounds/completed.mp3")


def main():
    tabata = Controller()


if __name__ == "__main__":
    main()