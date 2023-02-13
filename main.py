import real_bot as bot
import subprocess
import time
import http.client as httplib

current_machine_id = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()

def loop():
    data = int(input("LOOP: "))
    try:
        for i in range(1,data+1):
            do = bot.real_bot(email=email,password=password,files_path_img=path_image,title_path=title_path,file_title=file_title,files_path_desc = desc_path)
            countdown_(bot.random.randrange(20,30))
    except Exception:
        return print("FAILED")

  
def checkInternetHttplib(url="www.facebook.com", timeout=3):
    connection = httplib.HTTPConnection(url, timeout=timeout)
    try:
        connection.request("HEAD", "/")
        connection.close()
        return True
    except Exception as exep:
        return False
def countdown_(t):
        while t:
            mins,sec = divmod(t,60)
            timer = '{:02d}:{:02d}'.format(mins,sec)
            print(timer,end="\r")
            time.sleep(1)
            t -= 1

if(checkInternetHttplib() == True):
    if(current_machine_id == "266C1F68-0DD3-3745-88B8-D8C4976AC676"):
    
        if __name__ == "__main__":
            print(" Account Facebook ".center(100,"#"))
            print("\n")
            print("#Email: Gunakan Akun Facebook (old)")
            print("#Password: Password tidak akan ditampilkan dikonsol")
            print("#Catatan: Jika sudah mengisi password dengan benar langsung tekan enter untuk melanjutkan")
            print("\n")
            print("#".center(100,"#"))
            email = input("> Email: ")
            password = bot.getpass.getpass("> Password: ")
            bot.os.system("cls")
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
            

            print(bot.real_bot.tables())
            inputs = int(input("Command: "))

            while(inputs != 3):
                if(inputs == 1):
                    bot.real_bot(email=email,password=password,files_path_img=path_image,title_path=title_path,file_title=file_title,files_path_desc = desc_path)
                elif(inputs == 2):
                    loop()
                    pass
                else:
                    print("Command not found..")
                print(bot.real_bot.tables())
                inputs = int(input("Command: "))
    else:
        bot.os.system('cls')
        print("HWID TIDAK TERDAFTAR!")
        countdown_(10)
        exit();
else:
    print("YOU ARE NOT CONNECTED INTERNET!!! \n")
    countdown_(10)
    exit();