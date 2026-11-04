import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def bypass_gtraffic(url):
    # Cấu hình trình duyệt Chrome
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless") # Bỏ comment dòng này nếu muốn chạy ẩn trình duyệt không hiện giao diện
    options.add_argument("--disable-notifications")
    
    driver = webdriver.Chrome(options=options)
    
    try:
        print(f"Đang truy cập vào liên kết: {url}")
        driver.get(url)
        
        # Chờ trang tải hoàn tất
        wait = WebDriverWait(driver, 30)
        
        # Bước 03: Cuộn xuống cuối trang để tìm nút lấy mã
        print("Đang cuộn xuống cuối trang...")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Đợi thời gian đếm ngược hoặc tải nội dung (thường các trang này yêu cầu đợi vài giây)
        time.sleep(10)
        
        # Tương tác với nút lấy mã hoặc ô nhập mã xác nhận (Bước 04)
        # Lưu ý: XPath dưới đây mang tính chất minh họa, cần kiểm tra (Inspect) mã nguồn thực tế của trang để chỉnh sửa nếu cấu trúc thay đổi
        try:
            get_code_btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'lấy mã') or contains(@class, 'btn')]"))
            )
            get_code_btn.click()
            print("Đã nhấn nút lấy mã.")
        except Exception as e:
            print("Không tìm thấy nút tự động, vui lòng kiểm tra lại phần tử trên trang:", e)
            
        # Giữ trình duyệt mở để quan sát kết quả thực thi
        input("Nhấn Enter để kết thúc và đóng trình duyệt...")

    except Exception as e:
        print(f"Đã xảy ra lỗi trong quá trình chạy: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    # Liên kết được lấy từ hình ảnh tải lên
    target_url = "https://gtraffic.io/9Qa6Fn9"
    bypass_gtraffic(target_url)
