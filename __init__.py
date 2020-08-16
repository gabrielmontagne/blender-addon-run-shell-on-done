import bpy
from bpy.app.handlers import persistent
from bpy.props import StringProperty
from bpy.types import Scene, Panel
from shlex import split
from bpy.path import abspath
import subprocess

bl_info = {
    'name': "Run on done",
    'category': 'Development',
    'author': "Gabriel Montagné Láscaris-Comneno",
    'blender': (2, 80, 0)
}

@persistent
def handle_finished(scene):
    command = scene.done_command
    cwd = scene.done_reference_path

    if not command:
        return

    args = split(command)
    try:
        result = subprocess.run(args, cwd=abspath(cwd))
    except Exception as e:
        print("Couldn't run command", command, "on", cwd)

class SCENE_PT_run_on_done(Panel):
    """Scene panel for config run on done."""
    bl_label = "Run on done"
    bl_idname = "SCENE_PT_run_on_done"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout
        space = context.space_data

        row = layout.row()
        row.prop(context.scene, "done_reference_path")
        row = layout.row()
        row.prop(context.scene, "done_command")

        row = layout.row()

def register():

    Scene.done_reference_path = StringProperty(
        name = "Done  folder context",
        default = "//",
        description = "Define the ' done' reference path",
        subtype = 'DIR_PATH')

    Scene.done_command = StringProperty(
        name = "Done  shell command",
        default = "make",
        description = "Command to run on ' done'"
    )

    bpy.utils.register_class(SCENE_PT_run_on_done)
    bpy.app.handlers.render_complete.append(handle_finished)

def unregister():
    bpy.utils.unregister_class(SCENE_PT_run_on_done)
    bpy.app.handlers.render_complete.remove(handle_finished)


if __name__ == '__main__':
    register()
