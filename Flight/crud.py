import mysql.connector
try:
   conn = mysql.connector.connect(
      host='127.0.0.1',
      user='root',
      password='Deepanshu',
       database='indigo'
    )
   mycursor=conn.cursor()
   print("connection established")
except:
   print("connection error")
# mycursor.execute("Create Database indigo")
# conn.commit()
#
# mycursor.execute("""
# Create Table airpot(
#       airpod_id INTEGER Primary Key,
#       code varchar(50) NOT NULL,
#       city varchar(50) NOT NULL,
#       name varchar(255) NOT NULL
# )
# """)
# conn.commit()
# mycursor.execute("""
# INSERT INTO airpot VALUES
# (1,'Del','NewDelhi','IGIA'),
# (2,'CCU','KolKata','NSCA'),
# (3,'BOM','Mumbai','CSMA')
# """)
# conn.commit()
# mycursor.execute('Select * from airpot where airpod_id>1')
# data=mycursor.fetchall()
# print(data)
# for i in data:
#     print(i[3])
# mycursor.execute("""update airpot Set name='Bombay' where airpod_id=3""")
# conn.commit()
# mycursor.execute('Select * from airpot')
# data=mycursor.fetchall()
# print(data)
# mycursor.execute('Delete from airpot where airpod_id=3')
# conn.commit()
# mycursor.execute('Select * from airpot')
# data=mycursor.fetchall()
# print(data)