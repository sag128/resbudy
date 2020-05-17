import plotly.express as px
import pandas as pd

# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
def fig(fname):
    
    data = pd.read_csv(fname)
    # Preview the first 5 lines of the loaded data
    #print(data)
    
    px.set_mapbox_access_token(open("mapbox.mapbox_token").read())
    # carshare = px.data.carshare()
    fig = px.scatter_mapbox(data,hover_name='name' , lat='lat', lon='lon',
                            color_continuous_scale=px.colors.cyclical.IceFire,size='reviews', size_max=100,
                            zoom=11,height=1000,width=1920,color="ratings")
    fig.show()

def fig2(fname):
    
    data = pd.read_csv(fname)
    # Preview the first 5 lines of the loaded data
    #print(data)
    
    
    px.set_mapbox_access_token(open("mapbox.mapbox_token").read())
    # carshare = px.data.carshare()
    fig2 = px.scatter_mapbox(data,hover_name='Unnamed: 0', lat='lat', lon='lon',
                            color_continuous_scale=px.colors.cyclical.mrybm,size='size' ,color='rating',
                            zoom=11,height=1000,width=1920,size_max=100,text="reviews")
    fig2.show()
    










