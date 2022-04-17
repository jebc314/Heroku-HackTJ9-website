from flask import Flask, render_template,request
import json
import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/puzzle', methods=["GET"])
def puzzle():
    # test create_stl
    piece = create_stl(np.array([
        [[1,1,1],
        [1,1,1],
        [1,1,1]],
        [[0,0,0],
        [0,1,0],
        [0,0,0]],
        [[0,0,0],
        [0,0,0],
        [0,0,0]],
    ]))

    name = "cube"

    # save to the files
    piece.save('static/files/'+name+'.stl')
    save_png(piece, name)

    output = {
        'stl': 'files/'+name+'.stl',
        'png':'files/'+name+'.png'
    }

    return json.dumps(output)

def save_png(piece, name):
    # Create a new plot
    figure = pyplot.figure()
    axes = mplot3d.Axes3D(figure)

    # Load the STL files and add the vectors to the plot
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(piece.vectors))

    # Auto scale to the mesh size
    scale = piece.points.flatten()
    axes.auto_scale_xyz(scale, scale, scale)

    # Show the plot to the screen
    pyplot.savefig('static/files/'+name+'.png')

# input is numpy array
def create_stl(object):
    def create_cube(size=1):
        size = size/2
        # Define the 8 vertices of the cube
        vertices = np.array([\
            [-size, -size, -size],
            [+size, -size, -size],
            [+size, +size, -size],
            [-size, +size, -size],
            [-size, -size, +size],
            [+size, -size, +size],
            [+size, +size, +size],
            [-size, +size, +size]])
        # Define the 12 triangles composing the cube
        faces = np.array([\
            [0,3,1],
            [1,3,2],
            [0,4,7],
            [0,7,3],
            [4,5,6],
            [4,6,7],
            [5,1,2],
            [5,2,6],
            [2,3,6],
            [3,7,6],
            [0,1,5],
            [0,5,4]])

        # Create the mesh
        cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
        for i, f in enumerate(faces):
            for j in range(3):
                cube.vectors[i][j] = vertices[f[j],:]
        
        return cube

    size = 5

    cubes = []

    for layer in range(3):
        for row in range(3):
            for col in range(3):
                if object[layer][row][col] == 1:
                    cube = create_cube(size)
                    cube.translate(size * np.array([col,row,layer]))
                    cubes.append(cube)

    cube_combined = mesh.Mesh(np.concatenate([cube.data.copy() for cube in cubes]))
    # cube_combined.save('static/files/cube.stl')

    return cube_combined