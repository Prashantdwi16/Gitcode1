from django.shortcuts import render
from .serializer import *
from .queries import *
from .helpers import *
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import hashlib
from rest_framework.exceptions import APIException
from datetime import datetime
import os

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def EmailLoginapi(request):
    try:
        serializer = EmailLoginSerialzers(data=request.data)
        if serializer.is_valid():
            EmailID = serializer.data["EmailID"]
            Password = serializer.data["Password"]
            userData = EmailLogin_q(EmailID, Password)
            if type(userData) == dict:
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data': userData,
                    'message': 'User Found successFully',
                }
                return Response(json_data)
            else:
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data': '',
                    'message': 'User Not Found',
                }
                return Response(json_data)
        else:
            json_data = {
                'status_code': 300,
                'status': 'Fail',
                'Reason': serializer.errors,
                'Remark': 'Send valid data'
            }
            return Response(json_data)
    except Exception as e:
        print("Error --------:", e)
        json_data = {
            'status_code': 400,
            'status': 'Fail',
            'Reason': e,
            'Remark': 'landed in exception',
        }
        raise APIException(json_data)
 
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def Signupapi(request):
    try:
        serializer = SignupSerialzers(data=request.data)
        if serializer.is_valid():
            Name = serializer.data["Name"]
            EmailID = serializer.data["EmailID"]                   
            Password = serializer.data["Password"]
            
           
            Data = {
                "Name":Name,
                "EmailID":EmailID,
                "Password":Password,
                
                "IsDeleted": "0",
                "CreatedAt": datetime.now(),
                "CreatedBy": "system",
                "UpdatedAt": datetime.now(),
                "UpdatedBy": "system"
                    }
            userData = Signup_q(Data.values())
           
            if userData:
                json_data = {

                    'status_code': 200,
                    'status': 'Success',
                    'message': 'Data  Inserted successFully',
                }
                return Response(json_data)
            else:
                json_data = {
                    
                    'status_code': 200,
                    'status': 'Success',
                    'message': 'Data  not saved',
                }
                return Response(json_data)
        else:
            json_data = {
                'status_code': 300,
                'status': 'Fail',
                'Reason': serializer.errors,
                'Remark': 'Send valid data'
            }
            return Response(json_data)
    except Exception as e:
        print("Error --------:", e)
        json_data = {
            'status_code': 400,
            'status': 'Fail',
            'Reason': e,
            'Remark': 'landed in exception',
        }
        raise APIException(json_data)    
    
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def FileUpload(request):
    try:
        serializer = UploadFileSerialzers(data=request.data)
        if serializer.is_valid():
            File = request.FILES.get("File")
            EmailID = serializer.data["EmailID"]  
            userData= Email_q(EmailID)                 #
            if userData:
                split_tup = os.path.splitext(str(File))
                # file_name = split_tup[0]
                file_extension = split_tup[1]
                if file_extension==".pptx" or file_extension==".docx" or file_extension==".xlsx":
                     filedata=second_file_uploader(File,"",str(File).split(' ')[0])
                     filepath = 'D:\Files'+filedata['path']+'/'+filedata['fileName']
                     Data = {
                        "File":filepath,
                        "EmailID":EmailID,
                        "IsDeleted": "0",
                        "CreatedAt": datetime.now(),
                        "CreatedBy": "system",
                        "UpdatedAt": datetime.now(),
                        "UpdatedBy": "system"
                            }
                     Data = Insertfile_q(Data.values())
                     if Data:
                        json_data = {

                            'status_code': 200,
                            'status': 'Success',
                            'message': 'Data  Inserted successFully',
                        }
                        return Response(json_data)
                     else:
                        json_data = {
                            
                            'status_code': 200,
                            'status': 'Success',
                            'message': 'Data  not saved',
                        }
                        return Response(json_data)
                else:
                    json_data = {

                        'status_code': 200,
                        'status': 'Success',
                        'message': 'File extension is not supported',
                    }
                    return Response(json_data)
            else:
                json_data = {
                    
                    'status_code': 200,
                    'status': 'Success',
                    'message': 'User not found',
                }
                return Response(json_data)
        else:
            json_data = {
                'status_code': 300,
                'status': 'Fail',
                'Reason': serializer.errors,
                'Remark': 'Send valid data'
            }
            return Response(json_data)
    except Exception as e:
        print("Error --------:", e)
        json_data = {
            'status_code': 400,
            'status': 'Fail',
            'Reason': e,
            'Remark': 'landed in exception',
        }
        raise APIException(json_data)    
    


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def AllList(request):
    try:
        
        page = get_page(request.data.get('page', 1))
        content = request.data.get('content', 20)
        numb = int(page)*int(content)
        pageNumber = int(numb)
        userData = DataList_q(pageNumber,content)
        count=countDataList_1()
        
        if userData :
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                            'data': userData,
                            'count': count['count'],
                            'message': 'Data successFully fetched ',
                }
                return Response(json_data)
        else:
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data': [],
                    'message': 'Data not Fetched',
                }
                return Response(json_data)      
    
    except Exception as e:
        print("Error --------:", e)
        json_data = {
            'status_code': 400,
            'status': 'Fail',
            'Reason': e,
            'Remark': 'landed in exception',
        }
        raise APIException(json_data)