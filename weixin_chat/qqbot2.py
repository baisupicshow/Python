from qqbot import _bot as bot
bot.Login(['-q', '1431077852'])
bl = bot.List('buddy', '任')
if bl:
    b = bl[0]
    bot.SendTo(b, 'hello')

gl = bot.List('group', '苏州大学摄影分享')
if gl:
    group = gl[0]
    bot.SendTo(group,'大家好')