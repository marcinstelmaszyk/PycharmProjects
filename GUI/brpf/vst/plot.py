from matplotlib import axes


class Plot(axes.Axes):

    def __init__(self, *args, **kwargs):
        self.plot_id = kwargs.pop('plot_id', 0)
        self.ax = AxesProxy(kwargs.pop('ax', None) or self)
        super().__init__(*args, **kwargs)
        self._plot_configuration = dict()
        self._data = dict()

    def __getitem__(self, item):
        return self._plot_configuration[item]

    def __call__(self, *args, **kwargs):
        """Retrieve plot's data"""
        parameter = args[0]
        return self._data[parameter]

    def _set_data(self, key, value):
        self._data[key] = value


class AxesProxy:
    def __init__(self, proxied_object):
        self._proxied = proxied_object

    def __setstate__(self, state):
        pass

    def __eq__(self, other):
        return self._proxied == other

    def __getattr__(self, item):
        attribute = getattr(self._proxied, item)
        if callable(attribute):
            def wrapped_method(*args, **kwargs):
                return attribute(*args, **kwargs)
            return wrapped_method
        else:
            return attribute
