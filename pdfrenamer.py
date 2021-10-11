from PIL import ImageOps
import pyautogui as pag
import sys
import time

winexploc = pag.locateCenterOnScreen('images/filefolder.png', confidence = 0.8)
iecopyloc = pag.locateCenterOnScreen('images/iecopy.png', confidence = 0.8) 
pdfloc = pag.locateAllOnScreen('images/pdflogo.png', confidence=0.8 )
pdfieloc = pag.locateAllOnScreen('images/pdfie.png', confidence=0.8)
msedgeloc = pag.locateCenterOnScreen('images/msedge.png', confidence=0.85)

pag.FAILSAFE = True
pag.PAUSE = 1


if pdfloc:

    for pos in pdfloc:
        pag.click(pos)
        pag.press('enter')
        pag.moveTo(620,265)
        pag.tripleClick()
        pag.rightClick()
        pag.moveTo(671,354)
        pag.click()
        pag.click(winexploc)
        pag.press('f2')
        pag.hotkey('ctrl','v')
        pag.press('enter')
        time.sleep(4)

pag.click(msedgeloc)
pdfielist = list(pdfieloc)
pag.moveTo(pdfielist[0])
pag.click(button='middle', clicks=len(pdfielist))






