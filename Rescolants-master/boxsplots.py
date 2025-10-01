import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
import zipfile

#base = Path("prueba_automatizada/Results")
zip_path = Path("prueba_automatizada/Results.zip")
subcarpetas = ["CN", "QN"]
tiempos = ["10s", "30s", "60s"]  # Ajusta si tus carpetas tienen nombres distintos

with zipfile.ZipFile(zip_path) as zf:
    base = zipfile.Path(zf, "Results")

    for sub in subcarpetas:
        filas = []

        for t in tiempos:
            carpeta = base / sub / t
            if not carpeta.exists():
                continue

            for f in carpeta.rglob("nuevos.csv"):
                with f.open("r") as archivo:
                    df = pd.read_csv(archivo, header=None)
                df.columns = [
                    "segmento", "algoritmo", "mejor_costo", "mejor_longitud",
                    "nodo_inicio", "nodo_fin", "tiempo_us", "long_tour",
                    "long_salida", "arcos", "costo_recoleccion", "costo_recorrer"
                ]
                df["tiempo"] = t                # Añade la etiqueta de tiempo
                filas.append(df)

        if not filas:
            print(f"No se encontraron archivos para {sub}")
            continue

        datos = pd.concat(filas, ignore_index=True)

        plt.figure(figsize=(10, 6))
        sns.boxplot(
            data=datos,
            x="algoritmo",
            y="mejor_costo",
            hue="tiempo",   # Se diferencian los 3 tiempos
            palette="Set2"  # Colores opcionales
        )
        plt.title(f"Costo por algoritmo y tiempo ({sub})")
        plt.ylabel("Costo")
        plt.xlabel("Algoritmo")
        plt.legend(title="Tiempo")
        plt.tight_layout()
        plt.savefig(f"boxplot_{sub}_tiempos.jpg", dpi=300, bbox_inches="tight")
        plt.close()

        print(f"Guardado: boxplot_{sub}_tiempos.jpg")

# for sub in subcarpetas:
#     filas = []

#     for t in tiempos:
#         carpeta = base / sub / t
#         for f in carpeta.rglob("nuevos.csv"):
#             df = pd.read_csv(f, header=None)
#             df.columns = [
#                 "segmento", "algoritmo", "mejor_costo", "mejor_longitud",
#                 "nodo_inicio", "nodo_fin", "tiempo_us", "long_tour",
#                 "long_salida", "arcos", "costo_recoleccion", "costo_recorrer"
#             ]
#             df["tiempo"] = t                # Añade la etiqueta de tiempo
#             filas.append(df)

#     if not filas:
#         print(f"No se encontraron archivos para {sub}")
#         continue

#     datos = pd.concat(filas, ignore_index=True)

#     plt.figure(figsize=(10, 6))
#     sns.boxplot(
#         data=datos,
#         x="algoritmo",
#         y="mejor_costo",
#         hue="tiempo",   # Se diferencian los 3 tiempos
#         palette="Set2"  # Colores opcionales
#     )
#     plt.title(f"Costo por algoritmo y tiempo ({sub})")
#     plt.ylabel("Costo")
#     plt.xlabel("Algoritmo")
#     plt.legend(title="Tiempo")
#     plt.tight_layout()
#     plt.savefig(f"boxplot_{sub}_tiempos.jpg", dpi=300, bbox_inches="tight")
#     plt.close()

#     print(f"Guardado: boxplot_{sub}_tiempos.jpg")