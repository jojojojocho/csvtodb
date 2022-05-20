import scipy.io
import csv
import pymysql
import re

if __name__ == '__main__':
    conn = pymysql.connect(host='127.0.0.1', user='root', password='12345',

                           db='datingjpa', charset='utf8')

    # conn = pymysql.connect(host='springboot-jpadating.cporkyk21dry.ap-northeast-2.rds.amazonaws.com', user='root', password='12345678',
    #
    #                         db='datingjpa', charset='utf8')

    curs = conn.cursor()

    conn.commit()

    f = open('C:/p_data/sajudatingjpa/사주_일주.csv', 'r')

    csvReader = csv.reader(f)

    id = 0


    for row in csvReader:
        if (id == 0):
            id += 1
            continue;

        year = row[0]
        lunar_year = (row[1])
        year_words = (row[2])
        month = row[3]
        lunar_month = row[4]
        month_words = row[5]
        day = row[6]
        lunar_day = row[7]
        day_words = row[8]
        month_compare = row[9]
        sql = """insert into saju_calender (id, year, lunar_year, year_words, month, lunar_month, month_words, day, 
        lunar_day, day_words, month_compare ) values ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )"""

        id += 1
        curs.execute(sql,
                     (id, year, lunar_year, year_words, month, lunar_month, month_words, day, lunar_day, day_words,
                      month_compare))

    conn.commit()
    conn.close()
    f.close()
