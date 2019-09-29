import pymysql
import time
import requests
import datetime
from loguru import logger
from bs4 import BeautifulSoup

db = pymysql.connect(
    host='host',
    user='username',
    password='passwd',
    database='dbname',
    port='port'
)

cursor = db.cursor()


def query_by_topic_name(topic_name):
    sql = "select * from topic where topic_name = '%s' " % topic_name
    cursor.execute(sql)
    return cursor.fetchone()


def insert_topic(topic_name, count):
    sql = "insert into topic (topic_name, count) value ('%s', %d) " % (topic_name, count)
    cursor.execute(sql)
    db.commit()


def update_topic(topic_name, count):
    sql = "update topic set count=%d, update_datetime='%s' where topic_name = '%s' " % \
          (count, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), topic_name)
    cursor.execute(sql)
    db.commit()


while True:
    logger.add("logs/topic_log", rotation="3 days", enqueue=True)
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
    logger.info("新增话题：%d;更新话题：%d" % (insert_count, update_count))
    time.sleep(600)
