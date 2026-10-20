from common.io.writeToa import readToa
import numpy as np

reference = r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre\EODP\EODP_TER_2021\EODP-TS-L1C\output"
outdir    = r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre\EODP\EODP_TER_2021\EODP-TS-L1C\output_ruben"

bands = ['VNIR-0', 'VNIR-1', 'VNIR-2', 'VNIR-3']
tol = 0.01e-3
three_sigma = 1 - 0.997

tests = [f'l1c_toa_{band}.nc' for band in bands]

for fname in tests:
    out = readToa(outdir, fname)
    ref = readToa(reference, fname)

    out = np.sort(np.ravel(out))
    ref = np.sort(np.ravel(ref))

    if out.shape != ref.shape:
        print(fname, 'NOK (tamaños distintos:', out.shape, 'vs', ref.shape, ')')
        continue

    with np.errstate(divide="ignore", invalid="ignore"):
        rel = np.abs(out - ref) / np.abs(ref) * 100
    rel[(ref == 0) & (out == 0)] = 0

    n_bad = np.count_nonzero(~(rel <= tol))
    limit = ref.size * three_sigma
    print(fname, 'OK' if n_bad < limit else 'NOK', f'({n_bad} puntos fuera de {ref.size})')