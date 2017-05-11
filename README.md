# ImitationTmall
用python开发基于Django框架的仿天猫网站项目
This Project is imitation Tmall website for using python based on the development of Django framework

+ python2.7
+ django1.9
+ 基于xadmin的后台管理系统
+ django-simple-captcha0.4.6：验证码功能

## 开发目的
+ 首先是，对过往python学习的一次总结，因为之后打算从事wab后端开发。因此动手写一个项目是对知识点的一次梳理
+ 再者，作为一个非科班出身的家伙，我更需要一个实际作品来提高自己的竞争力。因为我也不喜欢夸夸其谈。

## 开发顺序
在写此文档时，并没有进行实际的开发。但是整个网站的架构已经在我的脑海中了。我在此做一个简单的梳理。<del>之后可能会改动</del>
+ 首先是需求的分析，通过参观实际天猫网站，进行需求分析和表结构设计
+ APP和model.py的设计
+ xadmin搭建的后台管理系统
+ 用户登录、注册及找回密码功能（验证码及验证邮件功能）
+ 无需登录的页面功能实现（利用模板继承功能）
+ 添加购物车功能实现；
+ 其他功能实现；
+ 全局搜索功能实现；
+ 细节完善
+ 部署上线
+ 写个总结报告

## 前端素材
前端文件来源于这个网站：[HOW2J.CN](http://how2j.cn/)
这是一个很不错的学习java web开发的网站。我直接把实战项目中的前端文件拿来用了。只做了少量修改。
项目开发数周，由于使用到django的模板，因此已经将原前端素材改的面目全非，为了实现某些功能甚至添加了新的页面。

## 脑图
![仿天猫项目脑图](https://github.com/Liweimin0512/ImitationTmall/blob/master/XMindtmall.png?raw=true)
