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

# List of kingdoms
kingdoms = [
    "Cascade Kingdom",
    "Cap Kingdom",
    "Sand Kingdom",
    "Lake ingdom",
    "Wooded Kingdom",
    "Cloud Kingdom",
    "Lost Kingdom",
    "Metro Kingdom",
    "Snow Kingdom",
    "Seaside Kingdom",
    "Luncheon Kingdom",
    "Ruined Kingdom",
    "Bowser's Kingdom",
    "Moon Kingdom",
    "Mushroom Kingdom",
    "Dark Side",
    "Darker Side"
]

# Define the panel class
class RomfsCheckPanel(bpy.types.Panel):
    bl_label = "Romfs Check"
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

        if context.scene.romfs_checked:
            col = layout.column()
            col.label(text="Select Kingdom:")
            col.prop(context.scene, "selected_kingdom")
        else:
            layout.label(text="ObjectData and StageData folders not found.")

# Operator to check romfs folder
class CheckRomfsOperator(bpy.types.Operator):
    bl_idname = "addon.check_romfs"
    bl_label = "Check Romfs"

    def execute(self, context):
        romfs_folder_path = context.scene.romfs_folder_path
        if os.path.exists(romfs_folder_path):
            stage_data_path = os.path.join(romfs_folder_path, "ObjectData", "StageData")

            if os.path.exists(stage_data_path):
                context.scene.romfs_checked = True
                self.report({'INFO'}, "ObjectData and StageData folders found in the specified romfs folder.")
            else:
                context.scene.romfs_checked = False
                self.report({'ERROR'}, "ObjectData and StageData folders not found in the specified romfs folder.")
        else:
            context.scene.romfs_checked = False
            self.report({'ERROR'}, "Specified romfs folder does not exist.")
        return {'FINISHED'}

# Property to store romfs folder path
bpy.types.Scene.romfs_folder_path = bpy.props.StringProperty(
    name="Romfs Folder Path",
    description="Path to the 'romfs' folder containing Super Mario Odyssey dump",
    subtype='DIR_PATH'
)

# Property to store whether romfs is checked
bpy.types.Scene.romfs_checked = bpy.props.BoolProperty(
    name="ROMFS Checked",
    default=False
)

# Property to store selected kingdom
bpy.types.Scene.selected_kingdom = bpy.props.EnumProperty(
    items=[(kingdom, kingdom, "") for kingdom in kingdoms],
    name="Selected Kingdom"
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
