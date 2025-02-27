import logging
import os

import script

# ---------------------- 主程序 ----------------------
if __name__ == "__main__":
    try:
        # 检查配置文件
        if not os.path.exists('.env'):
            raise FileNotFoundError("缺少配置文件 .env")
        script.scrape_current_page()
        logging.info("脚本执行完毕")

    except Exception as e:
        logging.critical("主程序异常终止", exc_info=True)
