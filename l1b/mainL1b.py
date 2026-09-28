# MAIN FUNCTION TO CALL THE L1B MODULE

from l1b.src.l1b import l1b

# Directory - common directory for the execution of the E2E modules
auxdir = r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre\EODP\auxiliary"
indir = r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre\EODP\EODP_TER_2021\EODP-TS-L1B\input"
outdir = r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre\EODP\EODP_TER_2021\EODP-TS-L1B\output_ruben"

# Initialise the L1B module
myL1b = l1b(auxdir, indir, outdir)

# Process the L1B module
myL1b.processModule()
