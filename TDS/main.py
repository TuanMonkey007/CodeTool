import os
import requests
import sys
import time
from colorama import Fore, Style, init  # Import colorama để tạo màu sắc
# Khởi tạo colorama để hỗ trợ màu trên Windows
init(autoreset=True)

from TDS_Account import TDS_Account
from constants import *

if __name__ == "__main__":
    print(f"{Fore.BLUE}[ℹ] Đang lấy ACCESS_TOKEN từ .env...", end="", flush=True)
    time.sleep(1)  # Giả lập thời gian load

    ACCESS_TOKEN = APP_VALUE_TDS_TOKEN

    if not ACCESS_TOKEN:
        sys.stdout.write(f"\r{Fore.RED}[⚠] ERROR: ACCESS_TOKEN is missing! Vui lòng kiểm tra file .env!\n")
        sys.stdout.flush()
    else:
        sys.stdout.write(f"\r{Fore.GREEN}[✔] ACCESS_TOKEN found! Bắt đầu kiểm tra tài khoản...\n")
        sys.stdout.flush()
        acl = TDS_Account(ACCESS_TOKEN)
        acl.ShowInfo()
        # acl_job = acl.GetJob_FaceBook("facebook_follow","ALL")
        # print(acl_job)
        #print(acl.Receive_Coin("facebook_page", "WMYVW9QCMTFG54XA3AJR"))