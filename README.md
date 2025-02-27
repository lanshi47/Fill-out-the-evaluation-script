# 南通理工学院自动评教系统脚本使用说明

## 简介

这个Python脚本旨在自动化南通理工学院的教学评估过程。它使用Selenium WebDriver来模拟用户操作，自动登录评教系统，填写评估表单，并提交结果。

## 功能特点

- 自动登录评教系统
- 自动选择"优秀"选项
- 自动提交评教表单
- 验证评分是否为100分
- 支持多次评教（默认18次）

## 环境要求

- Python 3.x
- Chrome浏览器
- ChromeDriver（与Chrome浏览器版本匹配）

## 依赖库

- selenium
- pandas
- lxml
- python-dotenv（用于管理环境变量）

## 安装步骤

1. 克隆或下载此项目到本地。
2. 安装所需的Python库：
   ```
   pip install selenium pandas lxml python-dotenv
   ```
3. 下载与您的Chrome浏览器版本匹配的ChromeDriver，并将其路径添加到系统环境变量中。

## 配置

1. 在项目根目录创建一个`.env`文件。
2. 在`.env`文件中添加以下配置：
   ```
   CHROME_DRIVER_PATH=<您的ChromeDriver路径>
   URL=<评教系统的URL>
   USERNAME=<您的用户名>
   PASSWORD=<您的密码>
   ```

## 使用方法

1. 确保所有配置都已正确设置。
2. 运行脚本：
   ```
   python script.py
   ```
3. 脚本将自动执行18次评教过程。

## 注意事项

- 请确保您的网络连接稳定。
- 脚本执行过程中，请勿手动操作浏览器。
- 如果遇到验证码或其他安全措施，可能需要手动干预。
- 使用自动化脚本可能违反学校政策，请谨慎使用。

## 免责声明

本脚本仅用于学习和研究目的。使用者应当遵守学校规定和相关法律法规。作者不对使用此脚本造成的任何问题负责。

## 贡献

欢迎提出改进建议或直接贡献代码。请通过 GitHub Issues 或 Pull Requests 与我们联系。

## 许可证

[MIT License](LICENSE)
