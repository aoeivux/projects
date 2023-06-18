#将django的默认的数据库引擎修改为pymysql
#原因是django默认的数据库引擎mysqlclient 只支持python2 不支持python3
import pymysql
pymysql.version_info=(1,4,3,"final",0)
pymysql.install_as_MySQLdb()