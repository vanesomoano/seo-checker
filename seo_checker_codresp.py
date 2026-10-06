import csv
import requests

# Lista de URLs de ejemplo para auditar (puedes cambiarlas o cargarlas desde un archivo)
urls = [
    "https://example.com",
    "https://example.com/blog",
    "https://example.com/contacto",
    "https://example.com/pagina-no-existe"
]

def comprobar_urls(lista_urls):
    print(f"{'URL':<40} | {'ESTADO':<6}")
    print("-" * 50)
    
    for url in lista_urls:
        try:
            # Hacemos una petición con un User-Agent simulando un bot o navegador
            headers = {'User-Agent': 'SEO-Audit-Bot/1.0'}
            response = requests.get(url, headers=headers, timeout=5)
            status = response.status_code
        except requests.exceptions.RequestException:
            status = "Error de conexión"
            
        print(f"{url:<40} | {str(status):<6}")

if __name__ == "__main__":
    comprobar_urls(urls)
