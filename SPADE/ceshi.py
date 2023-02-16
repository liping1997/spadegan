import os
for i in os.listdir('./datasets/image'):
    a=i.replace('image','')
    os.rename('./datasets/image/{}'.format(i),'./datasets/image/{}'.format(a))