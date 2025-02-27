import logging
import os

import script # Import the script module

# Call the scrape_current_page function from the script module

# ---------------------- 主程序 ----------------------
if __name__ == "__main__":
    try:
        # 检查配置文件
        if not os.path.exists('config.ini'):
            raise FileNotFoundError("缺少配置文件 config.ini")
        script.scrape_current_page()
        logging.info("脚本执行完毕")

    except Exception as e:
        logging.critical("主程序异常终止", exc_info=True)

