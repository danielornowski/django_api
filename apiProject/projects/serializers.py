from rest_framework import serializers
from .models import Project, Comment


class ProjectModelSerializer(serializers.ModelSerializer):
    created = serializers.SerializerMethodField()
    end_date = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'name', 'created', 'end_date', 'status']

    def get_created(self, obj):
        return obj.created.strftime('%Y-%m-%d')

    def get_end_date(self, obj):
        if obj.end_date is None:
            return None
        else:
            return obj.end_date.strftime('%Y-%m-%d')

    def set_created(self, obj):
        return obj.created.strftime('%Y-%m-%d')


class CommentModelSerializer(serializers.ModelSerializer):
    add_date = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ['id', 'project_id', 'author', 'add_date', 'body']
    def get_add_date(self, obj):
        return obj.add_date.strftime('%Y-%m-%d - %H:%m')