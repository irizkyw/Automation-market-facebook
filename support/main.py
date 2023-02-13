# import os,random
# #DEMO
# class main:
#     def __init__(self,files_path_img="D:/do this/pemutih",files_path_desc="D:/do this/desc"):
#         self.files_path_img = files_path_img
#         self.files_path_desc = files_path_desc
#         self.output()
#         self.desc_()

#     def check(self):
#         files = os.listdir(self.files_path_img)

#         generate = True
#         while(generate):
#             index = random.randrange(0,len(files))
#             if files[index][:2] != "d_":
#                 generate = False
#                 return files[index]
#             else:
#                 print("{},PICTURE ALREADY UPLOADED".format(files[index]))

#     def desc_(self):
#         files = os.listdir(self.files_path_desc)
#         try:
#             index = random.randrange(0,len(files))
#             desc = open("{}/{}".format(self.files_path_desc,files[index]),"r")
#             output = desc.readlines()
#             x = ""
#             for desc in output:
#                 x+=desc
#             return x
#         except Exception:
#             print("DESC NOT FOUND")
#         # return desc
#     def output(self):
#         print(self.desc_())
        
# if __name__ == "__main__":
#     main()
import subprocess

current_machine_id = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()

print("HWID: ",current_machine_id)