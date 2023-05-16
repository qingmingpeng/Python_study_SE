


# file = open(r"D:\Python Study\trading_system_autotest\config\environment.yaml",encoding="utf-8")

#
# try:
#     a = file.read()
#     print(a)
# except Exception as e:
#     print(e)
# finally:
#     file.close()


# with open(r"D:\Python Study\trading_system_autotest\config\environment.yaml","r",encoding="utf-8") as file:
#
#     for i in file.readlines():
#         print("====")
#         print(i)
#     file.seek(0)
#     a = file.read()
#     print(a)

import yaml
from common.tools import get_project_path,sep

class GetConf:
    def __init__(self):
        with open(get_project_path()+sep(["config","environment.yaml"],True),"r",encoding="utf-8") as file:
            self.env = yaml.load(file,Loader=yaml.FullLoader)


    def get_username_password(self):
        return self.env["username"],self.env["password"]



if __name__=='__main__':
    print(GetConf().get_username_password())