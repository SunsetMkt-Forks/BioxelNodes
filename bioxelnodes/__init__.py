from .nodes import custom_nodes
from . import auto_load
from . import menu

import bpy


bl_info = {
    "name": "Biovel Nodes",
    "author": "Ma Nan",
    "description": "",
    "blender": (4, 1, 0),
    "version": (0, 1, 0),
    "location": "File -> Import",
    "warning": "",
    "category": "Node"
}

auto_load.init()


def register():
    auto_load.register()
    custom_nodes.register()
    menu.create_menu()


def unregister():
    try:
        menu.remove_menu()
        custom_nodes.unregister()
        auto_load.unregister()
    except RuntimeError:
        pass
