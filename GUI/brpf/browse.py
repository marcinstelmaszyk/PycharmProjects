from enum import Enum
from matplotlib import pyplot as plt
from brpf.brpfigure import BRPFigure


class BrowseType(Enum):
    SIMPLE = 1
    COMPLEX = 2


class BrowseFactory:
    def __init__(self, n: int):
        self.max: int = n

    def __iter__(self):
        self.current_id: int = 0
        return self

    def __next__(self):
        if self.current_id >= self.max:
            raise StopIteration
        self.current_id += 1
        return Browse(id=self.current_id, type=BrowseType.SIMPLE)


class Browse:
    def __init__(self, *args, **kwargs):
        self.figures = list()
        self.type: BrowseType = kwargs.get('type', BrowseType.SIMPLE)
        self.id: int = kwargs.get('id', -1)

    def __str__(self):
        return f"[{self.id}] {self.type}"

    @property
    def dim(self):
        return 2 if self.type == BrowseType.SIMPLE else 3

    def _add_figure(self, **kwargs):
        fig = plt.figure(FigureClass=BRPFigure, **kwargs)
        self.figures.append(fig)

    def configure(self):
        self._add_figure(id=1, dim=self.dim)

        for fig in self.figures:
            fig.configure()

    def run(self):
        for fig in self.figures:
            fig.run()

    def savefig(self, path):
        for fig in self.figures:
            fig.savefig(path)
