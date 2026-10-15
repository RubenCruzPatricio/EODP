
# MAIN FUNCTION TO CALL THE L1C MODULE

from l1c.src.l1c_main import l1c

auxdir = r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre\EODP\auxiliary"
indir = r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre\EODP\EODP_TER_2021\EODP-TS-L1C\input"
outdir = r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre\EODP\EODP_TER_2021\EODP-TS-L1C\output_ruben"

# Initialise the ISM
myL1c = l1c(auxdir, indir, outdir)
myL1c.processModule()
