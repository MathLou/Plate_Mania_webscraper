# Plate_Mania_webscraper

Webscraping do site [plate mania](platesmania.com/) com dados apenas das placas de cada estado US, gerada com auxilio de AI e desenvolvido no framewrok python playwrigth.

1. Clone o repositório no seu ambiente de desenvolvimento (Vscode e afins)
2. Criar um ambiente virtual no vscode dentro do diretório com o nome do projeto:
```
  virtualenv <nome_do_ambiente>
```
4. Entre no ambiente virtual:
   ```
     <nome_do_ambiente>/bin/activate
   ```
6. Instale os pacotes necessários:
   ```
     pip install -r requirements.txt
   ```
8. Abra o script [playwrigth_plates_mania.py](https://github.com/MathLou/Plate_Mania_webscraper/blob/main/playwrigth_plate_mania.py) e mude o ```adress```para um dos estados desejados da coluna em rosa [neste link](https://platesmania.com/us/stat):
   
![image](https://github.com/user-attachments/assets/8946f942-75c3-4f97-af6b-db5e639a41bc)

7. Rode e salve em um arquivo .txt com:
   ```
     python playwrigth plates_mania.py >> <nome_do_estado>.txt
   ```
9. Saída da forma:
   ```
   Image 1:
      Main Image URL = https://img03.platesmania.com/241023/m/26223035.jpg
      License Image URL = https://img03.platesmania.com/241023/inf/262230351afe3c.png
      License Plate = MTREE
       (...)
   ```
