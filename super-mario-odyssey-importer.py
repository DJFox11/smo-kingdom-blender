import bpy
import os

bl_info = {
    "name": "Super Mario Odyssey Kingdom Importer",
    "author": "DJ_Fox11",
    "category": "All",
    "location": "View 3D > Tool Shelf > Kingdom Importer",
    "description": "A tool for importing Kingdoms from Super Mario Odyssey",
    "version": (1, 0, 0),
    "blender": (4, 0, 0),
    "warning": "A dumped ROM of Super Mario Odyssey is needed. (1.0.0-1.3.0)",
    "doc_url": "https://github.com/DJFox11/smo-kingdom-blender",
    "tracker_url": "https://github.com/DJFox11/smo-kingdom-blender/issues",
}

# Define the panel class
class RomfsCheckPanel(bpy.types.Panel):
    bl_label = "Super Mario Odyssey Romfs Check"
    bl_idname = "PT_RomfsCheckPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Kingdom Importer'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Please specify the path to the 'romfs' folder:")

        row = layout.row()
        row.prop(context.scene, "romfs_folder_path", text="")

        row = layout.row()
        row.operator("addon.check_romfs")

# Operator to check romfs folder
class CheckRomfsOperator(bpy.types.Operator):
    bl_idname = "addon.check_romfs"
    bl_label = "Check Romfs"

    def execute(self, context):
        romfs_folder_path = context.scene.romfs_folder_path
        if os.path.exists(romfs_folder_path):
            object_data_path = os.path.join(romfs_folder_path, "ObjectData")
            stage_data_path = os.path.join(romfs_folder_path, "StageData")

            if os.path.exists(object_data_path) and os.path.exists(stage_data_path):
                self.report({'INFO'}, "ObjectData and StageData folders found in the specified romfs folder.")
            else:
                self.report({'ERROR'}, "ObjectData or StageData folders not found in the specified romfs folder.")
        else:
            self.report({'ERROR'}, "Specified romfs folder does not exist.")
        return {'FINISHED'}

# Property to store romfs folder path
bpy.types.Scene.romfs_folder_path = bpy.props.StringProperty(
    name="Romfs Folder Path",
    description="Path to the 'romfs' folder containing Super Mario Odyssey dump",
    subtype='DIR_PATH'
)

# Register the classes
def register():
    bpy.utils.register_class(RomfsCheckPanel)
    bpy.utils.register_class(CheckRomfsOperator)

# Unregister the classes
def unregister():
    bpy.utils.unregister_class(RomfsCheckPanel)
    bpy.utils.unregister_class(CheckRomfsOperator)

# For testing the addon in Blender's text editor
if __name__ == "__main__":
    register()
