from tabata import Tabata
from view import View
import time
from playsound import playsound

#TODO: Sound

class Controller:
    def __init__(self, num_sets=8, num_cycles=5, exercise_t=30, rest_t=15):
        self.model = Tabata(num_sets, num_cycles, exercise_t, rest_t)
        self.view = View(exercise_t, num_sets, num_cycles)

    def _countdown(self, t):
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            self.view.update(self.view.timer, timer)
            if t < 6:
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
        mins, secs = divmod(num_cycles*num_sets*(rest_t+exercise_t), 60)
        duration = '{:02d}:{:02d}'.format(mins, secs)
        self.view.workout_summary(duration)
        self.view.root.mainloop()

def main():
    tabata = Controller(2, 1, 15, 10)
    tabata.run()


if __name__ == "__main__":
    main()