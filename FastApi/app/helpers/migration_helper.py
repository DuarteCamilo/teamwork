import importlib
from importlib import resources
from types import ModuleType

from peewee import Model


def get_entity_table_names(entities: set[Model]) -> set[str]:
    """
    Returns the class names of the given set of classes.
    Args:
        classes (set[type]): A set of classes.
    Returns:
        set[str]: A set of class names.
    """

    return {cls._meta.table_name for cls in entities}


def get_entity_modules() -> set[ModuleType]:
    """
    Imports all modules in the entities folder and returns them.
    Returns:
        set[str]: A set of module names.
    """

    entities_path = resources.files("app.entities")
    entity_filenames = [
        entry.name
        for entry in entities_path.iterdir()
        if entry.is_file() and entry.name.endswith(".py")
    ]

    entity_modules = set()

    for filename in entity_filenames:
        module_name = f"app.entities.{filename.removesuffix('.py')}"
        module = importlib.import_module(module_name)
        entity_modules.add(module)

    return entity_modules


def get_remaining_entities(entities: set[Model]) -> set[Model]:
    """
    Returns the class names of the remaining Peewee entities from entities folder that are not included in the given set.
    Args:
        included_entities (set[Model]): A set of Peewee entities.
    Returns:
        set[str]: A set of Peewee entity class names.
    """

    remaining_entities = set()

    for module in get_entity_modules():
        for attr_name in dir(module):
            attr = getattr(module, attr_name)

            if isinstance(attr, type) and issubclass(attr, Model) and attr is not Model:
                if attr not in entities:
                    remaining_entities.add(attr)

    return remaining_entities
