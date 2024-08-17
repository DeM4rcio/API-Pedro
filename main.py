import subprocess

url = "http://tabnet.datasus.gov.br/cgi/csv/dpnibr17239274591.csv"
output_file = "dpnibr17239274591.csv"

try:
    # Usando wget para baixar o arquivo
    # subprocess.run(["wget", url, "-O", output_file], check=True)
    print("Arquivo CSV baixado com sucesso!")
    
    # Ou usando curl (descomente se preferir usar curl)
    subprocess.run(["curl", "-o", output_file, url], check=True)

    # Agora podemos continuar a automação com pandas
    import pandas as pd
    df = pd.read_csv(output_file , encoding="ISO-8859-1")
    print(df.head())  # Exibir as primeiras linhas como exemplo

except subprocess.CalledProcessError as e:
    print(f"Erro ao baixar o arquivo com wget/curl: {e}")
