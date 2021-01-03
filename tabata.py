import time

class Tabata:
    def __init__(self, num_sets=8, num_cycles=5, exercise_t=30, rest_t=15):
        self._num_sets = num_sets
        self._num_cycles = num_cycles
        self._exercise_t = exercise_t
        self._rest_t = rest_t

    def set_num_sets(self, num_sets):
        if isinstance(num_sets, int):
            self._num_sets = num_sets
            return num_sets
        else:
            print("Not an integer")
            return False

    def set_num_cycles(self, num_cycles):
        if isinstance(num_cycles, int):
            self._num_cycles = num_cycles
            return num_cycles
        else:
            print("Not an integer")
            return False


    def set_rest_time(self, rest_t):
        if isinstance(rest_t, int):
            self._rest_t = rest_t
            return rest_t
        else:
            print("Not an integer")
            return False

    def set_exercise_time(self, exercise_t):
        if isinstance(exercise_t, int):
            self._exercise_t = exercise_t
            return exercise_t
        else:
            print("Not an integer")
            return False

    def get_num_sets(self):
        return self._num_sets

    def get_num_cycles(self):
        return self._num_cycles

    def get_exercise_t(self):
        return self._exercise_t

    def get_rest_t(self):
        return self._rest_t

    ###########################################################################
    ###################### Not part of the MVC framework ######################
    ###########################################################################

    def _countdown(self, t):
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1

    def start_exercise(self):
        for curr_c in range(0, self._num_cycles):
            for curr_s in range(0, self._num_sets):
                print("Start")
                self._countdown(self._exercise_t)
                print("Rest")
                self._countdown(self._rest_t)

        print("Exercise finished!")


def main():
    tabata = Tabata(1, 1)
    tabata.start_exercise()


if __name__ == "__main__":
    main()
