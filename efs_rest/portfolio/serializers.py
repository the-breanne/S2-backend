from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
            model = Todo

            fields = ('task_number', 'task_name', 'task_des', 'due_date')


