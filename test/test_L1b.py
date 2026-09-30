import os
import numpy as np
from netCDF4 import Dataset


# Resultados de referencia
reference_dir = (
    r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre"
    r"\EODP\EODP_TER_2021\EODP-TS-L1B\output"
)

# Resultados generados por nosotros
results_dir = (
    r"C:\Users\rubik\OneDrive\Escritorio\Master\5 Semisemestre"
    r"\EODP\EODP_TER_2021\EODP-TS-L1B\output_ruben"
)


def compare_files(reference_file, results_file):

    print(f"\nComparando {os.path.basename(reference_file)}")

    with Dataset(reference_file, "r") as reference:
        with Dataset(results_file, "r") as results:

            # Variables de cada archivo
            reference_variables = set(reference.variables.keys())
            results_variables = set(results.variables.keys())

            if reference_variables != results_variables:
                print("ERROR: Las variables no coinciden.")
                return False

            # Comparar cada variable
            for variable in reference_variables:

                reference_data = reference.variables[variable][:]
                results_data = results.variables[variable][:]

                if reference_data.shape != results_data.shape:
                    print(f"ERROR: Dimensiones diferentes en {variable}")
                    return False

                if not np.allclose(
                    reference_data,
                    results_data,
                    rtol=1e-5,
                    atol=1e-8,
                    equal_nan=True
                ):
                    max_difference = np.max(
                        np.abs(
                            np.asarray(reference_data)
                            - np.asarray(results_data)
                        )
                    )

                    print(
                        f"ERROR: Diferencias en {variable}. "
                        f"Máxima diferencia: {max_difference}"
                    )

                    return False

    print("OK")
    return True


def main():

    print("========================================")
    print("          TEST DEL MODULO L1B")
    print("========================================")

    reference_files = {
        f for f in os.listdir(reference_dir)
        if f.endswith(".nc")
    }

    results_files = {
        f for f in os.listdir(results_dir)
        if f.endswith(".nc")
    }

    # Comprobar que existen los mismos archivos
    if reference_files != results_files:

        print("ERROR: Las carpetas no contienen los mismos archivos.")

        print("\nSolo en output:")
        for f in sorted(reference_files - results_files):
            print(f)

        print("\nSolo en output_ruben:")
        for f in sorted(results_files - reference_files):
            print(f)

        return

    all_ok = True

    for filename in sorted(reference_files):

        reference_file = os.path.join(reference_dir, filename)
        results_file = os.path.join(results_dir, filename)

        if not compare_files(reference_file, results_file):
            all_ok = False

    print("\n========================================")

    if all_ok:
        print("L1B TEST: PASSED")
    else:
        print("L1B TEST: FAILED")

    print("========================================")


if __name__ == "__main__":
    main()