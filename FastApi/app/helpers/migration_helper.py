"""
This module contains helper functions for migrations.
"""

import importlib
from importlib import resources
from types import ModuleType

from peewee import Model


def get_entity_table_names(entities: set[Model]) -> set[str]:
    """
    Returns the table names of the given entities.
    """

    return {cls._meta.table_name for cls in entities}


def get_entity_modules() -> set[ModuleType]:
    """
    Imports all modules from the entities folder and returns them.
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
    Returns the entities from the entities folder that are not in the given set of entities.
    """

    remaining_entities = set()

    for module in get_entity_modules():
        for attr_name in dir(module):
            attr = getattr(module, attr_name)

            if isinstance(attr, type) and issubclass(attr, Model) and attr is not Model:
                if attr not in entities:
                    remaining_entities.add(attr)

    return remaining_entities
