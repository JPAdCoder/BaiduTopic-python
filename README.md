## BaiduTopic-python [GitLab](https://github.com/JPAdCoder/BaiduTopic-python) [GitHub](http://adcoder.club:10080/AdCoder/baidutopic-python)

>* ###说明
#### &nbsp;&nbsp;&nbsp;&nbsp;使用python抓取百度搜索风云榜Top50的话题内容以及搜索数量，每十分钟抓取一次

>* ### 依赖  
 * #### Python 3.x <https://www.python.org/>  
 * #### Requests <https://github.com/psf/requests/>  
 * #### BeautifulSoup4 <https://www.crummy.com/software/BeautifulSoup/>  
 * #### Pymysql <https://github.com/PyMySQL/PyMySQL>  
 * #### loguru <https://github.com/Delgan/loguru>  
   
>* ### 数据库  
#### &nbsp;&nbsp; Mysql 5.7 <https://www.mysql.com/>  
  
>* ### 运行方法  
#### 1. &nbsp;&nbsp;&nbsp;&nbsp;修改spider.py文件中pymysql.connect()中的参数，改为自己库的参数。  
#### 2. &nbsp;&nbsp;&nbsp;&nbsp;修改spider.sql在开头加上use 你的数据库;  
#### 3. &nbsp;&nbsp;&nbsp;&nbsp;执行spider.sql创建需要的表  
#### 4. &nbsp;&nbsp;&nbsp;&nbsp;切换到项目根目录在terminal或者cmd执行python spider.py
