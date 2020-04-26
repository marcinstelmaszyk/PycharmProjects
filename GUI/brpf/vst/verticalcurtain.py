import numpy as np
from brpf.vst.plot import Plot
import matplotlib.pyplot as plt
from matplotlib import colors


class MappingNorm(colors.BoundaryNorm):
    def __init__(self, levels, ncolors):
        self.mapping = {lev: i for i, lev in enumerate(levels)}
        self.Nlevels = len(levels)
        super().__init__(np.arange(self.Nlevels + 1), ncolors)

    def __call__(self, *args, **kwargs):
        if len(args[0]) == self.Nlevels:
            return np.arange(0, self.Nlevels)
        return [self.mapping.get(value, self.Ncmap) for value in args[0]]


class MappingColormap(colors.ListedColormap):
    def __init__(self, c):
        transparent_value = colors.to_rgba('none')
        super().__init__(c + [transparent_value])


class VerticalCurtain(Plot):
    name = "VerticalCurtainPlot"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def extract(self):
        self._set_data('along_track1', np.arange(0, self.plot_id + 2, 1))
        self._set_data('parameter1', np.arange(0, self.plot_id + 2, 1))

    def configure(self):
        self.ax.grid(True)
        self.ax.xaxis.set_major_locator(plt.MaxNLocator(7))
        self.ax.set_title(f"{self.name}")

    def plot(self, *args, **kwargs):
        # make these smaller to increase the resolution
        dx, dy = 0.05, 0.05

        # generate 2 2d grids for the x & y bounds
        y, x = np.mgrid[slice(0, 5 + dy, dy),
                        slice(0, 5 + dx, dx)]
        z = x + y
        z = z[:-1, :-1]

        mapping = {
            2: 'green',
            4: 'red',
            8: 'blue',
        }

        # Discrete color map
        cmap = MappingColormap(list(mapping.values()))
        norm = MappingNorm(sorted(mapping.keys()), cmap.N)
        im = self.ax.pcolormesh(x, y, z, cmap=cmap, norm=norm)

        # Colorbar
        cb = self.ax.figure.colorbar(ax=self.ax, mappable=im, drawedges=True)
        cb.set_ticks(np.arange(0.5, cb.norm.Ncmap))
        cb.ax.set_yticklabels(cb.norm.mapping.keys())
        cb.ax.tick_params(length=0)

        # Edgecolor
        cb.outline.set_edgecolor('white')

        # Dividers
        cb.dividers.set_color('white')
        cb.dividers.set_linewidth(5)
