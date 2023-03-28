from pymapd import connect
import osmnx as ox
import geopandas as gpd

G = ox.graph_from_place('Los Angeles, California', network_type='drive')

ox.plot_graph(G)