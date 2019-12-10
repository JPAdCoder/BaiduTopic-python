import datetime
import time
import pymysql
import requests
from bs4 import BeautifulSoup


def get_conn():
    return pymysql.connect(
        host='host',
        user='username',
        password='passwd',
        database='dbname',
        port='port'
    )


def query_by_topic_name(topic_name):
    db = get_conn()
    cursor = db.cursor()
    sql = "select * from topic where topic_name = '%s' " % topic_name
    cursor.execute(sql)
    cursor.close()
    db.close()
    return cursor.fetchone()


def insert_topic(topic_name, count):
    db = get_conn()
    cursor = db.cursor()
    sql = "insert into topic (topic_name, count) value ('%s', %d) " % (topic_name, count)
    cursor.execute(sql)
    cursor.close()
    db.close()
    db.commit()


def update_topic(topic_name, count):
    db = get_conn()
    cursor = db.cursor()
    sql = "update topic set count=%d, update_datetime='%s' where topic_name = '%s' " % \
          (count, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), topic_name)
    cursor.execute(sql)
    cursor.close()
    db.close()
    db.commit()


while True:
    response = requests.get('http://top.baidu.com/buzz?b=1&fr=topindex')
    response.encoding = 'gbk'
    soup = BeautifulSoup(response.text, 'html.parser')
    keyword_list = []
    count_list = []
    insert_count = 0
    update_count = 0
    for item in soup.find_all(class_='keyword'):
        keyword_list.append(item.a.get_text())

    for item in soup.find_all(class_='last')[2:]:
        count_list.append(int(item.span.get_text()))
    zipped = zip(keyword_list, count_list)

    for item in zipped:
        if query_by_topic_name(item[0]) is not None:
            update_topic(item[0], item[1])
            update_count += 1
        else:
            insert_topic(item[0], item[1])
            insert_count += 1
    print("新增话题：%d;更新话题：%d" % (insert_count, update_count))
    time.sleep(600)
