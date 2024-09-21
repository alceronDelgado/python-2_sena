import pandas as pd

valores_izquierda = {
    "X": ["X1","X2","X3","X4","X5","X6"],
    "W:": ["W6","W7","W8","W9","W1","W0"],
    "Y": ["Y1","Y2","Y3","Y4","Y5","Y6"]
}

valores_derecha = {
    "Z":["z2","z3","z4","z5","other6","other7"],
     "A":["a2","a3","a4","a5","other6","other7"],
     "Y":["y2","y3","y4","y5","other6","other7"],
}

dtaUno = pd.DataFrame(valores_izquierda)
dtaDos = pd.DataFrame(valores_derecha)

df_merge = pd.merge(dtaUno, dtaDos)
print(df_merge)