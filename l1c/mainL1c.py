# MAIN FUNCTION TO CALL THE L1C MODULE

from l1c.src.l1c_main import l1c

auxdir = r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre\EODP\auxiliary"
indir = (r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre\EODP\EODP_TER_2021\EODP-TS-L1C\input\gm_alt100_act_150,"
         r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre\EODP\EODP_TER_2021\EODP-TS-L1C\input\l1b_output")
outdir = r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre\EODP\EODP_TER_2021\EODP-TS-L1C\output_ruben"

#auxdir = r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre\EODP\auxiliary"
#indir = (r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre\EODP\EODP-TS-E2E\gm_out,"
#         r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre\EODP\EODP-TS-E2E\output_ruben2")
#outdir = r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre\EODP\EODP-TS-E2E\output_ruben3"

# Initialise the ISM
myL1c = l1c(auxdir, indir, outdir)
myL1c.processModule()
