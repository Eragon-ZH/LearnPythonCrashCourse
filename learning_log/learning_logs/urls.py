"""定义learning_logs的URL模式"""

from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    # 主页
    path('', views.index, name='index'),

    # 显示所有主题
    path('topics/', views.topics, name='topics'),

    # 单个主题
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # 添加新主题
    path('new_topic/', views.new_topic, name='new_topic'),

    # 添加新项目
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # 编辑项目
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
# 书上没有这一行在Django 2.0会报错
app_name = "learning_logs"
