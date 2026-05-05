import numpy as np
import pylab as plt
import pandas as pd

def hello():
  print("hello")

def loadcsv(ifile):
  return pd.read_csv(ifile,header=None,sep=";").replace(",",".",regex=True).to_numpy().astype("float")

def pintar_imagen(filename,vmin=None,vmax=None,colormap="coolwarm",colorbar=False,savepath=""):
  plt.imshow(loadcsv(filename),cmap=colormap,vmin=vmin,vmax=vmax)
  if colorbar:
    plt.colorbar()
  if savepath != "":
    plt.savefig(savepath)


def choose_region(filename,origin,shape,vmin=None,vmax=None,colormap="coolwarm",savepath=""):
  datos=loadcsv(filename)
  pintar_imagen(filename,vmin,vmax,colormap)
  region=np.zeros_like(datos)
  end=np.array(origin)+np.array(shape)
  region[origin[0]:end[0],origin[1]:end[1]]=1
  region=region.astype(bool)
  plt.imshow(region,alpha=.2,cmap="binary")
  if savepath != "":
    plt.savefig(savepath)
  return region
    
