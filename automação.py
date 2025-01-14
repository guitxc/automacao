'''
Nesse codigo irei fazer uma automação basica de adicionar produtos ao sistema de estoque da empressa
Ela sera feita em python e funcionara em primeiro plano
E usara um site de testes para a automação

Primeiro irei fazer o passo a passo
1 - Acessar o sistema
2 - Logar no sistema
3 - Adicionar os produtos
4 - Adiconar todos os produtos ate acabar a tabela

Vou utlizar dois import nesse codigo
O pyautogui - utilizado para fazer comandos automaticamente em primeiro plano
Instalar = pip install pyautogui
O pandas - utilizado para ler a tabela .csv

'''
import pyautogui
import time
# Primeiro passo
pyautogui.PAUSE = 0.3
pyautogui.press("win")
pyautogui.write("Edge")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(1)
# Segundo passo
pyautogui.click(x=687, y=493)
pyautogui.write("teste@email.com")
pyautogui.press("tab")
pyautogui.write("123")
pyautogui.press("tab")
pyautogui.press("enter")
# Terceiro passo
import pandas
tabela = pandas.read_csv("produtos.csv")
for linha in tabela.index:
    pyautogui.click(x=644, y=351)
    pyautogui.write(str(tabela.loc[linha,"codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha,"obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    # Quinto passo
    pyautogui.scroll(9000)