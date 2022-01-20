import sys
import cv2
import numpy as np
import random

print('-'*30)
print('视频鬼畜化工具-0.0.2')
print('author: shr-NaHCO3')
print('-'*30)
# 文件输入，不可以包含路径
video = ""
# 处理率
get_frame_num = 1
# 输出图像大小
output_width = 150
output_height = 50
keep_image_proportion = True

try: 
    video = input('要转换的视频名称(不可以包含路径，需要添加后缀名)：\n    ')
    get_frame_num = int(input('视频处理率(越小越流畅，但是需要花费更多时间)：\n    '))
    keep_image_proportion = input('输出文件是否保持原有比例？[yes/no]：\n    ')
    if keep_image_proportion=='yes':
        keep_image_proportion = True
        output_width = int(input('输出文件的宽度(高度将根据原比例自动计算。)：\n    '))
        if output_width<=0 or output_width>=200:
            if input('宽度过大，可能导致视频无法正常播放。是否继续？[yes/no]')!='yes':
                input('强制终止程序。')
                sys.exit(0)
    else: 
        keep_image_proportion = False
        output_width = int(input('输出文件的宽度：\n    '))
        output_height = int(input('输出文件的高度：\n    '))
except: input("输入错误。程序将强制终止。")+sys.exit(0)







# 等比例缩放
if keep_image_proportion:
    capx = cv2.VideoCapture(video)
    output_height = int((capx.read()[1].shape[0]*(output_width/capx.read()[1].shape[1]))*0.5)



def list_to_video_string(list):
    BLACK_AND_WHITE_STRING = [
        '█▇▆▅▄▃▂▁ ',
    ]
    res=[]
    for item in list:
        fs = BLACK_AND_WHITE_STRING[random.randint(0, len(BLACK_AND_WHITE_STRING)-1)]
        # fs = BLACK_AND_WHITE_STRING[0]
        res.append(fs[int(item//(255/(len(fs))))-1])
        
    return ''.join(res)



# 获取视频对象
cap = cv2.VideoCapture(video)

#结果
res = [f'{output_width}|{output_height}|{get_frame_num}|{cap.get(cv2.CAP_PROP_FPS)}']
 # 输出长|输出宽|处理率|帧率



# 生成字符串数组
if cap.isOpened():
    # 计数器
    _counter = 0

    # 循环读取并操作
    while True:
        # 读取图像
        ret, img = cap.read()
        if not ret:
            break
        print(f'processing frame{_counter}...', end='')
        
        # 为防止占用过高，根据处理率处理相应帧
        if _counter%get_frame_num==0:
            # 缩放
            img = cv2.resize(img, (output_width, output_height))

            # 转化为灰白图像
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            pre_res = []
            for row in np.array(img).tolist():
                pre_res.append(list_to_video_string(row))
            res.append('\\n'.join(pre_res))

            # # 保存
            # cv2.imwrite(f'{video}_{_counter}.jpg', img)

            print('done.')
        else:
            print('discard.')

        _counter+=1
else:
    print("ERROR: CAN NOT OPEN FILE")



# 存储
with open('./vedio.vt', 'w', encoding='utf8') as f:
    f.write('\n'.join(res))

print('结果已保存。')

input()