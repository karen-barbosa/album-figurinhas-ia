import urllib.request
import json
import sys

def test_api():
    try:
        # Testa /figurinhas
        with urllib.request.urlopen("http://127.0.0.1:8000/figurinhas") as response:
            status = response.getcode()
            content = response.read().decode('utf-8')
            print("Status GET /figurinhas:", status)
            data = json.loads(content)
            print("Quantidade de figurinhas:", len(data))
            # Pega a última figurinha da lista
            print("Última figurinha:", data[-1])
            
        # Testa imagem ID 30 (Karen Barbosa)
        with urllib.request.urlopen("http://127.0.0.1:8000/figurinhas/30/imagem") as response:
            status = response.getcode()
            headers = response.info()
            img_data = response.read()
            print("\nStatus GET /figurinhas/30/imagem:", status)
            print("Content-Type da imagem:", headers.get_content_type())
            print("Tamanho da imagem:", len(img_data), "bytes")
            
    except Exception as e:
        print("Erro durante o teste:", e)

if __name__ == "__main__":
    test_api()
