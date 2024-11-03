import pymysql

#CONNECTING TO DB MYSQL
connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '4444',
    database = 'TASKS',
    port = 3307,
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

#CREATION HOSPITAL TABLE
def create_hospital():
    with connection.cursor() as cursor:
        sql = """
         CREATE TABLE IF NOT EXISTS TASKS.HOSPITAL(
            ID INT AUTO_INCREMENT PRIMARY KEY,
            NAME VARCHAR(100),
            BED_COUNT INT
        );
        """
        cursor.execute(sql)
    connection.commit()
    
# CREATION DOCTOR TABLE
def create_doctor():
    with connection.cursor() as cursor:
        sql = """
        CREATE TABLE IF NOT EXISTS TASKS.DOCTOR(
            ID INT AUTO_INCREMENT PRIMARY KEY,
            NAME VARCHAR(100),
            HOSPITAL_ID INT,
            JOINING_DATE DATE,
            SPECIALITY VARCHAR(255),
            SALARY INT,
            EXPERIENCE INT,
            FOREIGN KEY (HOSPITAL_ID) REFERENCES HOSPITAL(ID)
        );
        """
        cursor.execute(sql)

#CREATION FUNCTIONS
create_hospital()
create_doctor()
#COMMIT
connection.commit()
    
#INSERTING DATA TO TABLE HOSPITAL
def add_hospital(NAME, BED_COUNT):
    with connection.cursor() as cursor:
        sql = """
        INSERT INTO HOSPITAL (NAME, BED_COUNT)
        VALUES (%s, %s)
        """
        cursor.execute(sql, (NAME, BED_COUNT))

#INSERTING DATA TO TABLE DOCTOR
def add_doctors(NAME, HOSPITAL_ID, JOINING_DATE, SPECIALITY, SALARY):
    with connection.cursor() as cursor:
        sql = """
        INSERT INTO DOCTOR (NAME, HOSPITAL_ID, JOINING_DATE, SPECIALITY, SALARY)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (NAME, HOSPITAL_ID, JOINING_DATE, SPECIALITY, SALARY))
        
# #INSERTING HOSPITALS        
# add_hospital("City Hospital", 200)
# add_hospital("Greenwood Clinic", 150)
# add_hospital("Sunshine Medical Center", 300)
# add_hospital("Starlight Hospital", 250)
# add_hospital("Riverdale Hospital", 180)
# #COMMIT
# connection.commit()

# #INSERTING DOCTORS
# add_doctors("Dr. Smith", 1, "2023-01-15", "Cardiologist", 120000)
# add_doctors("Dr. Johnson", 2, "2022-05-22", "Neurologist", 115000)
# add_doctors("Dr. Williams", 3, "2023-03-12", "Orthopedic Surgeon", 130000)
# add_doctors("Dr. Brown", 4, "2021-07-30", "Pediatrician", 110000)
# add_doctors("Dr. Jones", 5, "2022-09-25", "Dermatologist", 125000)
# add_doctors("Dr. Garcia", 1, "2023-02-05", "Oncologist", 140000)
# add_doctors("Dr. Martinez", 2, "2021-11-20", "Rheumatologist", 100000)
# add_doctors("Dr. Rodriguez", 3, "2023-04-18", "Pulmonologist", 105000)
# add_doctors("Dr. Wilson", 4, "2022-12-10", "Gastroenterologist", 120000)
# add_doctors("Dr. Anderson", 5, "2023-06-28", "Endocrinologist", 125000)
# #COMMIT
# connection.commit()

# GET HOSPITAL DATA BY ID
def get_hospital_by_id(hospital_id):
    with connection.cursor() as cursor:
        sql = """
        SELECT * FROM TASKS.HOSPITAL
        WHERE ID = %s;
        """
        cursor.execute(sql, (hospital_id,))
        result = cursor.fetchone()
        return result

# GET DOCTOR DATA BY ID
def get_doctor_by_id(doctor_id):
    with connection.cursor() as cursor:
        sql = """
        SELECT * FROM TASKS.DOCTOR
        WHERE ID = %s;
        """
        cursor.execute(sql, (doctor_id,))
        result = cursor.fetchone()
        return result

# #ID ASSIGNMENT
# hospital_id = 1
# doctor_id = 2

# #DISPLAY HOSPITAL BY ID
# hospital_data = get_hospital_by_id(hospital_id)
# print("Hospital Data:", hospital_data)

# #DISPLAY DOCTOR BY ID
# doctor_data = get_doctor_by_id(doctor_id)
# print("Doctor Data:", doctor_data)

#FILTERING DOCTORS BY SPECIALITY AND SALARY
def filter_doctors(speciality, salary):
    with connection.cursor() as cursor:
        sql = """
        SELECT * FROM TASKS.DOCTOR
        WHERE SPECIALITY = %s AND SALARY >= %s;
        """
        cursor.execute(sql,(speciality, salary))
        result = cursor.fetchall()
        return result
        
# #FILTER ASSIGNMENT
# spec = "Neurologist"
# sal = 100000

# #FILTERING
# doctor_filter = filter_doctors(spec, sal)
# print("Filtered", doctor_filter)

#DISPLAY DOCTOR BY HOSPITAL
def get_doc_by_hospital(hospital_id):
    with connection.cursor() as cursor:
        sql = """
        SELECT D.NAME, H.NAME 
        FROM DOCTOR AS D
        JOIN HOSPITAL AS H 
        ON D.HOSPITAL_ID = H.ID
        WHERE HOSPITAL_ID = %s;
        """
        cursor.execute(sql, (hospital_id,))
        result = cursor.fetchall()
        return result
    
# #ASSIGN HOSPITAL BY ID
# hospital_id = 2

# #DISPLAY DOCTOR BY HOSPITAL_ID
# doctor_by_hospital_id = get_doc_by_hospital(hospital_id)
# print("Doctors: ", doctor_by_hospital_id)

#UPDATE EXPERIENCE
def update_experience():
    with connection.cursor() as cursor:
        sql = """
        UPDATE DOCTOR
        SET EXPERIENCE = TIMESTAMPDIFF(YEAR, JOINING_DATE, CURDATE());
        """
        cursor.execute(sql)
    connection.commit()

# #UPDATE FUNCTION
# update_experience()

#CONNECTION CLOSING
connection.close()