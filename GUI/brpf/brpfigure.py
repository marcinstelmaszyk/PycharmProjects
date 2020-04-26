from matplotlib import figure, pyplot
from brpf.utilities import overrides


class BRPFigure(figure.Figure):
    def __init__(self, *args, **kwargs):
        self.id = kwargs.pop('id')
        self.dim = kwargs.pop('dim')
        self.gridshape = (2, 3)
        super().__init__(*args, **kwargs)

    @overrides(figure.Figure)
    def __str__(self):
        return f"{super().__str__()}, id={self.id}"

    @overrides(figure.Figure)
    def add_subplot(self, *args, **kwargs):
        """Add a subclass of `~.vst.Plot` to the BRPFigure.

        The call of base class' method add_subplot() is extended by passing
        information about plot's position in the <List_of_Plots>.

        :param args:
        :param kwargs:
        :return:
        """
        gridspec = args[0]
        try:
            ax = super().add_subplot(gridspec, projection=kwargs['type'],
                                plot_id=kwargs['id'])
        except KeyError as e:
            raise AssertionError(f"Missing kwarg {e} in add_subplot() call.")

        return ax

    def _get_plots(self):
        return self.axes

    def add_brpfplot(self, type, row, col, **kwargs):
        colspan = kwargs.pop('colspan', 1)
        rowspan = kwargs.pop('rowspan', 1)
        pyplot.subplot2grid(self.gridshape, loc=(row, col),
                            rowspan=rowspan, colspan=colspan, fig=self,
                            type=type, **kwargs)

    def _add_plots(self):
        self.add_brpfplot('BasicPlot', 0, 0, id=0)
        self.add_brpfplot('BasicPlot', 1, 0, id=1)
        self.add_brpfplot('MergedPlot', 0, 1, id=2, rowspan=2, colspan=2)

    def configure(self):
        self._add_plots()
        self.subplots_adjust(wspace=0.3, hspace=0.4, bottom=0.2, top=0.85)
        self.suptitle("Browse")

    def run(self):
        for ax in self._get_plots():
            ax.extract()
            ax.configure()
            ax.plot()
