import numpy as np
from common.io.writeToa import readToa
reference = r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre\EODP\EODP_TER_2021\EODP-TS-L1B\output"
outdir    = r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre\EODP\EODP_TER_2021\EODP-TS-L1B\output_ruben"

bands = ['VNIR-0', 'VNIR-1', 'VNIR-2', 'VNIR-3']
tol = 0.001
three_sigma = 1 - 0.997

prefixes = ['l1b_toa_eq_', 'l1b_toa_']
fnames = [f'{p}{band}.nc' for band in bands for p in prefixes]

for fname in fnames:
    out = readToa(outdir, fname)
    ref = readToa(reference, fname)

    with np.errstate(divide="ignore", invalid="ignore"):
        rel = np.abs(out - ref) / np.abs(ref)
    rel[(ref == 0) & (out == 0)] = 0

    n_bad = np.count_nonzero(rel > tol)
    limit = ref.shape[0] * ref.shape[1] * three_sigma
    print(fname, 'OK' if n_bad < limit else 'NOK')