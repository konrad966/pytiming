import time
import numpy as np

class TimeStats():
    def __init__(self):
        self._time_samples = {}

    def log_time(self, name, interval):
        if name not in self._time_samples.keys():
            self._time_samples[name] = []
        self._time_samples[name].append(interval)

    def clear(self, name):
        if name in self._time_samples:
            del self._time_samples[name]

    def clear_all(self):
        self._time_samples = {}

    def print_elem(self, name):
        if name in self._time_samples.keys():
            print()
            v = self._time_samples[name]
            v = np.array(v)
            time_mean_msec = np.mean(v) * 1000
            print(f'Mean time for {name} : {time_mean_msec:.2f} msec')
            print()

    def print_all(self):
        print()
        for k, v in self._time_samples.items():
            v = np.array(v)
            time_mean_msec = np.mean(v) * 1000
            print(f'Mean time for {k} : {time_mean_msec:.2f} msec')
        print()

class TimeMeasure():
    TIME_STATS = TimeStats()
    SYNC_FUN = None
    def __init__(self, name='default', time_stats=None, verbose=False):
        self._name = name
        self._time_s = 0
        self._time_e = 0
        self._interval = 0
        self._verbose = verbose
        if time_stats is None:
            self._time_stats = self.TIME_STATS
        else:
            self._time_stats = time_stats
         
    def __enter__(self):
        if self.SYNC_FUN is not None:
            self.SYNC_FUN()
        self._time_s = time.time()
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.SYNC_FUN is not None:
            self.SYNC_FUN()
        self._time_e = time.time()
        self._interval = self._time_e - self._time_s
        if self._verbose:
            print(f'{self._name} took {self._interval:.5f} sec')
        if self._time_stats is not None:
            self._time_stats.log_time(self._name, self._interval)

    @classmethod
    def set_sync_fun(cls, sync_fun):
        cls.SYNC_FUN = sync_fun

    @classmethod
    def register_global_timestats(cls, time_stats):
        cls.TIME_STATS = time_stats

    @classmethod
    def print_all(cls):
        cls.TIME_STATS.print_all()
