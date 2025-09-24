import os     #وارد کردن ماژول ها
import glob


file=glob.glob('*')   #گرفتن فایل ها از مسیر فایل اصلی
ext_set=set()

for each_f in file :          #پیمایش بین فایل های   پوشه پروژه مان
    ext=each_f.split('.')[1]
    ext_set.add(ext)
    
def make () :
    for ex in ext_set :
        os.makedirs(ex+'file')
        
        
def move () :
    for each_f in file :
        ext=each_f.split('.')[1]
        os.rename(each_f,ext+'file')
        

make()
move()