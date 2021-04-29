import mysql.connector as connector

class PlasmaCenter:
    def __init__(self):
        self.con = connector.connect(host='localhost', port='3306', user='root', password='root', database='covidrelief', auth_plugin='mysql_native_password')

        query='create table if not exists plasmacenter(center VARCHAR(50) PRIMARY KEY, bloodgroups VARCHAR(50), FOREIGN KEY(center) REFERENCES centers(center) ON DELETE CASCADE)'
        self.cur=self.con.cursor()
        self.cur.execute(query)

    def insert_tests(self, center, bloodgroups):
        query= "INSERT INTO plasmacenter values('{}', '{}')".format(center, bloodgroups)
        self.cur.execute(query)
        self.con.commit()
        
    def update_tests(self, center, bloodgroups):
        query= "Update plasmacenter SET bloodgroups='{}' WHERE center='{}'".format(bloodgroups, center)
        self.cur.execute(query)
        self.con.commit()


# pc = PlasmaCenter()
# pc.update_tests("Morya Blood bank", "A, B, O, AB, -A")