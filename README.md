## BaiduTopic-python [GitLab](http://adcoder.club:10080/AdCoder/baidutopic-python) [GitHub](https://github.com/JPAdCoder/BaiduTopic-python)

## 1.说明  
>* 使用python抓取百度搜索风云榜Top50的话题内容以及搜索数量，每十分钟抓取一次

## 2.依赖  
>* Python 3.x <https://www.python.org/>  
> * Requests <https://github.com/psf/requests/>  
> * BeautifulSoup4 <https://www.crummy.com/software/BeautifulSoup/>  
> * Pymysql <https://github.com/PyMySQL/PyMySQL>  
> * loguru <https://github.com/Delgan/loguru>  
   
## 3.数据库  
>  * Mysql 5.7 <https://www.mysql.com/>  
  
## 4.运行方法  
> 1. 修改spider.py文件中pymysql.connect()中的参数，改为自己库的参数。  
> 2. 修改spider.sql在开头加上use 你的数据库;  
> 3. 执行spider.sql创建需要的表  
> 4. 切换到项目根目录在terminal或者cmd执行python spider.py
