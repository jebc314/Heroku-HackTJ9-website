#import numpy as np
#from stl import mesh
#
#def create_cube(size=1):
#    size = size/2
#    # Define the 8 vertices of the cube
#    vertices = np.array([\
#        [-size, -size, -size],
#        [+size, -size, -size],
#        [+size, +size, -size],
#        [-size, +size, -size],
#        [-size, -size, +size],
#        [+size, -size, +size],
#        [+size, +size, +size],
#        [-size, +size, +size]])
#    # Define the 12 triangles composing the cube
#    faces = np.array([\
#        [0,3,1],
#        [1,3,2],
#        [0,4,7],
#        [0,7,3],
#        [4,5,6],
#        [4,6,7],
#        [5,1,2],
#        [5,2,6],
#        [2,3,6],
#        [3,7,6],
#        [0,1,5],
#        [0,5,4]])
#
#    # Create the mesh
#    cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
#    for i, f in enumerate(faces):
#        for j in range(3):
#            cube.vectors[i][j] = vertices[f[j],:]
#    
#    return cube
#
#'''
#cube1 = create_cube()
#
#cube2 = create_cube()
#cube2.translate(np.array([2,2,0]))
#
#cube_combined = mesh.Mesh(np.concatenate([
#    cube1.data.copy(),
#    cube2.data.copy(),
#]))
#'''
#
#object = np.array([
#    [[1,1,1],
#    [1,1,1],
#    [1,1,1]],
#    [[0,0,0],
#    [0,1,0],
#    [0,0,0]],
#    [[0,0,0],
#    [0,0,0],
#    [0,0,0]],
#])
#
#size = 2
#
#cubes = []
#
#for layer in range(3):
#    for row in range(3):
#        for col in range(3):
#            if object[layer][row][col] == 1:
#                cube = create_cube(size)
#                cube.translate(size * np.array([col,row,layer]))
#                cubes.append(cube)
#
#cube_combined = mesh.Mesh(np.concatenate([cube.data.copy() for cube in cubes]))
#
#cube_combined.save('cube_combined.stl')

from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

# Create a new plot
figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

# Load the STL files and add the vectors to the plot
your_mesh = mesh.Mesh.from_file('static/files/cube.stl')
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

# Auto scale to the mesh size
scale = your_mesh.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)

# Show the plot to the screen
pyplot.savefig('static/files/cube.png')