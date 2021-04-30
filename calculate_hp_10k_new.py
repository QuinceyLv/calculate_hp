# -*- encoding: utf-8 -*-
'''
@Time    :   2020/11/21 21:12:26
@Author  :   Quincey Lyu
'''

import os


def CalculateHp(Amaj, Amin):
    if Amaj + Amin == 0:
        return '0'
    else:
        hp = (2 * Amaj * Amin) / ((Amaj + Amin) ** 2)
        return str(hp)


def colSum(listA: list, listB: list):
    listA = [int(i) for i in listA]
    listB = [int(i) for i in listB]
    listSum = []
    for j in range(0, len(listA)):
        listSum.append(listA[j] + listB[j])
    return listSum


os.chdir('d:/workspace')
fo = open('anser_hp_result_201112_2.txt', 'w')
# fo2 = open('windows.txt', 'w')
regions = []
fi2 = open('temp/anser_hp_data_sorted.txt', 'r')
temp = [0, 0, 0, 0, 0, 0]
i = 0
read = True

with open('temp/A-B-10k.sorted.Sfst') as fi1:
    for lines in fi1:
        line = lines.rstrip().split('\t')
        regions.append(line)

while True:
    if read is True:
        lines = fi2.readline()
    # print(regions[i][0:3], file=fo2)
    if not lines:   # 位点读完，结算跳出
        regions[i].insert(5, CalculateHp(temp[4], temp[5]))
        regions[i].insert(5, CalculateHp(temp[2], temp[3]))
        regions[i].insert(5, CalculateHp(temp[0], temp[1]))
        break
    else:
        line = lines.rstrip().split('\t')
        if line[0] == regions[i][0] and (int(line[1]) >= int(regions[i][1])) and (int(line[1]) <= int(regions[i][2])):  # 落在窗口内
            temp = colSum(temp, line[3:9])
            read = True
        else:   # 没有落在窗口内，不继续读取位点，往下个窗口中放
            regions[i].insert(5, CalculateHp(temp[4], temp[5]))
            regions[i].insert(5, CalculateHp(temp[2], temp[3]))
            regions[i].insert(5, CalculateHp(temp[0], temp[1]))
            temp = [0, 0, 0, 0, 0, 0]
            if i + 1 < len(regions):
                i += 1
                read = False
            else:   # 窗口读完，结算跳出
                regions[i].insert(5, CalculateHp(temp[4], temp[5]))
                regions[i].insert(5, CalculateHp(temp[2], temp[3]))
                regions[i].insert(5, CalculateHp(temp[0], temp[1]))
                break

fi2.close()

for ele in regions:
    print('\t'.join(ele), file=fo)

fo.close()
