# MAIN FUNCTION TO CALL THE L1B MODULE

from l1b.src.l1b_main import l1b

# Directory - common directory for the execution of the E2E modules
#auxdir = r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre\EODP\auxiliary"
#indir = r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre\EODP\EODP_TER_2021\EODP-TS-L1B\input"
#outdir = r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre\EODP\EODP_TER_2021\EODP-TS-L1B\output_ruben"

auxdir = r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre\EODP\auxiliary"
indir = r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre\EODP\EODP-TS-E2E\output_ruben"
outdir= r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre\EODP\EODP-TS-E2E\output_ruben2"

# Initialise the L1B module
myL1b = l1b(auxdir, indir, outdir)

# Process the L1B module
myL1b.processModule()
