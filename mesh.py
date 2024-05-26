def generate_mesh(points, colors):
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)

    o3d_colors = o3d.utility.Vector3dVector(PART_COLORS[colors - 1]/255)
    pcd.colors = o3d_colors

    alpha = 0.03
    mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(pcd, alpha)
    mesh.compute_vertex_normals()


    o3d.visualization.draw_geometries([mesh], mesh_show_back_face=True)
    print(mesh)
    return mesh