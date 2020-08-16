import bpy
from bpy.props import StringProperty
from bpy.types import Scene

bl_info = {
    'name': "Run on done",
    'category': 'Development',
    'author': "Gabriel Montagné Láscaris-Comneno",
    'blender': (2, 80, 0)
}

class SCENE_PT_run_on_done(bpy.types.Panel):
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
        row.prop(context.scene, "done_still_reference_path")
        row.prop(context.scene, "done_still_command")

        row = layout.row()

        row.prop(context.scene, "done_anim_reference_path")
        row.prop(context.scene, "done_anim_command")


def register():

    Scene.done_still_reference_path = StringProperty(
        name = "Done still folder context",
        default = "//",
        description = "Define the 'still done' reference path",
        subtype = 'DIR_PATH')

    Scene.done_still_command = StringProperty(
        name = "Done still shell command",
        default = "make",
        description = "Command to run on 'anim done'"
    )

    Scene.done_anim_reference_path = StringProperty(
        name = "Done anim folder context",
        default = "//",
        description = "Define the 'anim done' reference path",
        subtype = 'DIR_PATH')

    Scene.done_anim_command = StringProperty(
        name = "Done anim shell command",
        default = "make",
        description = "Command to run on 'anim done'"
    )

    bpy.utils.register_class(SCENE_PT_run_on_done)

def unregister():
    bpy.utils.unregister_class(SCENE_PT_run_on_done)

if __name__ == "__main__":
    register()
