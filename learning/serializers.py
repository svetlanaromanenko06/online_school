from rest_framework import serializers
from rest_framework.fields import IntegerField

from learning.models import Course, Lesson, Payment
from learning.validators import UrlValidator

class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [UrlValidator(field='video_url')]



class CourseSerializer(serializers.ModelSerializer):
    count_lesson = serializers.SerializerMethodField()
    lesson = LessonSerializer(source='lesson_set', many=True, read_only=True)

    def get_count_lesson(self, instance):
        return Lesson.objects.filter(course__id=instance.id).count()

    class Meta:
        model = Course
        fields = ['title', 'count_lesson', 'lesson']



class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'