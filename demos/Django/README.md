# Django

## 安装Django

```shell
pip install django
```

安装成功后会在 Python 安装目录下的 Scripts 文件夹中生成一个 `django-admin.exe` 文件（Windows系统）

## 创建Django项目

```shell
"D:\Python\Scripts\django-admin.exe" startproject 项目名称
# 如果已将 Scripts 目录加入环境变量：
django-admin startproject 项目名称
```

或者直接使用 PyCharm 的 `New Project` 进行创建

项目目录：

```
  mysite
    │  manage.py            【项目的管理】
    └─ mysite
            __init__.py     
            settings.py     【项目配置文件】
            urls.py         【URL和函数的对应关系】
            asgi.py         【接收请求】
            wsgi.py         【接收请求】
```

## 创建App

```shell
python manage.py startapp appname
```

App目录：

```
myapp
 │  admin.py
 │  apps.py         【对应应用的配置文件】
 │  models.py       【数据模块，用于设计数据库等】
 │  tests.py        【单元测试】
 │  views.py        【视图层，直接和浏览器进行交互】
 │  __init__.py
 │
 └─migrations
         __init__.py

```

## 快速上手

https://docs.djangoproject.com/zh-hans/4.2/intro/tutorial01/

## 数据库操作

> ORM

- 安装mysqlclient
  `pip install mysqlclient`