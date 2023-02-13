from selenium import webdriver
from tabulate import tabulate
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from random import randrange
import random
import os
import getpass
from selenium.webdriver.common.action_chains import ActionChains
class real_bot:
    def __init__(self,email="",password="",files_path_img="",title_path="",file_title="",files_path_desc="",PATH="C:/chromedriver.exe"):
        option = Options()
        self.email = email
        self.password = password
        self.driver = webdriver.Chrome(chrome_options=option, executable_path=PATH)
        self.main_url = "https://www.facebook.com"
        self.market_url = "https://mtouch.facebook.com/marketplace/selling/item/"
        self.infobars = "--disable-infobars"
        self.extensions = "--disable-extensions"
        self.sizepageY = 768
        self.sizepageX = 1024

        self.files_path_img = files_path_img
        self.title_path = title_path
        self.file_title = file_title
        self.files_path_desc = files_path_desc
        self.setUp()
        self.login_()
        self.post_()
        time.sleep(random.randint(1,3))
        print("########## DONE ##########")
        self.driver.quit()

    def setUp(self):
            option = Options()
            option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2 })
            option.add_argument(self.infobars)
            option.add_argument(self.extensions)
            self.driver.set_window_size(self.sizepageX,self.sizepageX)
            self.driver.get(self.main_url)

    def login_(self):
        try:
            email = self.driver.find_element_by_id("email")
            email.send_keys(self.email)
            Password = self.driver.find_element_by_id("pass")
            Password.send_keys(self.password)
            button = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button").click()
        except Exception:
            print('Some exception occurred while trying to find username or password field')

    def check_files_images(self):
        files = os.listdir(self.files_path_img)

        generate = True
        while(generate):
            index = random.randrange(0,len(files))
            if files[index][:2] != "d_":
                generate = False
                print(files[index])
                return files[index]
            else:
                print("{},PICTURE ALREADY UPLOADED".format(files[index]))

    def desc_(self):
            files = os.listdir(self.files_path_desc)
            index = random.randrange(0,len(files))
            desc = open("{}/{}".format(self.files_path_desc,files[index]),"r")
            output = desc.readlines()
            x = ""
            for desc in output:
                x+=desc
            return x

    def post_(self):
        try:
            file_image = self.check_files_images()
            self.driver.get(self.market_url)
            time.sleep(random.randint(1,5))
            self.driver.get(self.market_url)
            
            image = self.driver.find_element_by_xpath('//input[@type="file"]')
            image.send_keys("{}/{}".format(self.files_path_img, file_image))
            print(file_image)

            title = open("{}/{}".format(self.title_path,self.file_title),"r")
            lines_title = title.readlines()
            title_len = len(lines_title)
            title_rdm = random.randint(0,title_len-1)
            print(lines_title[title_rdm])

            fill_title = self.driver.find_element_by_xpath('//input[@name="title"]')
            fill_title.send_keys("{}".format(lines_title[title_rdm]))

            fill_price = self.driver.find_element_by_xpath('//input[@name="price"]')
            fill_price.send_keys(randrange(100,1000,100))

            category = self.driver.find_element_by_xpath('//input[@name="category"]')
            category.click()
            time.sleep(random.randint(2,5))
            choice_category = self.driver.find_element_by_xpath("//div[contains(a,'Lain-lain')]")
            choice_category.click()

            location = self.driver.find_element_by_xpath('//input[@name="location"]')
            self.driver.execute_script("arguments[0].setAttribute('value',arguments[1])",location, "{}".format("Aceh"))
            time.sleep(random.randint(2,4))
            
            fill_desc = self.driver.find_element_by_xpath('//textarea[@name="description"]')
            fill_desc.send_keys(self.desc_())
            source = self.driver.page_source
            pcdata1 = str(source).split('id="u_0_25_')
            pcdata2 = pcdata1[1].split('"')
            #Eksekusi tombol
            buttonid = 'u_0_25_' + pcdata2[0]
            postbutton = self.driver.find_element_by_xpath("//*[@id='"+buttonid+"']")
            postbutton.click()
            os.rename("{}/{}".format(self.files_path_img, file_image),
                      "{}/d_{}".format(self.files_path_img, file_image))
        except Exception:
            print('Some exception occurred while trying to find content field')

    def tables():
        head = {
                'Command': "Command",
                'Keterangan': "Keterangan",
            }
        data = [
            {'Command': 1, 'Keterangan': "Auto Post 1x (Direct Post)"},
            {'Command': 2, 'Keterangan': "Auto Post dengan looping (DELAY 30 sec)"},
            {'Command': 3, 'Keterangan': "STOP PROGRAM"}
        ]
        return tabulate(data, headers=head, tablefmt="grid") 
        
    
def loop():
    data = int(input("LOOP: "))
    for i in range(1,data+1):
        real_bot(email=email,password=password,files_path_img=path_image,title_path=title_path,file_title=file_title,files_path_desc = desc_path)
        print("DELAY!! 30 sec")
        time.sleep(random.randrange(20,30))
    return print("LOOPED")


if __name__ == "__main__":
    print(" Account Facebook ".center(100,"#"))
    print("\n")
    print("#Email: Gunakan Akun Facebook (old)")
    print("#Password: Password tidak akan ditampilkan dikonsol")
    print("#Catatan: Jika sudah mengisi password dengan benar langsung tekan enter untuk melanjutkan")
    print("\n")
    print("#".center(100,"#"))
    email = input("> Email: ")
    password = getpass.getpass("> Password: ")
    os.system("cls")
    print(" PATH ".center(100,"#"))
    print("\n")
    print("#CONTOH UNTUK PATH FOLDER DAN FILE")
    print("#FOLDER IMAGES: D:/produk/gambar_produk")
    print("#FOLDER TITLE: D:/produk/gambar_produk/title")
    print("#FOLDER TITLE: D:/produk/gambar_produk/deskripsi")
    print("#FOLDER TITLE: title.txt")
    print("\n")
    print("#".center(100,"#"))
    input_path_image = input("> FOLDER IMAGES: ")
    input_path_title = input("> FOLDER TITLE: ")
    files_path_desc = input("> FOLDER DESKRIPSI: ")
    input_path_ftitle = input("> NAMA FILE TITLE: ")

    path_image = input_path_image
    title_path = input_path_title
    file_title = input_path_ftitle
    desc_path = files_path_desc
    

    print(real_bot.tables())
    inputs = int(input("Command: "))

    while(inputs != 3):
        if(inputs == 1):
            real_bot(email=email,password=password,files_path_img=path_image,title_path=title_path,file_title=file_title,files_path_desc = desc_path)
        elif(inputs == 2):
            loop()
            pass
        else:
            print("Command not found..")
        print(real_bot.tables())
        inputs = int(input("Command: "))

