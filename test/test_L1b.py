from common.io.writeToa import readToa
import numpy as np
import matplotlib.pyplot as plt

from config.globalConfig import globalConfig
myglobal = globalConfig()
bands = myglobal.bands


reference= r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre\EODP\EODP_TER_2021\EODP-TS-L1B\output"
outdir=  r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre\EODP\EODP_TER_2021\EODP-TS-L1B\output_ruben"
outdir2=  r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre\EODP\EODP_TER_2021\EODP-TS-ISM\output_ruben"
outdir_eq=  r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre\EODP\EODP_TER_2021\EODP-TS-L1B\output_ruben_no_eq"

tol = 0.01e-2
three_sigma = 1-0.997

namee = []
name2 = []
name3 = []
name4 = []
for i in range(len(bands)):
    namee.append('l1b_toa_'+'eq_'+str(bands[i])+'.nc')
    name2.append('ism_toa_'+'isrf_'+str(bands[i])+'.nc')
    name3.append('ism_toa_'+'isrf_'+str(bands[i]))
    name4.append(('l1b_toa_'+str(bands[i])+'.nc'))

for inn in range(len(namee)):
    toa_l1b = readToa(outdir,namee[inn])
    toa_input = readToa(reference,namee[inn])
    toa_l1b_eq = readToa(outdir_eq,name4[inn])
    toa_lib_eq_input = readToa(outdir_eq,name4[inn])

    counter = 0
    counter_eq = 0
    points_treshold = toa_input.shape[0]*toa_input.shape[1]*three_sigma

    result =np.zeros((toa_l1b.shape[0],toa_l1b.shape[1]))
    result_eq =np.zeros((toa_l1b_eq.shape[0],toa_l1b_eq.shape[1]))
    for i in range(toa_l1b.shape[0]):
        for j in range(toa_l1b.shape[1]):
            result[i,j]=toa_l1b[i,j]-toa_input[i,j]
            result_eq[i,j] - toa_l1b_eq[i,j]-toa_lib_eq_input[i,j]

            if np.abs(result[i,j]>tol):
                counter += 1

            if np.abs(result_eq[i,j]>tol):
                counter_eq += 1
    print('Band '+bands[inn])
    if counter < points_treshold:
        print('Test with eq ' + namee[inn] + ' OK')
    else:
        print('Test with eq ' + namee[inn] + ' NOK')

    if counter_eq < points_treshold:
        print('Test with no eq ' + name4[inn] + ' OK')
    else:
        print('Test with no eq ' + name4[inn] + ' NOK')

    toa_ism = readToa(outdir2,name2[inn])
    mid_value = int(toa_ism.shape[0]/2)
    fig2,ax2 = plt.subplots()
    plt.grid(True)
    plt.suptitle('Alt = '+str(mid_value))
    plt.xlabel('Across Track [-]')
    plt.ylabel('Radiances [mW/m2/sr]')
    ax2.plot(toa_ism[mid_value,:],'k')
    fig2.savefig(outdir+'/'+name3[inn]+'_graph.png')
    #plt.show()

    toa_1 = readToa(outdir,namee[inn])
    mid_value_1 = int(toa_1.shape[0]/2)
    fig4,ax4 = plt.subplots()
    plt.grid(True)
    plt.suptitle('Alt = '+str(mid_value))
    plt.xlabel('Across Track [-]')
    plt.ylabel('Radiances [mW/m2/sr]')
    ax4.plot(toa_1[mid_value,:],'k')
    fig4.savefig(outdir+'/'+namee[inn]+'equalized'+'_graph.png')
    #plt.show()







    toa_eq = readToa(outdir_eq,name4[inn])
    mid_value = int(toa_eq.shape[0]/2)
    fig3,ax3 = plt.subplots()
    plt.grid(True)
    plt.suptitle('Alt = '+str(mid_value))
    plt.xlabel('Across Track [-]')
    plt.ylabel('Radiances [mW/m2/sr]')
    ax3.plot(toa_eq[mid_value,:],'k')
    fig3.savefig(outdir_eq+'/'+name4[inn]+'_non_equalized'+'_graph.png')
    #plt.show()