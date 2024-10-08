import os
libri_path = '/mnt/data/user/fan_xiaoran/librilight/combined_3s/'
list_dir=os.listdir(libri_path)
# print(len(os.listdir(libri_path)))
print("列表生成结束，开始遍历")
count=0
for i in range(1000):
    path=libri_path+list_dir[i]
    for root,_,files in os.walk(path):
        for filename in files:
            if filename.endswith(".wav"):
                count+=1
    print(count)

# import time
# t1=time.time()
# count=0
# for root, _, files in os.walk(libri_path):
#     for filename in files:
#         if filename.endswith('.wav'):
#             count+=1
# print(count)
# print(f"用时{time.time()-t1}s")

