import numpy as np
import pylab as plt
import pandas as pd

def hello():
  print("hello")

def loadcsv(ifile):
  return pd.read_csv(ifile,header=None,sep=";").replace(",",".",regex=True).to_numpy().astype("float")

def pintar_imagen(filename,vmin=None,vmax=None,colormap="coolwarm",colorbar=False,savepath="",emisivity=1):
  plt.imshow(loadcsv(filename)*emisivity,cmap=colormap,vmin=vmin,vmax=vmax)
  if colorbar:
    plt.colorbar()
  if savepath != "":
    plt.savefig(savepath,dpi=200)


def choose_region(filename,origin,shape,vmin=None,vmax=None,colormap="coolwarm",savepath="",emisivity=1):
  datos=loadcsv(filename)
  pintar_imagen(filename,vmin,vmax,colormap,False,emisivity)
  region=np.zeros_like(datos)
  end=np.array(origin)+np.array(shape)
  region[origin[0]:end[0],origin[1]:end[1]]=1
  region=region.astype(bool)
  plt.imshow(region,alpha=.2,cmap="binary")
  if savepath != "":
    plt.savefig(savepath,dpi=200)
  return region

def plot_T_evolution(prefix,T_list,title,tagpos=[80,22],color="black",savepath="",emisivity=1):
  Tavg=[]
  Tmax=[]
  for T in T_list:
    data=loadcsv(prefix+str(T)+".csv")*emisivity
    Tavg.append(np.average(data[region_carbono]))
    Tmax.append(np.max(data[region_carbono]))
  plt.plot(T_list,Tavg,"o",linewidth=3,markersize=8,color="tab:orange",label="T_avg")
  plt.plot(T_list,Tmax,"^",linewidth=3,markersize=8,color="tab:blue",label="T_max")

  T_list=np.array(T_list)
  if withfit:
    emisivity_fit=np.polyfit(T_list,Tavg,1)
    plt.plot(T_list,T_list*emisivity_fit[0]+emisivity_fit[1],"--",linewidth=3,color=color)
    plt.text(tagpos[0],tagpos[1],r"$\epsilon = $"+str(np.round(emisivity_fit[0],2)),fontsize=16,color=color)


  plt.legend()
  plt.grid(alpha=.7)
  plt.title(title,fontsize=20)
  plt.xlabel("real T (°C)",fontsize=18)
  plt.ylabel("measured T(°C)",fontsize=18)

  for spine in plt.gca().spines.values():
      spine.set_linewidth(2)

  if savepath!="":
    plt.savefig(savepath,dpi=200)
  return emisivity_fit
