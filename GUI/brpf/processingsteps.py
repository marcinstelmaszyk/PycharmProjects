from brpf.browse import BrowseFactory
import os
import pickle
import shutil
from matplotlib import projections
from brpf import utilities


class Processing:
    def __init__(self):
        self.name = None

    def configure(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError

    def cleanup(self):
        raise NotImplementedError


class MainProcessing(Processing):
    def __init__(self):
        super().__init__()
        self.browses = list()
        self.plot_types = ['Basic', 'Merged', 'VerticalCurtain']

    @staticmethod
    def register_plot_type(name):
        """Register plot type as a matplotlib projection.

        One has to register a plot type as a projection so
        a plot class can be directly added to a figure.Figure instance 'fig'
        with the following method:
            fig.add_subplot(gridspec, projection=<plot_type>)

        :param name: Plot class' name
        """
        cls = utilities.import_class_by_name(name, f'brpf.vst.{name.lower()}')
        projections.register_projection(cls)

    @staticmethod
    def store_browse(browse):
        os.makedirs('tmp', exist_ok=True)
        with open(f'tmp/Browse[{browse.id}].tmp', 'wb') as f:
            pickle.dump(browse, f)

    def configure(self):
        # Register all types of plots used by processor,
        # so Matplotlib API can add them to BRPFigure as a subplot.
        for name in self.plot_types:
            self.register_plot_type(name)

        # Create Browse instances
        self.browses.extend([b for b in BrowseFactory(1)])

    def run(self):
        for browse in self.browses:
            browse.configure()
            browse.run()
            self.store_browse(browse)

    def cleanup(self):
        pass


class PostProcessing(Processing):
    def __init__(self):
        super().__init__()

    def configure(self):
        pass

    def run(self):
        for browse_tmp_file in os.listdir('tmp'):
            f = pickle.load(open(f"tmp/{browse_tmp_file}", 'rb'))
            f.savefig(f'output/Browse[{f.id}]')

    def cleanup(self):
        shutil.rmtree('tmp')
