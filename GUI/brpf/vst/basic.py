import numpy as np
from brpf.vst.merged import Merged


class Basic(Merged):
    name = "BasicPlot"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def extract(self):
        self._set_data('along_track1', np.arange(0, self.plot_id + 2, 1))
        self._set_data('parameter1', np.arange(0, self.plot_id + 2, 1))

    def configure(self):
        self.grid(True)
        self.set_xlim(0, self.plot_id + 1)
        self.set_ylim(0, self.plot_id + 1)
        self.set_title(f"BasicPlot [{self.plot_id}]")

    def plot(self, *args, **kwargs):
        super().plot(self('along_track1'), self('parameter1'))
        pass



