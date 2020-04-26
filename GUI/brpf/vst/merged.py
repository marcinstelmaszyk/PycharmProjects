import numpy as np
from brpf.vst.plot import Plot
import matplotlib.pyplot as plt
from brpf.vst.verticalcurtain import VerticalCurtain


class Merged(Plot):
    name = "MergedPlot"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def extract(self):
        self._set_data('along_track1', np.arange(0, self.plot_id + 2, 1))
        self._set_data('parameter1', np.arange(0, self.plot_id + 2, 1)**2)
        self._set_data('along_track2', np.array([3, 5]))
        self._set_data('parameter2', np.array([5, 2]))

    def configure(self):
        self.add_vertical_curtain()
        self.grid(True)
        self.ax.xaxis.set_major_locator(plt.MaxNLocator(7))
        self.ax.set_title(f"{self.ax.get_title()} [{self.plot_id}]")

    def add_vertical_curtain(self):
        v = VerticalCurtain(self.figure, (0, 0, 1, 1), ax=self.axes)
        v.plot()
        v.configure()

    def plot(self, *args, **kwargs):
        for line in [1, 2]:
            try:
                super().plot(self(f'along_track{line}'), self(f'parameter{line}'))
            except KeyError:
                pass
        pass


