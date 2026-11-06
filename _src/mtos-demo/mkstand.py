import os
d=os.path.dirname(os.path.abspath(__file__))+'/'
old=open(d+'../../mtos-demo-k7r4/index.html',encoding='utf-8').read()
head=old[:old.index('<title>')]
if 'noindex' not in head: head=head.replace('<meta charset="utf-8">','<meta charset="utf-8">\n<meta name="robots" content="noindex,nofollow">')
body=open(d+'mtos-demo.html',encoding='utf-8').read().replace('</style>','</style></head><body>',1)
open(d+'../../mtos-demo-k7r4/index.html','w',encoding='utf-8').write(head+body+'\n</body></html>')
