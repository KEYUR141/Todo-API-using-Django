from rest_framework import serializers
from .models import TimingTodo, Todo
import re
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        #The Meta is used to point which type of model or which model we are using from models.py
        model = Todo
        fields = ['user','todo_title','todo_desc','is_completed','uid']
        #exclude = ['updated_at','created_at']

    def get_slugify(self,obj):
        return slugify(obj.todo_title)  # returns slugified title
    
    def validate(self,validated_data):
        if validated_data.get('todo_title'):
            todo_title = validated_data['todo_title']
            if len(todo_title) < 3:
                raise serializers.ValidationError('Todo title must be at least 3 characters long')
            
            regex = re.compile('[@_!#$%^&*()<>?|\}{~:]')
            if regex.search(todo_title) is not None:
                raise serializers.ValidationError('Todo_title cannot contains special characters')
        return validated_data
    

class TimingTodoSerializer(serializers.ModelSerializer):
    todo = TodoSerializer()
    
    class Meta:
        model = TimingTodo
        exclude = ['created_at','updated_at']
        