from selenium import webdriver
from requests import get
import time
import random

# URL do site
url = "https://devaneioa.blogspot.com/2024/04/a-danca-entre-ordem-e-caos-uma.html"

# Número de visualizações
numero_visualizacoes = 20000

# Opções do navegador (opcional)
options = webdriver.ChromeOptions()
options.add_argument("--headless")

# Abrindo o navegador
try:
  driver = webdriver.Chrome(options=options)
except Exception as e:
  print(f"Erro ao abrir o navegador: {e}")
  exit()

# Loop para gerar visualizações
for i in range(numero_visualizacoes):
  try:
    # Acessando o site
    driver.get(url)

    # Simulando tempo de espera (opcional)
    time.sleep(random.randint(2, 5))

  except Exception as e:
    print(f"Erro ao acessar o site: {e}")

# Fechando o navegador
try:
  driver.quit()
except Exception as e:
  print(f"Erro ao fechar o navegador: {e}")

# Imprimindo mensagem de finalização
print(f"Total de visualizações: {numero_visualizacoes}")
