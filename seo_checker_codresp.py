import csv
import requests
import sys

# Nombres de los archivos por defecto
ARCHIVO_ENTRADA = "urls.csv"
ARCHIVO_SALIDA = "informe_resultados.csv"

def comprobar_urls():
    print(f"Leyendo URLs desde '{ARCHIVO_ENTRADA}'...")
    
    try:
        with open(ARCHIVO_ENTRADA, mode='r', encoding='utf-8') as archivo_csv:
            lector = csv.reader(archivo_csv)
            # Intentamos leer la primera columna de cada fila
            urls = [fila[0].strip() for fila in lector if fila]
    except FileNotFoundError:
        print(f"Error: No se encuentra el archivo '{ARCHIVO_ENTRADA}'. Créalo antes de ejecutar el script.")
        return

    resultados = []
    print(f"Analizando {len(urls)} URLs...\n")
    print(f"{'URL':<50} | {'ESTADO':<6}")
    print("-" * 60)

    for url in urls:
        # Ignorar líneas vacías o cabeceras que pongan "url"
        if not url or url.lower() == "url":
            continue
            
        status = "Error"
        try:
            headers = {'User-Agent': 'SEO-Audit-Bot/1.0'}
            # Usamos allow_redirects=True para ver el código final o saber si redirige
            response = requests.get(url, headers=headers, timeout=5, allow_redirects=True)
            status = response.status_code
        except requests.exceptions.RequestException:
            status = "Error de conexión"
            
        print(f"{url:<50} | {str(status):<6}")
        resultados.append([url, status])

    # Guardar resultados en un nuevo CSV
    with open(ARCHIVO_SALIDA, mode='w', newline='', encoding='utf-8') as archivo_salida:
        escritor = csv.writer(archivo_salida)
        # Cabecera del informe
        escritor.writerow(["URL", "Codigo_Estado"])
        # Escribimos todos los resultados
        escritor.writerows(resultados)

    print(f"\n¡Informe generado con éxito! Guardado en '{ARCHIVO_SALIDA}'.")

if __name__ == "__main__":
    comprobar_urls()
