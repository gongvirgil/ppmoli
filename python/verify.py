#!/usr/bin/env python
# -* - coding: UTF-8 -* -
import urllib
import StringIO
from PIL import Image
import os


# 图片x轴的投影，如果有数据（黑色像素点）值为1否则为0
def get_projection_x(image):
    p_x = [0 for x in xrange(image.size[0])]
    for w in xrange(image.size[1]):
        for h in xrange(image.size[0]):
            if image.getpixel((h, w)) == 0:
                p_x[h] = 1
    return p_x


# 获取分割后的x轴坐标点
# 返回值为[起始位置, 长度] 的列表
def get_split_seq(projection_x):
    res = []
    for idx in xrange(len(projection_x) - 1):
        p1 = projection_x[idx]
        p2 = projection_x[idx + 1]
        if p1 == 1 and idx == 0:
            res.append([idx, 1])
        elif p1 == 0 and p2 == 0:
            continue
        elif p1 == 1 and p2 == 1:
            res[-1][1] += 1
        elif p1 == 0 and p2 == 1:
            res.append([idx + 1, 1])
        elif p1 == 1 and p2 == 0:
            continue
    return res


# 分割后的图片，x轴分割后，同时去掉y轴上线多余的空白
def split_image(image, split_seq=None):
    if split_seq is None:
        split_seq = get_split_seq(get_projection_x(image))
    length = len(split_seq)
    imgs = [[] for i in xrange(length)]
    res = []
    for w in xrange(image.size[1]):
        line = [image.getpixel((h, w)) for h in xrange(image.size[0])]
        for idx in xrange(length):
            pos = split_seq[idx][0]
            llen = split_seq[idx][1]
            l = line[pos:pos + llen]
            imgs[idx].append(l)
    for idx in xrange(length):
        datas = []
        height = 0
        for data in imgs[idx]:
            flag = False
            for d in data:
                if d == 0:
                    flag = True
            if flag is True:
                height += 1
                datas += data
        child_img = Image.new('L', (split_seq[idx][1], height))
        child_img.putdata(datas)
        res.append(child_img)
    return res

# # 从文件系统中加载样本数据
# trained_data = []
# for i in xrange(10):
#     trained_data.append([])
#     dir = os.listdir(os.path.join('trained', '%d' % i))
#         for file in dir:
#             fn = os.path.join('trained', '%d' % i, file)
#             img = Image.open(fn)
#             trained_data[i].append(list(img.getdata()))
#             img.close()


# 存放训练数据
if not os.path.exists('training'):
    os.mkdir('training')

# 存放训练结果
if not os.path.exists('training/result'):
    os.mkdir('training/result')

for i in xrange(10):
    # 网络上的图片转换成Image对象
    image = Image.open(StringIO.StringIO(urllib.urlopen(
        'http://10.0.0.231:1046/Admin/User/Verify?timestamp=%d' % i).read()))
    # 灰度化处理
    # 有很多种算法，这里选择rgb加权平均值算法
    gray_image = Image.new('L', image.size)
    # 获得rgb数据序列，每一个都是(r,g,b)三元组
    raw_data = image.getdata()
    gray_data = []
    for rgb in raw_data:
        value = 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]
        # value就是灰度值，这里使用127作为阀值，
        # 小于127的就认为是黑色也就是0 大于等于127的就是白色，也就是255
        if value < 127:
            gray_data.append(0)
        else:
            gray_data.append(255)
    gray_image.putdata(gray_data)
    res = split_image(gray_image)
    for a in xrange(len(res)):
        gray_image.save(os.path.join('training/result', '%d_%d.png' % (i, a)))
    gray_image.save(os.path.join('training', '%d.png' % i))
