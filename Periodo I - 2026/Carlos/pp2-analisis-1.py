#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 18:53:21 2026

@author: Davalillo D. Carlos M.
"""

import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from matplotlib.colors import BoundaryNorm
import plotly.io as pio

#Forzar la apertura en el navegador (a prueba de fallos)
pio.renderers.default = "browser"

#===============================================================================================
#===============================================================================================
#DATOS DEL MODELO
#-----------------------------------------------------------------------------------------------
CSV_FILE='datos-campo-carlos.csv' #Modificar según el caso
COL_G='g (s)'
COL_T1='t1 (s)'
COL_TSAT='tsat (s)'
#===============================================================================================
#===============================================================================================


#===============================================================================================
#Carga de datos
#-----------------------------------------------------------------------------------------------
print(f"Carga de datos desde {CSV_FILE}...")
df=pd.read_csv(CSV_FILE)
g=df[COL_G]
t1=df[COL_T1]
tsat=df[COL_TSAT]
#===============================================================================================


#===============================================================================================
#Cálculo de PHI con la ecuación de la cola de descarga
#-----------------------------------------------------------------------------------------------
phi=1+np.floor((g-t1)/tsat)
phi=np.maximum(phi,0)
#===============================================================================================


#===============================================================================================
#Actualización de los datos
#-----------------------------------------------------------------------------------------------
df['phi']=phi
#===============================================================================================


#===============================================================================================
#Generación de grillado en el plano XY para graficar el modelo (pero no los datos)
#-----------------------------------------------------------------------------------------------
n_max=16
t1_min=0
tsat_min=1
t1_max=math.ceil(max(t1))
tsat_max=math.ceil(max(tsat))
t1_range=np.linspace(t1_min,t1_max,n_max)
tsat_range=np.linspace(tsat_min,tsat_max,n_max)
t1_delta=t1_range[1]-t1_range[0]
tsat_delta=tsat_range[1]-tsat_range[0]
t1_mesh,tsat_mesh=np.meshgrid(t1_range,tsat_range)

#Cálculo de Phi con la función piso (floor)
g_const=65
phi_mesh=1+np.floor((g_const-t1_mesh)/tsat_mesh)
phi_mesh=np.maximum(phi_mesh,0)

#Para el plano de máximo flujo Phi
z_max=phi_mesh.max()
x_plane=np.array([[t1_min,t1_max],[t1_min,t1_max]])
y_plane=np.array([[tsat_min,tsat_max],[tsat_min,tsat_max]])
z_plane=np.array([[0,0],[z_max,z_max]])

#Versión sin la función piso (floor)
m_max=300
t1_range_smooth=np.linspace(t1_min,t1_max,m_max)
tsat_range_smooth=np.linspace(tsat_min,tsat_max,m_max)
t1_mesh_smooth,tsat_mesh_smooth=np.meshgrid(t1_range_smooth,tsat_range_smooth)
phi_mesh_smooth=1+(np.abs(g_const-t1_mesh_smooth)/tsat_mesh_smooth)
phi_mesh_smooth=np.maximum(phi_mesh_smooth,0)
#===============================================================================================


#===============================================================================================
#Visualización de los datos recopilados del modelo
#-----------------------------------------------------------------------------------------------
levels=np.arange(-0.5,int(phi_mesh.max())+1.5,1) 
cmap=plt.cm.jet
norm=BoundaryNorm(levels,ncolors=cmap.N,clip=True)

figure_1=plt.figure(dpi=300)
axis_1=figure_1.add_subplot(111, projection='3d')

x_pos=t1_mesh.flatten()
y_pos=tsat_mesh.flatten()
z_pos=np.zeros_like(x_pos)       
dz=phi_mesh.flatten()           

bar_colors=cmap(norm(dz))

#Grafica los datos como barras 3D
axis_1.bar3d(x_pos,y_pos,z_pos,t1_delta,tsat_delta,dz,color=bar_colors,shade=True)

axis_1.set_title('Modelo discreto de descarga de cola',fontweight='bold')
axis_1.set_xlabel('T1 [s]')
axis_1.set_ylabel('Tsat [s]')
axis_1.set_zlabel('Phi (vehículos)')
elevation_angle=30
azimuthal_angle=50
axis_1.view_init(elev=elevation_angle,azim=azimuthal_angle)
axis_1.invert_xaxis() 
axis_1.set_proj_type('persp',focal_length=0.25)
axis_1.dist=18 
axis_1.set_box_aspect([0.8,0.8,0.9]) 
#===============================================================================================

#===============================================================================================
#Visualización del modelo sin la función piso (floor)
#-----------------------------------------------------------------------------------------------
figure_2=go.Figure()

figure_2.add_trace(go.Surface(
    x=t1_range_smooth, 
    y=tsat_range_smooth, 
    z=phi_mesh_smooth, 
    colorscale='Hot', 
    showscale=True,
    name='Phi Continuo'
))

figure_2.add_trace(go.Surface(
    x=x_plane, 
    y=y_plane, 
    z=z_plane, 
    opacity=0.5, 
    colorscale=[[0,'blue'],[1,'blue']], 
    showscale=False,
    name='Plano Máximo Flujo'
))

figure_2.update_layout(
    title='Modelo discreto de descarga de cola',
    scene=dict(
        xaxis=dict(title='T1 [s]',autorange="reversed"), # <--- EJE INVERTIDO
        yaxis=dict(title='Tsat [s]'),
        zaxis=dict(title='Phi (vehículos)'),
        camera=dict(eye=dict(x=1.5, y=1.5, z=1.2)) # Ángulo similar a elev=30, azim=30
    )
)

figure_2.show()
#===============================================================================================



#===============================================================================================
#Mensajes para el usuario
#-----------------------------------------------------------------------------------------------
print("\n--- Inferencia de comportamiento de Tráfico ---")
print(f"Total ciclos analzados: {len(df)}")
print(f"Vehículos descargados promedio por ciclo: {df['phi'].mean():.2f}")
print(f"Máximo capacidad de descarga observada: {int(df['phi'].max())} vehículos")
print(f"Mínimo tiempo de verde efectivo: {df[COL_G].min():.2f} segundos")
#===============================================================================================






