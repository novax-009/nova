import importlib
import pkgutil
import logging

logger = logging.getLogger(__name__)

def register_all(application):
    """Automatically import all modules in features/ and call their register(application) if present."""
    package = __package__  # 'features'
    for _, module_name, _ in pkgutil.iter_modules(__path__):
        full_module_name = f"{package}.{module_name}"
        module = importlib.import_module(full_module_name)
        if hasattr(module, "register"):
            module.register(application)
            logger.info(f"Registered feature: {module_name}")