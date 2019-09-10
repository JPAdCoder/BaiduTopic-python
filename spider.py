import pymysql
import time
import requests
import datetime
from bs4 import BeautifulSoup

db = pymysql.connect(
    host='localhost',
    user='root',
    password='96241158aB!0',
    database='topic'
)

cursor = db.cursor()


def query_by_topic_name(topic_name):
    sql = "select * from topic where topic_name = '%s' " % topic_name
    cursor.execute(sql)
    return cursor.fetchone()


def insert_topic(topic_name, count):
    sql = "insert into topic (topic_name, count) value ('%s', %d) " % (topic_name, count)
    cursor.execute(sql)
    print("Insert %s " % sql)
    db.commit()


def update_topic(topic_name, count):
    sql = "update topic set count=%d, update_datetime='%s' where topic_name = '%s' " % \
          (count, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), topic_name)
    cursor.execute(sql)
    print("Update %s " % sql)
    db.commit()


while True:
    response = requests.get('http://top.baidu.com/buzz?b=1&fr=topindex')
    response.encoding = 'gbk'
    soup = BeautifulSoup(response.text, 'html.parser')
    keyword_list = []
    count_list = []
    for item in soup.find_all(class_='keyword'):
        keyword_list.append(item.a.get_text())

    for item in soup.find_all(class_='last')[2:]:
        count_list.append(int(item.span.get_text()))
    zipped = zip(keyword_list, count_list)

    for item in zipped:
        if query_by_topic_name(item[0]) is not None:
            update_topic(item[0], item[1])
        else:
            insert_topic(item[0], item[1])
    print("Sleep 600 Seconds")
    time.sleep(600)
