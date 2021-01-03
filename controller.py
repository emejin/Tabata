from tabata import Tabata
from view import View
import time

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
                self.view.update(self.exercise_rest_label, "Exercise")
                self._countdown(exercise_t)
                print("Rest")
                self.view.update(self.exercise_rest_label, "Rest")
                self._countdown(rest_t)

        print("Exercise finished!")


def main():
    tabata = Controller(1, 1)
    tabata.run()


if __name__ == "__main__":
    main()