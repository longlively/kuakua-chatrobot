"""
		WeChat KUAKUA_Robot v0.1
"""

# -*- coding:utf-8 -*- 

import itchat, re
from itchat.content import *
import random
import json

"""
    Constants
"""

REPLY = {'夸我': ['你真是太优秀',
                  '啥也不说了，夸！',
				  '每天看到你心情好呢！',
				  '你真是一位可爱的小天使啊！',
				  '一看你就是美丽与善良的化身 夸！',			  
				  '你上辈子一定拯救了银河系吧，优秀！',
				  '德才兼备说的就是你这样的社会主义接班人',
                  '以后你就是夸夸群里的元老，就是夸夸之父，简称夸父',
				  '你这句话完美的表达了你想被夸的坚定信念，你一定是一个执着追求自己理想的人！'
                  '你的头像，深深的感动了我，那副温情的画面，是最好的陪伴，只有最真挚细腻的人，才会映照出这幅有爱的画面',],
         'default': ['太棒了',
                     '真不错',
                     '好开心',
                     '嗯那',
                     '没什么好说的了，我送你一道彩虹屁吧']}

@itchat.msg_register([TEXT], isGroupChat=True)
def text_reply(msg):
        # 这里一定要修改成你想加群的群的名称  
    if msg['User']['NickName'] == '改成 群名称':
        print('Message from: %s' % msg['User']['NickName'])
        # 发送者的昵称
        username = msg['ActualNickName']
        print('Who sent it: %s' % username)

        match = re.search('夸我', msg['Text']) or re.search('求夸', msg['Text']) or re.search('夸一下', msg['Text'])
        if match:
            print('-+-+' * 5)
            print('Message content:%s' % msg['Content'])
            print('夸我 is: %s' % (match is not None))
            randomIdx = random.randint(0, len(REPLY['夸我']) - 1)
            itchat.send('@' + '%s\n%s' % (username, REPLY['夸我'][randomIdx]), msg['FromUserName'])


        print('isAt is:%s' % msg['isAt'])

        if msg['isAt']:
            randomIdx = random.randint(0, len(REPLY['default']) - 1)
            itchat.send('@' + '%s\n%s' % (username, REPLY['default'][randomIdx]), msg['FromUserName'])
            print('-+-+'*5)

itchat.auto_login(enableCmdQR=True, hotReload=True)
itchat.run()
