from gl import Renderer

from math import pi, cos, sin

width = 1024
height = 1024

rend = Renderer(width, height)

def lector(poligono):
    vectores = []
    triangulos = []
    for i in range(0, len(poligono), 2):
        x0 = int(poligono[i][1:len(poligono[i]) - 1])
        y0 = int(poligono[i + 1][0:len(poligono[i + 1]) - 1])
        vectores.append([x0, y0])
    for i in range(0, len(vectores)):
        v0 = vectores[i]
        if (i == len(vectores) - 1):
            v1 = vectores[0]
            v2 = vectores[1]
        elif (i + 1 < len(vectores)):
            v1 = vectores[i + 1]
            v2 = vectores[0]
        elif (i + 2 < len(vectores)):
            v1 = vectores[i + 1]
            v2 = vectores[i + 2]
        rend.glTriangle(v0, v1, v2)
        triangulos.append([v0, v1, v2])
    print(vectores)


poligono1Demo = "(165, 380) (185, 360) (180, 330) (207, 345) (233, 330) (230, 360) (250, 380) (220, 385) (205, 410) (193, 383)"
poligono2Demo = "(321, 335) (288, 286) (339, 251) (374, 302)"
poligono3Demo = "(377, 249) (411, 197) (436, 249)"
poligono4Demo = "(413, 177) (448, 159) (502, 88) (553, 53) (535, 36) (676, 37) (660, 52) (750, 145) (761, 179) (672, 192) (659, 214) (615, 214) (632, 230) (580, 230) (597, 215) (552, 214) (517, 144) (466, 180)"
poligono5Demo = "(682, 175) (708, 120) (735, 148) (739, 170)"

poligonosDemo = [poligono1Demo, poligono2Demo, poligono3Demo, poligono4Demo, poligono5Demo]
poligonos = [poligono.split(" ") for poligono in poligonosDemo]

for poligono in poligonos:
    lector(poligono)

#rend.glTriangle([130, 100], [250, 500], [500, 400])

rend.glFinish("output.bmp")
