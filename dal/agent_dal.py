import mysql.connector

from model.status import Status


class Dal:
    def __init__(self):
        self.mydb = mysql.connector.connect(host="127.0.0.1",user="root",password="",database="eagleeyedb")
        self.mycursor =self.mydb.cursor()

    def insert(self,id,codeName, realName, location, missionsCompleted, status:Status):

        sql = f"INSERT INTO `agents`(`id`, `codeName`, `realName`, `location`, `missionsCompleted`, `status`) VALUES ('{id}','{codeName}','{realName}','{location}','{missionsCompleted}','{status}')"

        self.mycursor.execute(sql)
        self.mydb.commit()

    def select(self,coloom1):
        sql=f"SELECT ({coloom1}) FROM `agents`"
        self.mycursor.execute(sql)
        myresult = self.mycursor.fetchall()
        for x in myresult:
            print(x)

    def update(self,coloom,whom,in_whom):
        sql = f"UPDATE `agents` SET {coloom} = '{in_whom}' WHERE {coloom} = '{whom}'"

        self.mycursor.execute(sql)
        self.mydb.commit()

    def delete(self,id):

        sql = f"DELETE FROM `agents` WHERE `id`={id}"

        self.mycursor.execute(sql)
        self.mydb.commit()


start_dal= Dal()
start_dal.insert(12,"eee","bar","car",4,"Acti")
# start_dal.select('realName')
# start_dal.update("realName","rt","eli")
# start_dal.delete(1)