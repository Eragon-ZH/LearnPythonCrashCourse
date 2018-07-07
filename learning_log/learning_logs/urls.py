"""定义learning_logs的URL模式"""

from django.conf.urls import url

from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),

    # 显示所有的主题
    url(r'^topics/$', views.topics, name='topics'),

    # 显示特点的主题
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]
# 书上没有这一行在Django 2.0会报错
app_name = "learning_logs"
