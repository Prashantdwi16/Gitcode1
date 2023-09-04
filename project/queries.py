from django.db import connection, transaction, connections
from .helpers import *



def EmailLogin_q(EmailID, Password):
    """_summary get EmailLogin_q
    """
    with connections["company"].cursor() as cursor:
        resp = cursor.execute("""SELECT ID, LoginUUID, Name, EmailID, 
                              Password, IsDeleted, CreatedAt, CreatedBy, UpdatedAt, UpdatedBy 
                              FROM company.login 
                              where EmailID='{}' and Password='{}' and IsDeleted='0';
                              """.format(EmailID, Password))
        if resp and cursor.rowcount:
            resp = dictfetchone(cursor)
        else:
            resp = None

    return resp

def Email_q(EmailID):
    """
    """
    with connections["company"].cursor() as cursor:
        resp = cursor.execute("""SELECT  EmailID
                             
                              FROM company.login 
                              where EmailID='{}' and IsDeleted='0';
                              """.format(EmailID))
        if resp and cursor.rowcount:
            resp = dictfetchone(cursor)
        else:
            resp = None

    return resp


def Signup_q(Data):
    """_summary_
    This Function Makes Querry to Insert user Data
    """
    with connections["company"].cursor() as cursor:
        resp = cursor.execute("""INSERT INTO  company.login  (LoginUUID, Name, EmailID, 
                              Password, IsDeleted, CreatedAt, CreatedBy, UpdatedAt, UpdatedBy)
         VALUES (UUID(), %s, %s, %s, %s, %s, %s, %s, %s);""",Data )
   
    return resp

def Insertfile_q(Data):
    """_summary_
    This Function Makes Querry to Insert user Data
    """
    with connections["company"].cursor() as cursor:
        resp = cursor.execute("""INSERT INTO  company.uploadfiles(uploadfilesUUID, File, EmailID,
                               IsDeleted, CreatedAt, 
                              CreatedBy, UpdatedAt, UpdatedBy)
         VALUES (UUID(), %s, %s, %s, %s, %s, %s, %s);""",Data )
   
    return resp



def DataList_q(pageNumber, content):
    """_summary_
    Selecting
    """
    with connections["company"].cursor() as cursor:
        resp = cursor.execute(f"""SELECT  up.ID, up.uploadfilesUUID, up.File, up.EmailID, up.IsDeleted,
                               up.CreatedAt, up.CreatedBy, up.UpdatedAt, up.UpdatedBy
                              FROM company.uploadfiles up
                              Left JOIN company.login lu
                              ON up.EmailID = lu.EmailID
                              where  up.IsDeleted= '0'  and lu.IsDeleted= '0'   
                              group by up.ID order by up.id asc limit {pageNumber},{content} ;""")
        if resp and cursor.rowcount:
            # resp = dictfetchall(cursor) // for get all table
            resp = dictfetchall(cursor)
        else:
            resp = None

    return resp  

def countDataList_1():
    """_summary_
    counting
    """
    with connections["company"].cursor() as cursor:
        resp = cursor.execute(f"""SELECT  count(up.ID) count
                              FROM company.uploadfiles up
                              Left JOIN company.login lu
                              ON up.EmailID = lu.EmailID
                              where  up.IsDeleted= '0'  and lu.IsDeleted= '0'   
                                ;""")
        if resp and cursor.rowcount:
            resp = dictfetchone(cursor)
        else:
            resp = None

    return resp  