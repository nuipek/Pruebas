'''
Created on 14 nov. 2018

@author: saparicio
'''
import psycopg2

if __name__ == '__main__':
    
    user = "postgres"
    password = "Eurohelp"
    host = "127.0.0.1" # localhost
    port = "5432"
    dbname = "postgres"
    sslmode='verify-ca'
    sslrootcert="D:\\localhost.crt"
    sslcert="D:\\client.crt" 
    sslkey="D:\\client.key"
        
    try:
        connection = psycopg2.connect(user = user,
                                      password = password,
                                      host = host,
                                      port = port,
                                      dbname = dbname,
                                      sslmode=sslmode,
                                      sslrootcert=sslrootcert,
                                      sslcert=sslcert, 
                                      sslkey=sslkey
                                       )
        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print ( connection.get_dsn_parameters(),"\n")
        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record,"\n")
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
    passwd = 'Eurohelp'
    """                
    dsnSlave = "dbname=postgres user=postgres password=Eurohelp host=localhost port=5432"
    
    conn = psycopg2.connect(dbname='postgres', user='postgres', password=passwd, host='localhost', port='5432')
    #conn = psycopg2.connect(dsnSlave)
    print ( conn.get_dsn_parameters(),"\n")
    
    conn.close()
    """
    