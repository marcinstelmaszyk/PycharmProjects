from brpf import utilities as utils


class BRPF:
    """
    Example:
        proc = BRPF()
        proc.configure()
        proc.run()
        proc.cleanup()
    """
    def __init__(self):
        self._processing_steps = list()

    def __str__(self):
        return "Steps: " + ",".join([step.__name__ for step in self._processing_steps])

    def __repr__(self):
        return str(self)

    def _add_ps(self, name: str) -> None:
        """Initialize and add processing step to self._processing_steps

        :param name: Processing step class' name
        """
        processing_step = utils.init_class_by_name(name, mod_name="brpf.processingsteps")
        self._processing_steps.append(processing_step)

    def configure(self):
        """Add processing steps to the processor.
        """
        self._add_ps("MainProcessing")
        self._add_ps("PostProcessing")

    def run(self):
        """Configure and run processing steps.
        """
        for step in self._processing_steps:
            step.configure()
            step.run()

    def cleanup(self):
        for step in self._processing_steps:
            step.cleanup()
