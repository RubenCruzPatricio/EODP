
# MAIN FUNCTION TO CALL THE ISM MODULE

from ism.src.ism import ism

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = r'C:\\Users\\rubik\\OneDrive\\Escritorio\\Master\\5 Semisemestre\\EODP\\auxiliary'
indir = r"C:\\Users\\rubik\\OneDrive\\Escritorio\\Master\\5 Semisemestre\\EODP\\EODP_TER_2021\\EODP-TS-L1B\\input"
outdir = r"C:\\Users\\rubik\\OneDrive\\Escritorio\\Master\\5 Semisemestre\\EODP\\EODP_TER_2021\\EODP-TS-L1B\\output_ruben

# Initialise the ISM
myIsm = ism(auxdir, indir, outdir)
myIsm.processModule()
