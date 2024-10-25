# Plate_Mania_webscraper

Webscraping do site [plate mania](platesmania.com/) com dados apenas das placas de cada estado US, gerada com auxilio de AI e desenvolvido no framewrok python playwrigth.

1. Clone o repositório no seu ambiente de desenvolvimento (Vscode e afins)
2. Criar um ambiente virtual no vscode dentro do diretório com o nome do projeto:
  `virtualenv <nome_do_ambiente>`
3. Entre no ambiente virtual:
   `<nome_do_ambiente>/bin/activate`
4. Instale os pacotes necessários:
   `pip install -r requirements.txt`
5. Abra o script [playwrigth_plates_mania.py]() e mude o ```adress```para um dos estados desejados [neste link](https://platesmania.com/us/stat), desta forma:
![image](https://github.com/user-attachments/assets/8946f942-75c3-4f97-af6b-db5e639a41bc)
6. Rode e salve em um arquivo .txt com:
   `python playwrigth plates_mania.py >> <nome_do_estado>.txt`
