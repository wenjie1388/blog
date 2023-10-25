# 开发环境

DEBUG_ = True


MYSQLNAME = "blog"
MYSQLUSER = "root"
MYSQLPASSWORD = "root"
MYSQLHOST = "127.0.0.1"
MYSQLPORT = 3307

REDIS_HOST = "127.0.0.1"
REDIS0_LOCATION = "redis://" + REDIS_HOST + ":6379/0"
REDIS1_LOCATION = "redis://" + REDIS_HOST + ":6379/1"
REDIS2_LOCATION = "redis://" + REDIS_HOST + ":6379/2"
REDIS3_LOCATION = "redis://" + REDIS_HOST + ":6379/3"
REDIS4_LOCATION = "redis://" + REDIS_HOST + ":6379/4"
REDIS5_LOCATION = "redis://" + REDIS_HOST + ":6379/5"
REDIS6_LOCATION = "redis://" + REDIS_HOST + ":6379/6"
REDIS7_LOCATION = "redis://" + REDIS_HOST + ":6379/7"
REDIS8_LOCATION = "redis://" + REDIS_HOST + ":6379/8"
REDIS9_LOCATION = "redis://" + REDIS_HOST + ":6379/9"
REDIS10_LOCATION = "redis://" + REDIS_HOST + ":6379/10"


EMAIL_BACKEND1 = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST1 = "smtp.qq.com"
EMAIL_PORT1 = 25  # 或者 465/587是设置了 SSL 加密方式
# EMAIL_HOST_USER1 = '1293426034@qq.com'
EMAIL_HOST_USER1 = "wenjie1388@foxmail.com"
EMAIL_HOST_PASSWORD1 = "vctgmzghjpbribcc"  # 第三方登陆使用的授权密码
EMAIL_USE_TLS1 = True  # 这里必须是 True，否则发送不成功
