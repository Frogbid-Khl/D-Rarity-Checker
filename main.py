import json
import xlsxwriter
import pandas as pd

def search(array, n, x):
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1

in_file_path = 'input/_metadata.json'

col_name = []
row_name=[]
value_updated=[]
json_object = []

j = 1
with open(in_file_path, 'r') as in_json_file:
    json_obj_list = json.load(in_json_file)

    for json_obj in json_obj_list:
        for json_o in json_obj['attributes']:
            n = len(col_name)
            result = search(col_name, n, json_o['trait_type'])
            if (result == -1):
                col_name.append(json_o['trait_type'])
                col_name.append('Total')

            n = len(row_name)

            result = search(row_name, n, [json_o['trait_type'],json_o['value']])
            if (result == -1):
                row_name.append([json_o['trait_type'],json_o['value']])
                value_updated.append(1)
                print([json_o['trait_type'], json_o['value'], value_updated[result],'new'])
            else:
                print('old:'+str(value_updated[result]))
                up=value_updated[result]+1
                value_updated.insert(result, up)
                print([json_o['trait_type'], json_o['value'], value_updated[result],'index: '+str(result),'old'])
                print('new:'+str(value_updated[result]))




workbook = xlsxwriter.Workbook('output/rarity.xlsx')
worksheet = workbook.add_worksheet()
row = 0
column = 0

for x in range(len(col_name)):
    row = 0
    worksheet.write(row, column, col_name[x])
    row+= 1
    for y in range(len(row_name)):
        if row_name[y][0]==col_name[x]:
            worksheet.write(row, column, row_name[y][1])
            worksheet.write(row, column+1, value_updated[y])
            row+=1

    column+=1


workbook.close()

df = pd.read_excel('output/rarity.xlsx')

print(df)

print(len(col_name)/2)

print(col_name)
#i=0
#for item in row_name:
    #print(str(item)+' ['+str(value[i])+']')
    #i+=1

print(value_updated)