from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoSerializer,TimingTodoSerializer
from .models import Todo,TimingTodo
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication


# Create your views here.
@api_view(['GET','POST','PATCH'])
def home(request):
    if request.method == 'GET':
        return Response({
            'status': 'confirmed',
            'message': 'Framework is working',
            'Method': request.method,
        })
    elif request.method == 'POST':
        return Response({ 
            'status':'Cofirmed',
            'message': 'Framework is working',
            'Method': request.method,
            })
    elif request.method == 'PATCH':
        return Response({
            'status':'Cofirmed',
            'message': 'Framework is working',
            'Method': request.method,
            })
    else:
        return Response({
            'status':'Cofimred',
            'message': 'Framework is working',
            'Method': 'Others',
            })


@api_view(['GET'])
def getTodo(request):
    todo_obj = Todo.objects.all()
    serializer = TodoSerializer(todo_obj,many=True)
    return Response({
            'status':True,
            'Message':"Todo Fetched",
            'data':serializer.data
    })



@api_view(['POST'])
def postTodo(request):
    try:
        data = request.data
     
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'Message': "Created the Todo List",
                'data': serializer.data
            })
        else:
            return Response({
                'status': False,
                'Message': "Validation errors",
                'errors': serializer.errors
            })
    except Exception as e:
        return Response({
            'status': False,
            'Message': "Not Working Well",
            'error': str(e)
        })

@api_view(['PATCH'])
def patchTodo(request):
    try:
        data = request.data
        if not data.get('uid'):
            return Response({
            'status': False,
            'Message': "UID IS REQUIRED",
        })
        obj = Todo.objects.get(uid=data.get('uid'))
        serializer = TodoSerializer(obj,data = data,partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'Message': "Todo Updated",
                'data': serializer.data
            })
        return Response({
                'status': True,
                'Message': "Todo Updated",
                'data': serializer.data
            })
    except Todo.DoesNotExist:
        return Response({
            'status': False,
            'Message': "Invalid UID",
            'data': ''
        })
    
    except Exception as e:
        print(e)
        return Response({
            'status': False,
            'Message': "Invalid UID",
            'data': ''
        })
    
#Class view api for organzing all methods like POST,GET,PATCH
#Here we cannot make custom methods and routes in APIView(only defined methods like post,get,etc)
class TodoView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self,request):
       
       todo_obj = Todo.objects.all()
       serializer = TodoSerializer(todo_obj,many=True)
       return Response({
            'status':True,
            'Message':"Todo Fetched",
            'data':serializer.data
        })
   
    def post(self,request):
        try:
            data = request.data
            data['users'] = request.user.id
            serializer = TodoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                'status': True,
                'Message': "Created the Todo List",
                'data': serializer.data
                })
            else:
                return Response({
                'status': False,
                'Message': "Validation errors",
                'errors': serializer.errors
                })
        except Exception as e:
            return Response({
            'status': False,
            'Message': "Not Working Well",
            'error': str(e)
        })
    
    def patch(self,request):
        try:
            data = request.data
            if not data.get('uid'):
                return Response({
                'status': False,
                'Message': "UID IS REQUIRED",
                })
            obj = Todo.objects.get(uid=data.get('uid'))
            serializer = TodoSerializer(obj,data = data,partial= True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'Message': "Todo Updated",
                    'data': serializer.data
                })
            return Response({
                    'status': True,
                    'Message': "Todo Updated",
                    'data': serializer.data
                })
        except Todo.DoesNotExist:
            return Response({
                'status': False,
                'Message': "Invalid UID",
                'data': ''
            })
    
        except Exception as e:
            print(e)
            return Response({
                'status': False,
                'Message': "Invalid UID",
                'data': ''
            })

class TodoViewSet(viewsets.ModelViewSet):
    
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @action(detail=False,methods=['GET'])
    def get_date_todo(self,request):
        obj = TimingTodo.objects.all()
        serializer = TimingTodoSerializer(obj,many=True)
        return Response({
            'status': True,
            'Message': "Timing Todo Fetched",
            'data': serializer.data
        })

    @action(detail=False, methods=['POST'])
    #We put detail true, when we want to pass the id of the object in the url like def add(self,request,parameter)
    def add_date_to_todo(self,request):
        try:
            data = request.data

            if not data.get('todo'): 
                return Response({ 
                    'status': False, 
                    'Message': "todo is required", 
                    'error': "Missing todo" 
                })
            
            serializer = TimingTodoSerializer(data = data)
            if(serializer.is_valid()):
                serializer.save()
                return Response({
                    'status': True,
                    'Message': "Todo Updated",
                    'data': serializer.data
                })
            return Response({
                    'status': False,
                    'Message': "Invalid Data",
                    'data': serializer.data
                })
        
        except Exception as e:
            print(e)
            return Response({
                'status': False,
                'Message': "Something Went Wrong",
                'error': str(e)
            })
        

