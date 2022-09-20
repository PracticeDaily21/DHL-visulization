#pip install folium
import pandas as pd
import folium
df1 = pd.read_excel('/Users/yiyicao/Desktop/DHL Data.xlsx', sheet_name = 'Suppliers')
df2 = pd.read_excel('/Users/yiyicao/Desktop/DHL Data.xlsx', sheet_name = 'WHs')
df3 = pd.read_excel('/Users/yiyicao/Desktop/DHL Data.xlsx', sheet_name = 'Customers')

S = df1[["Latitude", "Longitude", "Supplier_ID"]] # suppliers
display(S)

W = df2[["Latitude", "Longitude", "WH_ID"]] # warehouse
display(W)

C = df3[["Latitude", "Longitude", "Customer_ID"]] # customers
display(C)

map = folium.Map(location=[S.Latitude.mean(),S.Longitude.mean()],zoom_start=14, control_scale=True)
for index, location_info in S.iterrows():
    folium.Marker([location_info["Latitude"], location_info["Longitude"]], popup=location_info["Supplier_ID"], icon=folium.Icon(color='red', icon='info-sign')).add_to(map)
for index, location_info in W.iterrows():
    folium.Marker([location_info["Latitude"], location_info["Longitude"]], popup=location_info["WH_ID"],icon=folium.Icon(color='green', icon='info-sign')).add_to(map)
for index, location_info in C.iterrows():
    folium.Marker([location_info["Latitude"], location_info["Longitude"]], popup=location_info["Customer_ID"]).add_to(map)
    
display(map)
    
map = folium.Map(location=[S.Latitude.mean(), 
                           S.Longitude.mean()], 
                            zoom_start=14, control_scale=True, location=[37.09024, -95.712891],width=750, height=500)
for index, location_info in S.iterrows():
    folium.Marker([location_info["Latitude"], location_info["Longitude"]], popup=location_info["Supplier_ID"], icon=folium.Icon(color='red', icon='info-sign')).add_to(map)
for index, location_info in W.iterrows():
    folium.Marker([location_info["Latitude"], location_info["Longitude"]], popup=location_info["WH_ID"],icon=folium.Icon(color='green', icon='info-sign')).add_to(map)
    
display(map)

import plotly.express as px
Demand = df3[["Latitude", "Longitude", "Demand (Shipments)"]] # customers
fig = px.density_mapbox(df3, lat='Latitude', lon='Longitude', z='Demand (Shipments)', radius=10,
                        center=dict(lat=0, lon=180), zoom=0,
                        mapbox_style="stamen-terrain")
fig.show()
