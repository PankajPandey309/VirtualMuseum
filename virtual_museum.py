import sqlite3
from PIL import Image
from numpy import array

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        
        return conn
    except Error as e:
        print(e)
 
    return None
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_buildings(conn, building):
    """
    Create a new building
    :param conn:
    :param building:
    :return:
    """
 
    sql = ''' INSERT INTO buildings(id,name,info,pic,pic_id)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, building)
    return cur.lastrowid

def create_faculty(conn, fac):
    """
    Create a new faculty
    :param conn:
    :param fac:
    :return:
    """
 
    sql = ''' INSERT INTO faculty(id,name,branch,pic,pic_id)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, fac)
    return cur.lastrowid

def create_events(conn, event):
    """
    Create a new event
    :param conn:
    :param event:
    :return:
    """
 
    sql = ''' INSERT INTO events(e_id,name,description,s_head,f_head,pic,pic_id)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, event)
    return cur.lastrowid

def create_commitees(conn,commitee):
    """
    Create a new commitee
    :param conn:
    :param commitee:
    :return:
    """
 
    sql = ''' INSERT INTO commitees(c_id,name,s_head,f_head,descrition,pic,pic_id)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, commitee)
    return cur.lastrowid

def main():
    database = "C:\\sqlite\db\pythonsqlite.db"
 
    sql_create_buildings_table= """ CREATE TABLE IF NOT EXISTS buildings (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        info text,
                                        pic BLOB,
                                        pic_id integer  UNIQUE
                                    ); """
 
    sql_create_arts_table = """CREATE TABLE IF NOT EXISTS arts (
                                    pic_id integer  PRIMARY KEY,
                                    name text NOT NULL,
                                    artist text,
                                    descrition text NOT NULL,
                                    pic BLOB,
                                    FOREIGN KEY(pic_id) REFERENCES artists(artist_id)
                                );"""
    sql_create_commitees_table = """CREATE TABLE IF NOT EXISTS commitees (
                                    c_id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    s_head text,
                                    f_head text,
                                    descrition text NOT NULL,
                                    pic BLOB,
                                    pic_id integer  UNIQUE
                                );"""
    sql_create_events_table = """CREATE TABLE IF NOT EXISTS events (
                                    e_id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    s_head text,
                                    f_head text,
                                    description text NOT NULL,
                                    pic BLOB,
                                    pic_id integer ,
                                    c_id integer NOT NULL,
                                    FOREIGN KEY(pic_id) REFERENCES commitees(c_id)
                                );"""
      
    sql_create_artists_table = """CREATE TABLE IF NOT EXISTS artists (
                                    artist_id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    DOB text NOT NULL,
                                    comm text,
                                    FOREIGN KEY(comm) REFERENCES commitees(c_id)
                                );"""
   
    sql_create_Users_table= """ CREATE TABLE IF NOT EXISTS Users (
                                        Fullname text,
                                        Email text NOT NULL,
                                        Username text,
                                        Password Primary Key,
                                        Gender Text,
                                        country Text,
                                        PhoneNumber Text
                                    ); """
    sql_create_faculty_table= """ CREATE TABLE IF NOT EXISTS faculty (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        branch text,
                                        pic BLOB,
                                        pic_id integer  UNIQUE
                                    ); """
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create buildings table
        create_table(conn, sql_create_buildings_table)
        # create arts table
        create_table(conn, sql_create_arts_table)
        # create commitees table
        create_table(conn, sql_create_commitees_table)
        # create events table
        create_table(conn, sql_create_events_table)
        #create loginID table
        create_table(conn,sql_create_Users_table)
        #create faculty table
        create_table(conn,sql_create_faculty_table)
    else:
        print("Error! cannot create the database connection.")
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\buildings\AB1.jpg")
    #arr = array(img)
    #building_1 = (1001, 'AB-1','The academic block-1 ' ,arr,1001 )
    #create_buildings(conn, building_1)
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\buildings\ADMIN_BLOCK.jpg")
    #arr = array(img)
    #building_2 = (1002, 'Administration Block ','The Administration Block houses schools of Law and the administration office ' ,arr,1002 )
    #create_buildings(conn,building_2)
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\buildings\auditorium.jpg")
    #arr = array(img)
    #building_3 = (1003, 'Auditorium ','The Auditorium located on the seventh(7th) floor of the Academic-Block 1 is a setting where quizes, guest lectures  and other club events take place  ' ,arr,1003 )
    #create_buildings(conn, building_3)
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\buildings\GIRLS_HOSTEL.jpg")
    #arr = array(img)
    #building_4 = (1004, 'Girls Hostel ','The Girls Hostel is a dominant building consisting of fifteen floors with messes and canteens within  ' ,arr,1004 )
    #create_buildings(conn, building_4)
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\buildings\library.jpg")
    #arr = array(img)
    #building_5 = (1005, 'Library','The library is a fully centalized building and houses books on a vast array of subjects   ' ,arr,1005 )
    #create_buildings(conn, building_5)
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\buildings\maingate.jpg")
    #arr = array(img)
    #building_6 = (1006, 'Maingate','the maingate was built in the year 2010   ' ,arr,1006 )
    #create_buildings(conn, building_6)
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\buildings\A_block.jpg")
    #arr = array(img)
    #building_7 = (1007, 'Mens Hostel A','The Mens Hostel A or A block accomodates students rom 2nd year to the 4th year  ' ,arr,1007 )
    #create_buildings(conn, building_7)
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\buildings\room.jpg")
    #arr = array(img)
    #building_8 = (1008, 'Hostel Room','The rooms are available in both AC and non AC  ' ,arr,1008 )
    #create_buildings(conn, building_8)
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\buildings\gym.png")
    #arr = array(img)
    #building_9 = (1009, 'Gym','The Gyms come with fully stocked  equipment and a trainer  ' ,arr,1009 )
    #create_buildings(conn, building_9)
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\buildings\mess.jpg")
    #arr = array(img)
    #building_10 = (1010, 'Mess','The mess are divided into special, north and south mess and serve the respected cuisines  ' ,arr,1010 )
    #create_buildings(conn, building_10)
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\buildings\classroom.png")
    #arr = array(img)
    #building_11 = (1011, 'Classroom','The classrooms are spacious , comfortable and give a good vibe  ' ,arr,1011 )
    #create_buildings(conn, building_11)
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\buildings\monument.png")
    #arr = array(img)
    #building_12 = (1012, 'The monument','The monument was built in 2010  ' ,arr,1012 )
    #create_buildings(conn, building_12)
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\buildings\basket.jpg")
    #arr = array(img)
    #building_13 = (1013, 'The basketball Court','The Basket Ball  court is built keeping in mind the measurements of a professional sport court ' ,arr,1013 )
    #create_buildings(conn, building_13)


        
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\events\designu.jpg")
    #arr = array(img)
    #event_1 = (2001, 'DISENO','It explores the various talents in the field of mechanical engineering   ','Abishek Deswal','Prof. Gobinathan',arr,2001 )
    #create_events(conn, event_1)
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\events\foosball.jpg")
    #arr = array(img)
    #event_2 = (2002, 'Human Foosball','The event consists of a human version of thepopular game foosball  ','Anshul Raj','Prof. Balamurgan' ,arr,2002 )
    #create_events(conn, event_2)
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\events\motormash.jpg")
    #arr = array(img)
    #event_3 = (2003, 'Motor mash','The event displayed the skills of bikes','Nishant','Prof. ABC',arr,2003 )
    #create_events(conn, event_3)
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\events\parle-ji.jpg")
    #arr = array(img)
    #event_4 = (2004, 'Parle-G','It was a eating contest with parle-g the only  item on the menu','Abishek Deswal','Prof. Gobinathan' ,arr,2004 )
    #ascreate_events(conn, event_4)
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\events\passtheballon.jpg")
    #arr = array(img)
    #event_5 = (2005, 'Pass The Balloon','It was an entertainment event' ,'Abishek Deswal','Prof. Gobinathan',arr,2005 )
    #create_events(conn, event_5)
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\events\pithu.jpg")
    #arr = array(img)
    #event_6 = (2006, 'Pithu','It is a fun filled activity that filled all participants with nostalgia' ,'Abishek Deswal','Prof. Gobinathan',arr,2006 )
    #create_events(conn, event_6)
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\events\DOTA.jpg")
    #arr = array(img)
    #event_7 = (2007, 'DOTA','It is a multiplayer gaming event hosted by QUBIT' ,'Aditya Das','Prof. Prassanna',arr,2007 )
    #create_events(conn, event_7)
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\events\lasertag.jpg")
    #arr = array(img)
    #event_8 = (2008, 'Lasertag','THe lasertag event hosted by Qubit is available to all ages and is a must attend' ,'Aditya Das','Prof. Prassanna',arr,2008 )
    #create_events(conn, event_8)
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\events\bikemadness.jpg")
    #arr = array(img)
    #event_9 = (2009, 'Bikemadness','Itis a display of bike riding skills' ,'Nishant','Prof. Christo MIcheal',arr,2009 )
    #create_events(conn, event_9)
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\events\navratri.jpg")
    #arr = array(img)
    #event_10 = (2010, 'Navratri','Navratri is celebrited in VIT in various forms' ,'Aranya Roy','Prof. XYZ',arr,2010 )
    #create_events(conn, event_10)
    


    
    #arr = array(img)
    #commitee_1 = (3001, 'Connectivity' ,'Satakshi Sinha','Prof. Umayal C.','Its the combined committee of the schools, SELECT and SENSE',arr,3001 )
    #create_commitees(conn,commitee_1)
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\commitees\disenogp.jpg")
    #arr = array(img)
    #commitee_2 = (3002, 'Diseno' ,'Abishek Deswal','Prof. Gopinathan','It explores the various talents in the field of mechanical engineering',arr,3002 )
    #create_commitees(conn,commitee_2)
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\commitees\Shaurya.png")
    #arr = array(img)
    #commitee_3 = (3003, 'Shauya' ,'Tejas Khot','Prof. Arun Kumar Sharma ','The group aims at creating a formula car from scratch every year',arr,3003 )
    #create_commitees(conn,commitee_3)
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\commitees\qubit.jpg")
    #arr = array(img)
    #commitee_4 = (3004, 'Qubit' ,'Aditya Das','Prof. ShubbuLakshmi T ','The group focuses on events and workshops related to the branch of computer science',arr,3004 )
    #create_commitees(conn,commitee_4)
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\commitees\zuura.jpg")
    #arr = array(img)
    #commitee_5 = (3005, 'Zuura' ,'Ritwik Tripathi','Prof. Christo Michael','The Zuura formula racing club designs and competes in racing car events in India as well as abroad',arr,3005 )
    #create_commitees(conn,commitee_5)
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\commitees\enactus.jpg")
    #arr = array(img)
    #commitee_9 = (3009, 'Enactus' ,'Nishant Singh','Prof. Jaganathan','The Enactus does voluntary social work helping the  differentially abled and refugees ',arr,3009 )
    #create_commitees(conn,commitee_9)
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\commitees\music.jpg")
    #arr = array(img)
    #commitee_7 = (3007, 'Music' ,'Sudhanshu Sharma','Prof. Tanushree Chowdhary','The Music club nurtures a wide array of talents in music and frequently entertains with their performances ',arr,3007 )
    #create_commitees(conn,commitee_7)
    #img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\commitees\SAE.jpg")
    #arr = array(img)
    #commitee_8 = (3008, 'SAE' ,'Abu Bakt Azam','Prof. Daimanathan','Itis a automobile club ',arr,3008 )
    #create_commitees(conn,commitee_8)

    img = Image.open(r"C:\Users\PANKAJ\Desktop\DBMS\virtual_museum\pics\buildings\c.png")
    arr = array(img)
    fac_1 = (1001, 'Dr. G. Viswanathan','Chancellor ' ,arr,1001 )
    create_faculty(conn, fac_1)

   
    
    conn.commit()
    
   

if __name__ == '__main__':
    main()

    
