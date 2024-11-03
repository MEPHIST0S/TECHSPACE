import pymysql

#CONNECTING TO DB MYSQL
connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '4444',
    database = 'AUTHOR',
    port = 3307,
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

def create_blog_table():
    with connection.cursor() as cursor:
        sql = """
        CREATE TABLE IF NOT EXISTS BLOGS (
            id INT PRIMARY KEY,
            title VARCHAR(255),
            author_name VARCHAR(100)
        );
        """
        cursor.execute(sql)
    connection.commit()

#TABLE CREATION
create_blog_table()

#GETTING DATA FROM TXT
filename = "blogs.txt"

with open(filename, "r") as file:
    data = file.read().strip()
    
entries = data.split("-------------------------")

#INSERTING FUNCTION
def insert_blog(id, title, author_name):
    with connection.cursor() as cursor:
        sql = """
        INSERT INTO BLOGS (id, title, author_name)
        VALUES (%s, %s, %s)
        """
        cursor.execute(sql, (id, title, author_name))
    connection.commit()

#INSERTING AFTER RETRIVIENG AND ASSIGNMENT
for entry in entries:
    lines = entry.strip().split("\n")
    if len(lines) == 3:  #CHECKING
        id_line = lines[0].strip().split(":")
        title_line = lines[1].strip().split(":")
        author_name_line = lines[2].strip().split(":")
        
        id = int(id_line[1].strip())
        title = title_line[1].strip()
        author_name = author_name_line[1].strip()
        
        insert_blog(id, title, author_name)

#CONNECTION CLOSING
connection.close()