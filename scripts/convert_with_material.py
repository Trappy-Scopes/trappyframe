# Converts stl to gib (written with Claude)

import bpy
import sys

argv = sys.argv[sys.argv.index("--") + 1:]
stl_path, glb_path = argv[0], argv[1]

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_mesh.stl(filepath=stl_path)
obj = bpy.context.selected_objects[0]

mat = bpy.data.materials.new(name="MatteBlackPlastic")
mat.use_nodes = True
bsdf = mat.node_tree.nodes["Principled BSDF"]
bsdf.inputs["Base Color"].default_value = (0.02, 0.02, 0.02, 1.0)
bsdf.inputs["Roughness"].default_value = 0.45
bsdf.inputs["Metallic"].default_value = 0.0
bsdf.inputs["Specular IOR Level"].default_value = 0.3

obj.data.materials.clear()
obj.data.materials.append(mat)
bpy.ops.object.shade_smooth()

bpy.ops.export_scene.gltf(
    filepath=glb_path,
    export_format='GLB',
    export_materials='EXPORT',
    export_apply=True
)