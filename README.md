看见有5个fork很惊喜，代码我会持续优化的，不过最近在添java那边的坑。所以，coming soooooon！
# ImitationTmall
+ 仿照[天猫]()搭建的电商平台
+ 欢迎交流，也可以在issues中向我提问
+ 欢迎star

## 开发环境
+ python2.7
+ django1.9
+ 基于xadmin的后台管理系统
+ django-simple-captcha0.4.6：验证码功能
+ mysql5.5

## 开发目的
+ 首先是，对过往python学习的一次总结，因为之后打算从事wab后端开发。因此动手写一个项目是对知识点的一次梳理
+ 再者，作为一个非科班出身的家伙，我更需要一个实际作品来提高自己的竞争力。因为我也不喜欢夸夸其谈。

## 开发顺序
在写此文档时，并没有进行实际的开发。但是整个网站的架构已经在我的脑海中了。我在此做一个简单的梳理。<del>之后可能会改动</del>
+ 首先是需求的分析，通过参观实际天猫网站，进行需求分析和表结构设计
+ APP和model.py的设计
+ xadmin搭建的后台管理系统
+ 用户登录、注册及找回密码功能（验证码及验证邮件功能）
+ 无需登录的页面功能实现（主要围绕商品）
+ 需要登陆的页面功能实现（主要围绕订单）
+ 购物车相关功能实现；
+ 全局搜索功能实现；
+ 细节完善
+ 部署上线

## 网站功能
![仿天猫项目脑图](https://github.com/Liweimin0512/ImitationTmall/blob/master/XMindtmall.png?raw=true)

# 如何部署项目
这个我也在研究。

## 前端素材
前端文件来源于此网站：[HOW2J.CN](http://how2j.cn/)（一个很不错的学习java web开发的网站，安利一发）
项目开发过程中，由于使用了django模板template系统，因此已经将原文件改的有点儿面目全非了。<del>想到自己还没静下心真正学习前端技术呢。算是一次修炼吧。</del>
用到了Bootstrap

# 如何启动项目
+ 首先将项目克隆到本地，然后添加虚拟环境，项目依赖包。
+ 配置数据库
  1 确保你安装了正确版本的mysql
  2 在setting.py中将DATABASES文件修改为你本地的数据库。
```python
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "imitationtmall",
        'USER': "root",
        'PASSWORD': "admin",
        'HOST': "127.0.0.1",

    }
 }
```

+ 之后利用```migrate```命令来创建数据表
+ 我在项目中提供了我的数据库备份，可以直接将数据库内容导入。
+ 然后run server



