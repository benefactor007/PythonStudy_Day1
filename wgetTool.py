# coding=utf-8
import os
import sys

# wget -c -t 5 --no-check-certificate --http-user='wu_j7' --http-password='Tianyuan==222'
# 'https://cnninvmsvn01.joynext.com/CNS3.0_GP/30_DevelopLibrary/03_SW/00_Overall/03_SWIntegration&IntegrationTest
# /C047-RC8/all_images_C047_RC8.tar.gz'
def adv_wget(user_account: str,user_password: str, downloadLink: str, timesTry: int = 5) :
    #print("wget -c -t "+ str(timesTry) + " --no-check-certificate " + "--http-user=" + user_account + " --http-password=" + user_password + " " + downloadLink)
    os.system("wget -c -t "+ str(timesTry) + " --no-check-certificate " + "--http-user=" + user_account + " --http-password=" + user_password + " " + "'"+downloadLink +"'")


def main():
    if len(sys.argv) > 1:
        link1 = sys.argv[1]
    else:
        link1 = input ("Please input the software download link: ")
    adv_wget("wu_j7", "'Tianyuan==333'", link1)


if __name__ == '__main__':
    main()
