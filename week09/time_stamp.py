
import time

class TimeStamp:
    def __init__(self):
        self._time_stamps = []
      
    
    def __call__(self, *args):
        time_stamp = time.perf_counter_ns()
        if len(args) > 1:
            raise ValueError('Too many bloody arguments!')
        if args:
            self._time_stamps.append((time_stamp, args[0]))
        else:
            prior_time_stamp = self._time_stamps[0][0] if self._time_stamps else 0
            deltas_time_stamps = []
            for ts, label in self._time_stamps:
                deltas_time_stamps.append((ts - prior_time_stamp, label))
                prior_time_stamp = ts
            return deltas_time_stamps

t = TimeStamp()
print(t("starting"))
print(t("snooze"))
print(t())


