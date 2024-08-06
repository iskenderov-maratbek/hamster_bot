# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

# cards={}
# def connectDatabase():
#     global cards;
#     gc = gspread.service_account(filename='C:\\Users\\King\\Documents\\GitHub\\hamster_bot\\credentials.json')
#     # Подключение к Google Таблице

#     # Открытие таблицы по имени
#     sheet = gc.open('HAMSTER').sheet1

#     # Чтение данных
#     headers = sheet.get_all_values(range_name='A2:H100', major_dimension='COLUMNS')
#     # print(headers)
#     for i in headers:
#         if(i!=''):
#             for j in range(len(i)):
#                 if(j==0):
#                     cards[i[j]]=[]
#                 else:
#                     if(i[j]!=''):
#                             temp = [i[j].split()]
#                             temp.append(0)
#                             cards[i[0]].append(temp)



import pickle
cardsView = {}
cards={};

def openCards():
    global cardsView,cards
    with open('data.pkl', 'rb') as f:
        result = pickle.load(f)
        resultTransform=result
        for i in resultTransform.keys():
            cards.update({i:[]})
            for j in range(len(resultTransform[i])):
                cards[i].append([resultTransform[i][j].split(),0])
        print('\n\n')
        cardsView.update(result)


def updateCards(loaded_data):
      with open('data.pkl', 'wb') as f:
        pickle.dump(loaded_data, f)

def printCards():
    global cards
    for i in cards:
        print(i,cards[i])
        print('\n\n')
    # for i in data:        
    #     if(i.value!=''):
    # headers = sheet.get_all_records(expected_headers=['Markers', 'PR&Team', 'Legal', 'Specials'])
    # temp_headers = [i for i in headers if i]
    # print(headers)
    # headers = {i:[] for i in headers if i}
    # print(headers)
    # data = sheet.get_all_records(1)
    # print(data)
    # for i in data:
    #     if(i.value!=''):
            
    #         if (i.col%2==0):
    #             index = int(i.col/2)
    #             headers[temp_headers[index]].append(i.value)
    #         else:
    #             index = int(i.col//2)
    #             print(index)
    #             headers[temp_headers[index]].append(i.value)
                
    # headers = data.pop(0)
    # print(headers)
