# coding=utf-8
import os


WEBSITE_INFO = {"website_name": u"SJTU大学 OnlineJudge",
                "website_name_shortcut": u"JI oj",
                "website_footer": u"SJTU大学JI学院 <a href=\"http://www.sjtu.edu.cn/\">沪ICP备233333号-1</a>",
                # url结尾没有/
                "url": u"http://your-domain-or-ip.com"}


# https://github.com/QingdaoU/OnlineJudge/wiki/SMTP
SMTP_CONFIG = {"smtp_server": "smtp.domain.com",
               "email": "noreply@domain.com",
               "password": "your_password",
               "port": 25,
               "tls": True}


# 是否显示所有人的提交, False就只显示自己的
SHOW_ALL_SUBMISSIONS_LIST = False
