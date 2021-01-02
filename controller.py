import View
import Tabata

class Controller:
    def __init__(self, num_sets, num_cycles, exercise_t, rest_t):
        self.model = Tabata(num_sets, num_cycles, exercise_t, rest_t)
        self.view = View(exercise_t, num_sets, num_cycles)

    def run(self):

