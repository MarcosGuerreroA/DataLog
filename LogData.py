import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import lasio
import matplotlib.backends.backend_pdf

from PIL import Image

pathsIcon = ['Icon/Inteligent Reservoir.png', 'Icon/Litology.png']

pathDir = "Textura standar StrataID/"
imagenes = ['Anhydrite', 'Bentonite', 'Bony coal or impure coal', 
            'Breccia', 'Calcareous sandstone', 'Calcareous siltstone',
            'Carbonate wash', 'Chalk', 'Chert', 'Cherty limestone', 
            'Clastic limestone', 'Claystone', 'Coal', 'Conglomerate',
            'Dolomitic sandstone', 'Dolomitic shale', 'Dolomitic siltstone',
            'Dolostone or dolomite', 'Fossiliferous clastic limestone', 'Granite wash', 
            'Limestone', 'Limonite', 'Marl', 'Metamorphism', 'Oil shale',
            'Oolitic limestone', 'Plutonic rock', 'Quartz wash', 'Quartzite',
            'Salt', 'Sand', 'Sandstone', 'Sandy limestone', 'Shale', 'Siltstone',
            'Silty limestone', 'Subgraywacke', 'Unknown Litho', 'Volcanic rock', 'not sample', 'Cement', 'Gypsum', 'Red Shale']


for x in imagenes:
    print(str(imagenes.index(x)) +' '+ str(x))


def GenerateDataIndex(top_depth, bottom_depth, litho):
    DepthMaster = pd.Series(np.arange(int(top_depth), int(bottom_depth)))
    DFDephMaster = pd.DataFrame()
    DFDephMaster.insert(0, 'DEPTH', DepthMaster)
    DFDephMaster[litho] = np.nan
    return DFDephMaster

def GenerateIndex(top_depth, bottom_depth):
    interval = 100
    values = []
    value = top_depth
    while(True):
        if value >= bottom_depth:
            break
        else:
            if len(values) == 0:
                values.append(value)
            else:
                value = value + interval
                values.append(value)
    return values

def GetIndexDepthImage(top_depth, bottom_depth):
    ListDepths = list()
    ControlDepth = 0
    
    while True:
        if ControlDepth < bottom_depth:
            if len(ListDepths) <= 0:
                ListDepths.append(top_depth)
                ControlDepth = top_depth
            else:
                ControlDepth += 1000
                ListDepths.append(ControlDepth)
        else:
            break
    return ListDepths


las = lasio.read('FileLas-MCCLINTIC 12C 3H.las')
data = las.df()
data = data.replace([-999.25],[np.NaN])

data['DMEA']=data.index

def triple_combo_plot(top_depth,bottom_depth):
    if len(str(int(top_depth))) > 3:
        top_depth = int(top_depth / 1000) * 1000
    if len(str(int(top_depth))) > 2 and len(str(int(top_depth))) >= 3:
        top_depth = int(top_depth / 100) * 100

    logs=data[(data.DMEA >= top_depth) & (data.DMEA <= bottom_depth)]
    fig, ax = plt.subplots(ncols=8, figsize=(25,400),gridspec_kw={'width_ratios': [0.5, 0.1, 0.08, 0.08, 0.9, 0.9, 0.9,0.9],'height_ratios': [5]})
    fig.subplots_adjust(top=0.992,wspace=0)
    
    ax[0].set_xlim(0, 100)
    ax[0].set_xticks([0,10,20,30,40,50,60,70,80,90,100])
    ax[0].set_ylim(top_depth, bottom_depth)
    ax[0].set_yticks(GenerateIndex(top_depth, bottom_depth))
    ax[0].invert_yaxis()
    ax[0].xaxis.grid(True)
    ax[0].yaxis.grid(True)
    ax[0].get_xaxis().set_visible(True)  
    ax[1].set_yticks([])
    ax[1].set_xticks([])

    ax51=ax[0].twiny()
    ax51.set_xlim(0, 100)
    ax51.set_xticks([0,10,20,30,40,50,60,70,80,90,100])
    ax51.xaxis.grid(False)
    ax51.yaxis.grid(False)
    ax51.get_xaxis().set_visible(False) 

    ax52=ax[0].twiny()
    ax52.set_xlim(0, 100)
    ax52.set_xticks([0,10,20,30,40,50,60,70,80,90,100])
    ax52.xaxis.grid(False)
    ax52.yaxis.grid(False)
    ax52.get_xaxis().set_visible(False) 
    
    ax53=ax[0].twiny()
    ax53.set_xlim(0, 100)
    ax53.set_xticks([0,10,20,30,40,50,60,70,80,90,100])
    ax53.xaxis.grid(False)
    ax53.yaxis.grid(False)
    ax53.get_xaxis().set_visible(False) 

    ax54=ax[0].twiny()
    ax54.set_xlim(0, 100)
    ax54.set_xticks([0,10,20,30,40,50,60,70,80,90,100])
    ax54.xaxis.grid(False)
    ax54.yaxis.grid(False)
    ax54.get_xaxis().set_visible(False) 

    ax55=ax[0].twiny()
    ax55.set_xlim(0, 100)
    ax55.set_xticks([0,10,20,30,40,50,60,70,80,90,100])
    ax55.xaxis.grid(False)
    ax55.yaxis.grid(False)
    ax55.get_xaxis().set_visible(False) 

    ax56=ax[0].twiny()
    ax56.set_xlim(0, 100)
    ax56.set_xticks([0,10,20,30,40,50,60,70,80,90,100])
    ax56.xaxis.grid(False)
    ax56.yaxis.grid(False)
    ax56.get_xaxis().set_visible(False) 

    ax57=ax[0].twiny()
    ax57.set_xlim(0, 100)
    ax57.set_xticks([0,10,20,30,40,50,60,70,80,90,100])
    ax57.xaxis.grid(False)
    ax57.yaxis.grid(False)
    ax57.get_xaxis().set_visible(False) 
    
    ax58=ax[0].twiny()
    ax58.set_xlim(0, 100)
    ax58.set_xticks([0,10,20,30,40,50,60,70,80,90,100])
    ax58.xaxis.grid(False)
    ax58.yaxis.grid(False)
    ax58.get_xaxis().set_visible(False) 

    ax59=ax[0].twiny()
    ax59.set_xlim(0, 100)
    ax59.set_xticks([0,10,20,30,40,50,60,70,80,90,100])
    ax59.xaxis.grid(False)
    ax59.yaxis.grid(False)
    ax59.get_xaxis().set_visible(False)  
    
    lithologys = ['ANHYDRITE', 'ASH', 'CEMENT', 'LIMESTONE', 'NOSAMPLE', 'SALT', 'SAND', 'SHALE', 'SHALERED']
    lithologyDataStart = {}
    lithologyDataEnd = {}
    
    for lithos in lithologys:
       lithologyDataStart[lithos] = GenerateDataIndex(top_depth, bottom_depth, lithos)
       lithologyDataEnd[lithos] = GenerateDataIndex(top_depth, bottom_depth, lithos)
    
    
    for depth in logs['DMEA']:
        start = 0
        end = 0    
        DFStart = None
        DFEnd = None
        
        for lithology in lithologys:  
            DFStart = lithologyDataStart.get(lithology)
            DFEnd = lithologyDataEnd.get(lithology)
            #if str.upper(lithology) == str.upper(list(lithologyData.keys())[0]):

            if int(logs[str.upper(lithology)][depth]) > 0:
                if start == 0:
                    DFStart.loc[DFStart.index[DFStart['DEPTH'] == depth], lithology] = 0
                    DFEnd.loc[DFEnd.index[DFEnd['DEPTH'] == depth], lithology] = (start + int(logs[str.upper(lithology)][depth]))
                    end = start + int(logs[str.upper(lithology)][depth])
                    start = start + int(logs[str.upper(lithology)][depth]) 
                elif start > 0:
                    DFStart.loc[DFStart.index[DFStart['DEPTH'] == depth], lithology] = start
                    DFEnd.loc[DFEnd.index[DFEnd['DEPTH'] == depth], lithology] = (start + int(logs[str.upper(lithology)][depth]))
                    end = start + int(logs[str.upper(lithology)][depth])
                    start = start + int(logs[str.upper(lithology)][depth])       
            else:
                DFStart.loc[DFStart.index[DFStart['DEPTH'] == depth], lithology] = int(logs[str.upper(lithology)][depth])
                DFEnd.loc[DFEnd.index[DFEnd['DEPTH'] == depth], lithology] = (int(logs[str.upper(lithology)][depth]))
                       
            lithologyDataStart[lithology] = DFStart
            lithologyDataEnd[lithology] = DFEnd

    index = 30
    print(int(top_depth),int(bottom_depth), imagenes[index])
    ListDepths = GetIndexDepthImage(int(top_depth),int(bottom_depth))
    #ax[0].set_yticks(ListDepths)
    
    for CDepth in ListDepths:
        
        lithoStart1 = lithologyDataStart.get('ANHYDRITE')
        lithoEnd1 = lithologyDataEnd.get('ANHYDRITE') 
        ControlStart1 = pd.DataFrame() 
        ControlEnd1 = pd.DataFrame()
        if lithoStart1 is not None and lithoEnd1 is not None:
            lithoStart1.fillna(0, inplace=True)
            lithoEnd1.fillna(0, inplace=True)
            ControlStart1 = lithoStart1.loc[(lithoStart1['DEPTH'] >= CDepth) & (lithoStart1['DEPTH'] <= CDepth + 1000)]
            ControlEnd1 = lithoEnd1.loc[(lithoEnd1['DEPTH'] >= CDepth) & (lithoEnd1['DEPTH'] <= CDepth + 1000)]  

        lithoStart2 = lithologyDataStart.get('ASH')
        lithoEnd2 = lithologyDataEnd.get('ASH')  
        ControlStart2 = pd.DataFrame() 
        ControlEnd2 = pd.DataFrame()
        if lithoStart2 is not None and lithoEnd2 is not None:     
            lithoStart2.fillna(0, inplace=True)
            lithoEnd2.fillna(0, inplace=True)
            ControlStart2 = lithoStart2.loc[(lithoStart2['DEPTH'] >= CDepth) & (lithoStart2['DEPTH'] <= CDepth + 1000)]
            ControlEnd2 = lithoEnd2.loc[(lithoEnd2['DEPTH'] >= CDepth) & (lithoEnd2['DEPTH'] <= CDepth + 1000)] 

        lithoStart3 = lithologyDataStart.get('CEMENT')
        lithoEnd3 = lithologyDataEnd.get('CEMENT')
        ControlStart3 = pd.DataFrame()  
        ControlEnd3 = pd.DataFrame()
        if lithoStart3 is not None and lithoEnd3 is not None:       
            lithoStart3.fillna(0, inplace=True)
            lithoEnd3.fillna(0, inplace=True)
            ControlStart3 = lithoStart3.loc[(lithoStart3['DEPTH'] >= CDepth) & (lithoStart3['DEPTH'] <= CDepth + 1000)]
            ControlEnd3 = lithoEnd3.loc[(lithoEnd3['DEPTH'] >= CDepth) & (lithoEnd3['DEPTH'] <= CDepth + 1000)] 

        lithoStart4 = lithologyDataStart.get('LIMESTONE')
        lithoEnd4 = lithologyDataEnd.get('LIMESTONE') 
        ControlStart4 = pd.DataFrame()  
        ControlEnd4 = pd.DataFrame()   
        if lithoStart4 is not None and lithoEnd4 is not None:   
            lithoStart4.fillna(0, inplace=True)
            lithoEnd4.fillna(0, inplace=True)
            ControlStart4 = lithoStart4.loc[(lithoStart4['DEPTH'] >= CDepth) & (lithoStart4['DEPTH'] <= CDepth + 1000)]
            ControlEnd4 = lithoEnd4.loc[(lithoEnd4['DEPTH'] >= CDepth) & (lithoEnd4['DEPTH'] <= CDepth + 1000)] 

        lithoStart5 = lithologyDataStart.get('NOSAMPLE')
        lithoEnd5 = lithologyDataEnd.get('NOSAMPLE')  
        ControlStart5 = pd.DataFrame()  
        ControlEnd5 = pd.DataFrame() 
        if lithoStart5 is not None and lithoEnd5 is not None:  
            lithoStart5.fillna(0, inplace=True)
            lithoEnd5.fillna(0, inplace=True)
            ControlStart5 = lithoStart5.loc[(lithoStart5['DEPTH'] >= CDepth) & (lithoStart5['DEPTH'] <= CDepth + 1000)]
            ControlEnd5 = lithoEnd5.loc[(lithoEnd5['DEPTH'] >= CDepth) & (lithoEnd5['DEPTH'] <= CDepth + 1000)] 

        lithoStart6 = lithologyDataStart.get('SALT')
        lithoEnd6 = lithologyDataEnd.get('SALT')    
        ControlStart6 = pd.DataFrame()  
        ControlEnd6 = pd.DataFrame()
        if lithoStart6 is not None and lithoEnd6 is not None:   
            lithoStart6.fillna(0, inplace=True)
            lithoEnd6.fillna(0, inplace=True)
            ControlStart6 = lithoStart6.loc[(lithoStart6['DEPTH'] >= CDepth) & (lithoStart6['DEPTH'] <= CDepth + 1000)]
            ControlEnd6 = lithoEnd6.loc[(lithoEnd6['DEPTH'] >= CDepth) & (lithoEnd6['DEPTH'] <= CDepth + 1000)] 

        lithoStart7 = lithologyDataStart.get('SAND')
        lithoEnd7 = lithologyDataEnd.get('SAND')  
        ControlStart7 = pd.DataFrame()
        ControlEnd7 = pd.DataFrame()
        if lithoStart7 is not None and lithoEnd7 is not None:    
            lithoStart7.fillna(0, inplace=True)
            lithoEnd7.fillna(0, inplace=True)
            ControlStart7 = lithoStart7.loc[(lithoStart1['DEPTH'] >= CDepth) & (lithoStart7['DEPTH'] <= CDepth + 1000)]
            ControlEnd7 = lithoEnd7.loc[(lithoEnd1['DEPTH'] >= CDepth) & (lithoEnd7['DEPTH'] <= CDepth + 1000)] 

        lithoStart8 = lithologyDataStart.get('SHALE')
        lithoEnd8 = lithologyDataEnd.get('SHALE')  
        ControlStart8 = pd.DataFrame()  
        ControlEnd8 = pd.DataFrame()
        if lithoStart8 is not None and lithoEnd8 is not None:     
            lithoStart8.fillna(0, inplace=True)
            lithoEnd8.fillna(0, inplace=True)
            ControlStart8 = lithoStart8.loc[(lithoStart8['DEPTH'] >= CDepth) & (lithoStart8['DEPTH'] <= CDepth + 1000)]
            ControlEnd8 = lithoEnd8.loc[(lithoEnd8['DEPTH'] >= CDepth) & (lithoEnd8['DEPTH'] <= CDepth + 1000)] 

        lithoStart9 = lithologyDataStart.get('SHALERED')
        lithoEnd9 = lithologyDataEnd.get('SHALERED')  
        ControlStart9 = pd.DataFrame()
        ControlEnd9 = pd.DataFrame()
        if lithoStart9 is not None and lithoEnd9 is not None:    
            lithoStart9.fillna(0, inplace=True)
            lithoEnd9.fillna(0, inplace=True)
            ControlStart9 = lithoStart9.loc[(lithoStart9['DEPTH'] >= CDepth) & (lithoStart9['DEPTH'] <= CDepth + 1000)]
            ControlEnd9 = lithoEnd9.loc[(lithoEnd9['DEPTH'] >= CDepth) & (lithoEnd9['DEPTH'] <= CDepth + 1000)] 


        image1 = ax51.imshow(Image.open(pathDir + imagenes[0] + '.png'), cmap=plt.cm.gray, extent=[100, 0, CDepth+1000, CDepth])
        if 'ANHYDRITE' in ControlStart1:
            if ControlStart1['ANHYDRITE'].count() > 0: 
                poly1 = ax51.fill_betweenx(ControlStart1['DEPTH'], ControlStart1['ANHYDRITE'], ControlEnd1['ANHYDRITE'], facecolor='none', visible=False)
                clip1 = poly1.get_paths()[0]
                image1.set_clip_path(clip1, transform=ax51.transData)
        
        image2 = ax52.imshow(Image.open(pathDir + imagenes[3] + '.png'), cmap=plt.cm.gray, extent=[100, 0, CDepth+1000, CDepth])
        if 'ASH' in ControlStart2:
            if ControlStart2['ASH'].count() > 0: 
                poly2 = ax52.fill_betweenx(ControlStart2['DEPTH'], ControlStart2['ASH'], ControlEnd2['ASH'], facecolor='none', visible=False)
                clip2 = poly2.get_paths()[0]
                image2.set_clip_path(clip2, transform=ax52.transData)

        image3 = ax53.imshow(Image.open(pathDir + imagenes[40] + '.png'), cmap=plt.cm.gray, extent=[100, 0, CDepth+1000, CDepth])
        if 'CEMENT' in ControlStart3:
            if ControlStart3['CEMENT'].count() > 0: 
                poly3 = ax53.fill_betweenx(ControlStart3['DEPTH'], ControlStart3['CEMENT'], ControlEnd3['CEMENT'], facecolor='none', visible=False)
                clip3 = poly3.get_paths()[0]
                image3.set_clip_path(clip3, transform=ax53.transData)

        image4 = ax54.imshow(Image.open(pathDir + imagenes[20] + '.png'), cmap=plt.cm.gray, extent=[100, 0, CDepth+1000, CDepth])
        if 'LIMESTONE' in ControlStart4:
            if ControlStart4['LIMESTONE'].count() > 0: 
                poly4 = ax54.fill_betweenx(ControlStart4['DEPTH'], ControlStart4['LIMESTONE'], ControlEnd4['LIMESTONE'], facecolor='none', visible=False)
                clip4 = poly4.get_paths()[0]
                image4.set_clip_path(clip4, transform=ax54.transData)

        image5 = ax55.imshow(Image.open(pathDir + imagenes[39] + '.png'), cmap=plt.cm.gray, extent=[100, 0, CDepth+1000, CDepth])
        if 'NOSAMPLE' in ControlStart5:
            if ControlStart5['NOSAMPLE'].count() > 0: 
                poly5 = ax55.fill_betweenx(ControlStart5['DEPTH'], ControlStart5['NOSAMPLE'], ControlEnd5['NOSAMPLE'], facecolor='none', visible=False)
                clip5 = poly5.get_paths()[0]
                image5.set_clip_path(clip5, transform=ax55.transData)

        image6 = ax56.imshow(Image.open(pathDir + imagenes[29] + '.png'), cmap=plt.cm.gray, extent=[100, 0, CDepth+1000, CDepth])
        if 'SALT' in ControlStart6:
            if ControlStart6['SALT'].count() > 0: 
                poly6 = ax56.fill_betweenx(ControlStart6['DEPTH'], ControlStart6['SALT'], ControlEnd6['SALT'], facecolor='none', visible=False)
                clip6 = poly6.get_paths()[0]
                image6.set_clip_path(clip6, transform=ax56.transData)

        image7 = ax57.imshow(Image.open(pathDir + imagenes[30] + '.png'), cmap=plt.cm.gray, extent=[100, 0, CDepth+1000, CDepth])
        if 'SAND' in ControlStart7:
            if ControlStart7['SAND'].count() > 0: 
                poly7 = ax57.fill_betweenx(ControlStart7['DEPTH'], ControlStart7['SAND'], ControlEnd7['SAND'], facecolor='none', visible=False)
                clip7 = poly7.get_paths()[0]
                image7.set_clip_path(clip7, transform=ax57.transData)

        image8 = ax58.imshow(Image.open(pathDir + imagenes[33] + '.png'), cmap=plt.cm.gray, extent=[100, 0, CDepth+1000, CDepth])
        if 'SHALE' in ControlStart8:
            if ControlStart8['SHALE'].count() > 0: 
                poly8 = ax58.fill_betweenx(ControlStart8['DEPTH'], ControlStart8['SHALE'], ControlEnd8['SHALE'], facecolor='none', visible=False)
                clip8 = poly8.get_paths()[0]
                image8.set_clip_path(clip8, transform=ax58.transData)

        image9 = ax59.imshow(Image.open(pathDir + imagenes[42] + '.png'), cmap=plt.cm.gray, extent=[100, 0, CDepth+1000, CDepth])
        if 'SHALERED' in ControlStart9:
            if ControlStart9['SHALERED'].count() > 0: 
                poly9 = ax59.fill_betweenx(ControlStart9['DEPTH'], ControlStart9['SHALERED'], ControlEnd9['SHALERED'], facecolor='none', visible=False)
                clip9 = poly9.get_paths()[0]
                image9.set_clip_path(clip9, transform=ax59.transData)




    
    ax[0].grid(True)
    pdf = matplotlib.backends.backend_pdf.PdfPages("outputTestLog.pdf")
    #pdf.savefig(FigSeconnd, edgecolor='white')
    pdf.savefig(fig, edgecolor='white')
    pdf.close()
    plt.show()


triple_combo_plot(data.DMEA.min(), data.DMEA.max())