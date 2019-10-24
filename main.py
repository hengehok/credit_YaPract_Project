# -*- coding: utf8 -*-

import csv


from credit import Credit


if __name__ == "__main__":
    print('Что делаем? Считаем кредит(1) или Тестируем?(2)')
    choice = input()

    if choice == '1':
        print('Work with client datas')
        csv_path = "file1.csv"
        with open(csv_path) as csv_obj:
            reader = csv.DictReader(csv_obj, delimiter=',')

            for line in reader:
                print(line)
                credit = Credit(line)
                result = credit.processСlient()
                print('Result:',result)
            # print(credit.makeDesigion(line['age'],line['sex'],line['sourceIncome'], line['income'],line['rate'],line['expectedSum'],line['period'],line['goal']))
            # print(line['age'] +' - '+ line['sex'])
            # print (makeDesigion(66,'F','business',1000000,1,50000,2,'autocredit'))

    elif choice == '2':
        print('Test is running')
        csv_path = "testFile.csv"

        with open(csv_path) as csv_obj:
            reader = csv.DictReader(csv_obj, delimiter=',')
            for line in reader:
                #print(line)
                credit = Credit(line)
                result = credit.processСlient()

                #print(result)
                #print(line['expectedResult'])

                res = str(result)
                if res.find(line['expectedResult']) != -1:
                    print('PASS')
                else:
                    print('FAIL:', line['caseName'], '\n', line)




