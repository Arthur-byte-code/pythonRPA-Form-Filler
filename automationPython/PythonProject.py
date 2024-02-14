import pyautogui
import time
pyautogui.PAUSE=1
pyautogui.press("win")
pyautogui.write("microsoft edge")
pyautogui.press("enter")
time.sleep(5)
link = "file:///C:/Users/PutYourPcNameHere/Desktop/automationPython/Formul%C3%A1rio.html"
pyautogui.write(link)
time.sleep(8)
pyautogui.press("enter")

time.sleep(5)
 
import pandas 
tabela = pandas.read_csv("produtos.csv")
for linha in tabela.index: 

    
    pyautogui.click(x=634, y=130)
    
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")

    
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

   
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write((str(tabela.loc[linha, "preco_unitario"])))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs=tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)

    
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
 
