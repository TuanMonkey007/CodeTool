import os
import requests
import sys
import time
from colorama import Fore, Style, init  # Import colorama để tạo màu sắc
from constants import *
# Khởi tạo colorama để hỗ trợ màu trên Windows
init(autoreset=True)

class TDS_Account:
    def __init__(self, access_token):
        self.TDS_token = access_token
        self.user = None
        self.xu = None
        self.xudie = None

    def ShowInfo(self):
        url = f"https://traodoisub.com/api/?fields=profile&access_token={self.TDS_token}"

        # Hiển thị thông báo đang tải với hiệu ứng
        print(f"{Fore.BLUE}[ℹ] Đang lấy thông tin tài khoản...", end="", flush=True)
        time.sleep(1)  # Giả lập độ trễ cho hiệu ứng
        
        response = requests.get(url)

        if "error" not in response.json():
            data = response.json()
            if data.get("success") == 200:
                self.user = data["data"].get("user")
                self.xu = data["data"].get("xu")
                self.xudie = data["data"].get("xudie")

                # Ghi đè dòng trước đó
                sys.stdout.write(f"\r{Fore.GREEN}[✔] SUCCESS! Tài khoản đã xác thực.  \n")
                sys.stdout.flush()

                print(f"{Fore.YELLOW}👤 User: {Fore.CYAN}{self.user} | 💰 Xu: {Fore.CYAN}{self.xu} | ❌ Xudie: {Fore.CYAN}{self.xudie}")

            else:
                sys.stdout.write(f"\r{Fore.RED}[✖] API response error: {data}  \n")
                sys.stdout.flush()
        else:
            sys.stdout.write(f"\r{Fore.RED}[✖] Failed to fetch data! HTTP Status: {response.status_code}  \n")
            sys.stdout.flush()

    def GetJob_FaceBook(self, job_field, job_type):
        # Kiểm tra nếu job_type hợp lệ
        if job_field not in APP_VALUE_JOB_FIELD_FB:
            print(f"{Fore.RED}[❌] ERROR: Job type '{job_field}' không hợp lệ!{Style.RESET_ALL}")
            return None
        elif job_field in {"facebook_reaction", "facebook_reactioncmt"}:
            if job_type not in APP_VALUE_JOB_TYPE_FB:
                print(f"{Fore.RED}[❌] ERROR: Job type '{job_type}' không hợp lệ!{Style.RESET_ALL}")
                return None
            else:
                url = f"https://traodoisub.com/api/?fields={job_field}&access_token={self.TDS_token}&type={job_type}"
                print(f"{Fore.BLUE}[🔄] Đang lấy danh sách {APP_VALUE_JOB_FIELD_FB[job_field]} | {Fore.GREEN} Loại {APP_VALUE_JOB_TYPE_FB[job_type]}...", end="", flush=True)
                
        else:
            url = f"https://traodoisub.com/api/?fields={job_field}&access_token={self.TDS_token}"
            print(f"{Fore.BLUE}[🔄] Đang lấy danh sách {APP_VALUE_JOB_FIELD_FB[job_field]} | {Fore.GREEN} Loại Tất cả ...", end="", flush=True)
        

        # Gửi request lấy job
        response = requests.get(url)

        # Kiểm tra response
        if "error" not in response.text:
            print(f"\r{Fore.GREEN}[✅] Thành công! Nhận job {APP_VALUE_JOB_FIELD_FB[job_field]}{Style.RESET_ALL}")
            return response.json()
        else:
            print(f"\r{Fore.RED}[❌] Lỗi lấy job ({response.status_code}): {response.text}{Style.RESET_ALL}")
            return None

    def Receive_Coin(self, job_type, job_id):
        """
        Gửi yêu cầu nhận xu sau khi hoàn thành nhiệm vụ.
        
        :param job_type: Loại nhiệm vụ (facebook_reaction, facebook_share, ...)
        :param job_id: ID của nhiệm vụ đã làm xong
        """
        if job_type not in APP_VALUE_JOB_FIELD_FB:
            print(f"{Fore.RED}[❌] Lỗi: Loại nhiệm vụ '{job_type}' không hợp lệ!{Style.RESET_ALL}")
            return None

        url = f"https://traodoisub.com/api/coin/?type={job_type}&id={job_id}&access_token={self.TDS_token}"

        print(f"{Fore.BLUE}[🔄] Đang nhận xu từ nhiệm vụ {APP_VALUE_JOB_FIELD_FB[job_type]} - ID: {job_id}...", end="", flush=True)
        time.sleep(1)  # Giả lập độ trễ

        response = requests.get(url)

        if "error" not in response.text:
            print(f"\r{Fore.GREEN}[✅] Nhận xu thành công từ {APP_VALUE_JOB_FIELD_FB[job_type]} - ID {job_id}.{Style.RESET_ALL}")
            return response.json()
        else:
            error_message = response.json().get("error", "Không rõ lỗi")  # Chuyển response thành JSON
            print(f"\r{Fore.RED}[❌] Lỗi nhận xu ({response.status_code}): {error_message}{Style.RESET_ALL}")
            return None
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    pass