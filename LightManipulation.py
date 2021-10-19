bl_info = {
    "name": "Biblioteka manipulowania światłem",
    "author": "Tomasz Ostrowski",
    "version": (1, 0),
    "blender": (2, 92, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Umożliwia modyfikowanie wielu obiektów typu LIGHT",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}

import bpy

class AddObjectPanel(bpy.types.Panel):
    bl_label = "Dodaj światlo"
    bl_idname = "PT_AddObjectPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Oswietlenie'
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text = "Light", icon = 'OUTLINER_OB_LIGHT')
        row.operator("object.light_add")
        row.scale_y = 1.5

class LocationPanel(bpy.types.Panel):
    bl_label = "Lokalizacja"
    bl_idname = "PT_LocationPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Oswietlenie'
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        if obj.type == "LIGHT":
            row = layout.row()
            row.operator("transform.translate", text="Przenieś")
            col = layout.column()
            col.prop(obj, "location", text="Lokalizacja")

class RotationPanel(bpy.types.Panel):
    bl_label = "Rotacja"
    bl_idname = "PT_RotationPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Oswietlenie'
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        if obj.type == "LIGHT":
            row = layout.row()
            row.operator("transform.rotate", text="Obróć")
            col = layout.column()
            col.prop(obj, "rotation_euler", text="Obrót")

class ScalePanel(bpy.types.Panel):
    bl_label = "Rozmiar"
    bl_idname = "PT_ScalePanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Oswietlenie'
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        if obj.type == "LIGHT":
            row = layout.row()
            row.operator("transform.resize", text="Zmień rozmiar")
            col = layout.column()
            col.prop(obj, "scale", text="Skala")

class LightPanel(bpy.types.Panel):
    bl_label = "Światło"
    bl_idname = "PT_LightPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Oswietlenie'
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
    
        if obj.type == "LIGHT":
            row = layout.row()
            row.prop(obj, "name", text="Nazwa")
            row.prop(obj.data, "type", text="Typ")
            row = layout.row()
            row.prop(obj.data, "energy", text="Energia")
            row = layout.row()
            row.prop(obj.data, "color", text="Kolor")
            
            if obj.data.type == "SPOT" or obj.data.type == "POINT":
                row = layout.row()
                row.prop(obj.data, "shadow_soft_size", text="Rozmiar")
            if obj.data.type == "AREA":
                row = layout.row()
                row.prop(obj.data, "size", text="Rozmiar")
            if obj.data.type == "SUN":
                row = layout.row()
                row.prop(obj.data, "angle", text="Kąt")
            if obj.data.type == "SPOT":
                row = layout.row()
                row.prop(obj.data, "spot_blend", text="Rozmycie")

class PreviewPanel(bpy.types.Panel):
    bl_label = "Podgląd"
    bl_idname = "PT_PreviewPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Oswietlenie'
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        if obj.type == "LIGHT":
            row = layout.row()
            row.template_preview(obj.data)
        
class AllLightsPanel(bpy.types.Panel):
    bl_label = "Wszystkie światła"
    bl_idname = "PT_AllLightsPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Oswietlenie'
    
    def draw(self, context):
        layout = self.layout
        objects = context.selected_objects
        
        row = layout.row()
        row.operator("scene.all_lights", text="Zaznacz wszystkie")
        row.scale_y = 1.5
        if objects[0].type == "LIGHT":
            for obj in objects:
                row = layout.row()
                row.prop(obj, "name", text="Nazwa")
                row.prop(obj.data, "type", text="Typ")
                row.scale_y = 1.5
                row = layout.row()
                row.prop(obj.data, "energy", text="Energia")
                row = layout.row()
                row.prop(obj.data, "color", text="Kolor")
                
                if obj.data.type == "SPOT" or obj.data.type == "POINT":
                    row = layout.row()
                    row.prop(obj.data, "shadow_soft_size", text="Rozmiar")
                if obj.data.type == "AREA":
                    row = layout.row()
                    row.prop(obj.data, "size", text="Rozmiar")
                if obj.data.type == "SUN":
                    row = layout.row()
                    row.prop(obj.data, "angle", text="Kąt")
                if obj.data.type == "SPOT":
                    row = layout.row()
                    row.prop(obj.data, "spot_blend", text="Rozmycie")

class MyOperator(bpy.types.Operator):
    bl_idname = "scene.all_lights"
    bl_label = "Zaznacz wszystkie światła"
    
    def execute(self, context):
        objects = bpy.context.scene.objects

        for obj in objects:
            obj.select_set(obj.type == "LIGHT")
        return {"FINISHED"}
        
def register():
    bpy.utils.register_class(AddObjectPanel)
    bpy.utils.register_class(LocationPanel)
    bpy.utils.register_class(ScalePanel)
    bpy.utils.register_class(RotationPanel)
    bpy.utils.register_class(LightPanel)
    bpy.utils.register_class(PreviewPanel)
    bpy.utils.register_class(AllLightsPanel)
    bpy.utils.register_class(MyOperator)
    
def unregister():
    bpy.utils.unregister_class(LocationPanel)
    bpy.utils.unregister_class(ScalePanel)
    bpy.utils.unregister_class(RotationPanel)
    bpy.utils.unregister_class(LightPanel)
    bpy.utils.unregister_class(AddObjectPanel)
    bpy.utils.unregister_class(PreviewPanel)
    bpy.utils.unregister_class(AllLightsPanel)
    bpy.utils.unregister_class(MyOperator)

if __name__ == "__main__":
    register()