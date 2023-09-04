from django.db import connection, transaction, connections
import time
import os

def dictfetchall(cursor=''):
    # "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def dictfetchone(cursor=''):
    # "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return dict(zip([col[0] for col in desc], cursor.fetchone()))


    
def second_file_uploader(file_uploads, Files, filename):
    u_id = str(Files)
    f_name = str(filename).split()
    print("ffffffffffffffff",f_name)
    today = time.strftime("%Y/%m/%d")
    dirName = "D:\Files" + \
        u_id + str(f_name[0]) + "/" + today
    full_path = "D:\Files" + \
        u_id + str(f_name[0]) + "/" + today + "/" + file_uploads.name
    publish_path = "/media/social/" + u_id+str(f_name[0]) + "/" + today
    if not os.path.isdir(dirName):
        print("you are here now")
        os.makedirs(dirName)
        full_path = dirName+"/" + file_uploads.name
        with open(full_path, "wb+") as destination:

            for chunk in file_uploads.chunks():
                destination.write(chunk)
        destination.close()
    else:
        print("you are here now else ")
        with open(full_path, "wb+") as destination:
            for chunk in file_uploads.chunks():
                destination.write(chunk)
        destination.close()
    temp = str(time.time())
    extention = str(file_uploads.name).split(".")
    newtemp = temp.split('.')
    name = newtemp[0]+"."+extention[-1]
    oldpath = r"D:\Files" + u_id + \
        str(f_name[0]) + "/" + today + "/" + file_uploads.name
    newpath = r"D:\Files" + \
        u_id+str(f_name[0]) + "/" + today + "/"+str(name)
    os.rename(oldpath, newpath)
    data = dict()
    data.update(fileName=name)
    data.update(path=publish_path)
    print(data)
    return data


def get_page(num1):
    if type(num1)== str:
        if num1.isdigit():
            num=int(num1)
            if num<=1:
                return 0
            else:
                return num-1
        else:
            return 0
    elif type(num1)== int:
        num=int(num1)
        if num<=1:
            return 0
        else:
            return num-1
    else:
        return 0
