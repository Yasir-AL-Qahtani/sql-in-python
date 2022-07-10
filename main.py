from pymysql import connect
db=connect()
cursor=db.cursor()

def addmoive():
    id=input("Enter the id")
    cursor.execute(f"SELECT * FROM moives where id={id}")
    data=cursor.fetchall()
    if data:
        print("Sorry the id is taken")
        return
    name=input("Enter moive name")
    year=input("Enter moive year")
    rank=input("Enter moive rank")
    cursor.execute(f"Insert into movies values ({id},{name},{year},{rank})")
    print("Done!!")

def deleteMoive():
    id=input("Enter the id ")
    cursor.execute(f"SELECT * FROM moives where id={id}")
    data=cursor.fetchall()
    if data:
        name = input("Enter moive name")
        year = input("Enter moive year")
        rank = input("Enter moive rank")
        cursor.execute(f"DELETE FROM movies WHERE id={id},name={name},year={year},rank={rank}")
        print("Done!!")

    print("Sorry the id not found")
    return


def addActors():
    id=input("Enter the id")
    cursor.execute(f"SELECT * FROM actors where id={id}")
    data=cursor.fetchall()
    if data:
        print("Sorry the id is taken")
        return
    first_name = input("Enter actor name")
    last_name = input("Enter actor last name")
    gender = input("Enter actor gender")
    cursor.execute(f"Insert into movies values ({id},{first_name},{last_name},{gender})")
    print("Done!!")


def deleteActors():
    id = input("Enter the id ")
    cursor.execute(f"SELECT * FROM actors where id={id}")
    data=cursor.fetchall()
    if data:
        first_name = input("Enter actor name")
        last_name = input("Enter actor last name")
        gender = input("Enter actor gender")
        cursor.execute(f"DELETE FROM actors WHERE id={id},first_name={first_name},last_name={last_name},gender={gender}")

    print("Sorry the id not found")
    return


def Adddirectors():
    id = input("Enter the id ")
    cursor.execute(f"SELECT * FROM directors where id={id}")
    data=cursor.fetchall()
    if data:
        print("Sorry the id is taken")
        return

    first_name = input("Enter actor name")
    last_name = input("Enter actor last name")
    cursor.execute(f"Insert into directors values ({id},{first_name},{last_name})")
    print("Done!!")

def DeleteDirectors():
    id = input("Enter the id ")
    cursor.execute(f"SELECT * FROM directors where id={id}")
    data = cursor.fetchall()
    if data:
        first_name = input("Enter actor name")
        last_name = input("Enter actor last name")
        cursor.execute(f"DELETE FROM directors WHERE id={id},first_name={first_name},last_name={last_name}")

    print("Sorry the id not found")
    return

def AddRoles():
    actor_id = input("Enter the Actor id ")
    moive_id=input("Enter the moive Id")
    role=input("Enter the actor role")
    cursor.execute(f"SELECT * FROM roles where actor_id={actor_id}, moive_id={moive_id},role{role}")
    data=cursor.fetchall()
    if data:
        print("Sorry the roles exist")
        return
    else:
      cursor.execute(f"SELECT * FROM actors where id={actor_id}")
      data2=cursor.fetchall()
      cursor.execute(f"SELECT * FROM moives where id={moive_id}")
      data3=cursor.fetchall()
      if data2 and data3:
          cursor.execute(f"Insert into roles values ({actor_id},{moive_id},{role})")
          print("Done!!")

      else:
          print("Sorry you cant add")
          return





def DeleteRoles():
    actor_id = input("Enter the Actor id ")
    moive_id = input("Enter the moive Id")
    role = input("Enter the actor role")
    cursor.execute(f"SELECT * FROM roles where actor_id={actor_id}, moive_id={moive_id},role{role}")
    data = cursor.fetchall()
    if data:
        cursor.execute(f"DELETE FROM roles WHERE actor_id={actor_id},moive_id={moive_id},role={role}")
        print("Done")

    print("the Role not found")
    return














































