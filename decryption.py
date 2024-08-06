import os
import re
from database import cardsView

def getPrice(vtext,relustCards,left=False):
   delsymbols = ['@', '€','tokens','hour','per','pairs','Profit']
   vtext = [i for i in vtext if i not in delsymbols]
   print(vtext)
   profit_and_price = []
#    print('START CARDS')
#    print(relustCards)
#    print('\n\n')
   endDown=False
   skip=False
   for i in range(len(vtext)):
       if (len(vtext[i])>1):
          if (not skip):
            if (re.search(r'\d+[KM]$', vtext[i],re.IGNORECASE)):
                vtext[i]=vtext[i].lower()
                if ('k' in vtext[i]):
                    vtext[i]=vtext[i].replace('k','')
                    try:
                        profit_and_price.append([float(vtext[i])*1000,i])
                    except ValueError:
                        pass
                elif ('m' in vtext[i]):
                    vtext[i]=vtext[i].replace('m','')
                    try:
                        profit_and_price.append([float(vtext[i])*1000000,i])
                    except ValueError:
                        pass
            elif (re.search(r'\d', vtext[i],re.IGNORECASE)):
                try:
                    if (float(vtext[i])>9):
                        profit_and_price.append([float(vtext[i]),i])
                except ValueError:
                    pass
            elif (vtext[i] in 'lvl'):
                skip=True
            else:
                pass
          else:
           skip=False    
       for j in relustCards.keys():
          if (left):
            if(not ('Specials' in j or j[-1]=='L')):
                continue
          else:
            if(not ('Specials' in j or j[-1]=='R')):
                 continue
          for k in range(len(relustCards[j])):
            for m in range(len(relustCards[j][k][0])):
                if (len(relustCards[j][k][0])>1):
                    if (vtext[i].lower() in relustCards[j][k][0][m].lower() or relustCards[j][k][0][m].lower() in vtext[i].lower()):
                        relustCards[j][k][0].pop(m)
                        relustCards[j][k][1]=i
                        endDown=True
                        break
                else:
                    if (vtext[i].lower() == relustCards[j][k][0][m].lower() or relustCards[j][k][0][m].lower() == vtext[i].lower()):
                        relustCards[j][k][0].pop(m)
                        relustCards[j][k][1]=i
                        endDown=True
                        break
            if (endDown):
                endDown=False
                break
#    if(left):
#        print('END OF LEFT PICTURE')
#    else:
#        print('END OF RIGHT PICTURE')
#    print('END CARDS')
   print(profit_and_price)
   return relustCards,profit_and_price


def detectCategory(localcards):
    statsDict={}
    detected=''
    for j in localcards.keys():
        statsDict[j[:-2]]=0
    for j in localcards.keys():
          for k in range(len(localcards[j])):
            if (len(localcards[j][k][0])==0):

                statsDict[j[:-2]]=statsDict[j[:-2]]+1

    maxValue=max(statsDict.values())     
    setDetect=False
    # print(statsDict)
    for p in statsDict.keys():
        if(statsDict[p]==maxValue):
            detected=p
            if(setDetect==False):
                setDetect=True
            else:
                return 'UNDETECTED'
    return detected   

def delTempFile(filename):
    if os.path.isfile(filename): 
        os.remove(filename) 
    else:
        print("Файл не найден")


def create_sample(category,leftCards,rightCards,leftPrice,rightPrice,leftCardSample,rightCardSample):
    leftResultCards = {leftCardSample[i][0]:[0,0] for i in range(len(leftCardSample)) if (len(leftCards[i][0])!=0)}
    rightResultCards = {rightCardSample[i][0]:[0,0] for i in range(len(rightResultCards)) if (len(rightCards[i][0])!=0)}
    rightResultCards = {j:[0,0] for j in rightCrightResultCardsardSample}
    # tempCards=[localCards[f'{category}_L'],localCards[f'{category}_R']]
    print('\n\n')
    # localCards = localCards[leftCategory]+localCards[rightCategory]
    # for i in range(len(localCards[leftCategory])):
    # print(f'LEFT CARDS: {leftCards}')
    # print(f'RIGHT CARDS: {rightCards}')
    # print(f'LEFT PRICE: {leftPrice}')
    # print(f'RIGHT PRICE: {rightPrice}')
    # newCards={}
    # print(leftResultCards)
    # print('\n\n')
    # print(leftCardSample)
    print(leftCards)
    for k in range(len(leftCards)):
        for l in range(len(leftPrice)):
            if (len(leftCards[k][0])==0 and leftCards[k][1]<leftPrice[l][1]):
                if(leftResultCards[leftCardSample[k]][1]==0 or leftPrice[l][1]<leftResultCards[leftCardSample[k]][1]):
                    leftResultCards[leftCardSample[k]][0]=leftPrice[l][0]
                    leftResultCards[leftCardSample[k]][1]=leftPrice[l][1]
    
    print(rightCards)
    for k in range(len(rightCards)):
        for l in range(len(rightPrice)):
            if (len(rightCards[k][0])==0 and rightCards[k][1]<rightPrice[l][1]):
                if(rightResultCards[rightCardSample[k]][1]==0 or rightPrice[l][1]<rightResultCards[rightCardSample[k]][1]):
                    rightResultCards[rightCardSample[k]][0]=rightPrice[l][0]
                    rightResultCards[rightCardSample[k]][1]=rightPrice[l][1]
    print('\n\n')
    # print(f'LEFT CARD SAMPLE: {leftCardSample} || {len(leftCardSample)}')
    # print(f'LEFT CARDS: {leftCards} || {len(leftCards)}')
    print(f'LEFT RESULT CARDS:  {leftResultCards}')
    # print(f'CARDVALUE: {cardValue}')
    # for i in range(len(cardValue)):
        # for j in range(len(price)):
            # if(len(localCards[i][0])==0 and localCards[i][1]<price[j][1]):

    # print(f'TEMPCARDS: {tempCards[0]}')
    # print(f'CARDVALUES: {cardValue}')
    # for i in range(len(tempCards[0])):
    #     if (len(tempCards[i][0])==0):
    #         print(f'DETECT CARD: {cardValue[i]}')
            # pass
        # print(localCards[category][i][1])