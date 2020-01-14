'''
定义一个连接MySQL数据库，用来操作数据库，增删改查
'''
import pymysql

class Mysql():

    def __init__(self,ip,username,password,table_name,port=3306):
        self.ip=ip
        self.username=username
        self.password=password
        self.table_name=table_name
        self.port=port
        self.db=pymysql.connect(self.ip,self.username,self.password,self.table_name)

    def select(self,select_table,select_where,select_return="*"):
        '''

        :param select_table: 查询的表名
        :param select_where: 查询的条件
        :param select_return: 需要返回的数据
        :return: 返回字典格式的查询结果
        '''
        # 使用cursor()方法创建一个游标对象
        cursor=self.db.cursor()
        #根据传入的参数，拼接sql语句
        sql="select"+select_return+"from"+select_table+"where"+select_where
        #使用fetall()获取全部数据
        data=cursor(sql)
        # 关闭游标
        cursor.close()
        #返回查询到的数据
        return data



#连接数据库
db=pymysql.connect("localhost","root","root","test")
#使用cursor()方法创建一个游标对象
cursor=db.cursor()
#使用execute()方法执行SQL语句
cursor.execute("select * from interface_case ")
#使用fetall()获取全部数据
data=cursor.fetchall()
#打印获取到的数据
print(data)
print(type(data))
#关闭游标和数据库的连接
cursor.close()
db.close()