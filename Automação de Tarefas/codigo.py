import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.30

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(2)

pyautogui.click(393, 347)
pyautogui.write('luiz@gmail.com')

pyautogui.press('tab')
pyautogui.write('luizsenha21212')

pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(2)

tabela = pandas.read_csv('produtos.csv')

for linha in tabela.index:
    pyautogui.click(393, 251)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press('tab')

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press('tab')

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press('tab')

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press('tab')

    precoUnitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(precoUnitario)
    pyautogui.press('tab')

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press('tab')

    obs = str(tabela.loc[linha, "obs"])
    pyautogui.write(obs)
    pyautogui.press('tab')

    if obs != "nan":
        pyautogui.write('obs')

    pyautogui.press('enter')