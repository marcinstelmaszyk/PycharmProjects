import importlib


def import_class_by_name(name: str, mod_name: str):
    """Import class from the given module.

    :param name: Name of the class
    :param mod_name: Path to the module containing the class
    """
    module = importlib.import_module(mod_name)
    return module.__getattribute__(name)


def init_class_by_name(name: str, mod_name: str, **kwargs):
    """Import and initialize class from the given module.

    :param name: Name of the class
    :param mod_name: Path to the module containing the class
    :param kwargs: Arguments passed to class' initializer

    :return Class instance
    """
    cls = import_class_by_name(name, mod_name)
    return cls(**kwargs)


def overrides(interface_class):
    """Decorator to indicate that a method is overriding a base one."""
    def overrider(method):
        msg = f"Method '{method.__name__}' is not overriding anything from base class."
        assert (method.__name__ in dir(interface_class)), msg
        return method
    return overrider
