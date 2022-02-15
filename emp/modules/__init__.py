from os.path import dirname, basename, isfile
import glob

def __list_all_modules():
    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_modules = [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]
    return all_modules

ALL_MODULES = sorted(__list_all_modules())
print(f"Modules to load: {str(ALL_MODULES)}")
__all__ = ALL_MODULES + ["ALL_MODULES"]
