from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import re
import json

# headers = {
#     'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
# }

driver = webdriver.Chrome()
driver.get("https://huggingface.co/datasets/AdaptLLM/finance-tasks/viewer/Headline/test")


# 窗口全屏
driver.maximize_window()
# time.sleep(5)

# # 翻页按钮
# next_page_button_xpath = "//a[@class='flex items-center rounded-lg px-2.5 py-1 hover:bg-gray-50 dark:hover:bg-gray-800']"



# 20547
i = 1
while True:



    index_str = str(i%100)
    print(index_str)
    # 定位标签
    content = driver.find_elements(By.XPATH,
                                   "//tr[@class='group cursor-pointer space-x-4 divide-x border-b outline-offset-[-2px] last:border-none odd:bg-gray-50 hover:bg-gray-100 dark:odd:bg-gray-925 dark:hover:bg-gray-850 ']["+index_str+"]/*")

    if content:
        # 初始化元素列表
        list_element = []

        for j, element in enumerate(content):
            if j == 2 or j == 3:
                list_element.append(element.text)
            elif j > 3:
                j = 0

        # print(list_element)

        # 使用正则表达式获取所有问题序列中满足条件的序列
        questions_match = re.compile(r'(\bDoes\b[^?]*\?)(.*?\b(Yes|No)\b)', re.IGNORECASE | re.DOTALL)


        # questions_match = re.compile(r'(Does (.*?)\?)\s*(Yes|No)')
        # questions_match = re.compile(r'Does (.*?)(?=(Yes|No))')

        questions = questions_match.findall(list_element[0])
        # print(questions)

        # 初始化问题列表和答案列表
        question_list = []
        answer_list = []

        for question_answer in questions:
            # 清除空白字符
            # question_answer = question_answer.strip()
            # 分割每串语句并保存到对应列表中
            question = question_answer[0]
            question_list.append(question)

            # 正则表达式匹配 "Yes" 或 "No"
            pattern = re.compile(r'\b(Yes|No)\b', re.IGNORECASE)
            answer = pattern.findall(question_answer[1])
            answer_list.append(answer[0])

        # print(question_list)
        # print(answer_list)

        with open('json_file', 'a', encoding='utf-8') as f:
            for question, answer in zip(question_list, answer_list):
                # 构建json格式
                json_object = {
                    "id": list_element[1],
                    "Question": question,
                    "Answer": answer
                }
                # 写入json_file
                json.dump(json_object, f, ensure_ascii=False, indent=4)
                f.write('\n')

        # 尝试寻找下一页按钮
        if i % 100 == 0:
            try:
                before_url = driver.current_url
                print("URL before click:", before_url)
                # 等待显示可点击
                wait = WebDriverWait(driver, 20)
                click_element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body[@class='flex flex-col min-h-screen bg-white dark:bg-gray-950 text-black DatasetViewerPage']/div[@class='flex min-h-screen flex-col']/main[@class='flex flex-1 flex-col']/div[@class='SVELTE_HYDRATER contents']/div[@class='flex flex-col w-full']/div[@class='px-2.5 flex max-h-full flex-col overflow-hidden sm:h-[calc(100dvh-5.5rem)] xl:h-[calc(100dvh-3rem)] ']/div[@class='-mx-2.5 flex flex-1 flex-col overflow-hidden border-t min-h-64']/nav/ul[@class='flex select-none items-center justify-between space-x-2 text-gray-700 sm:justify-center border-t border-dashed border-gray-300 bg-gradient-to-b from-gray-100 to-white py-1 text-center font-mono text-xs dark:border-gray-700 dark:from-gray-950 dark:to-gray-900 ']/*/a[@class='flex items-center rounded-lg px-2.5 py-1 hover:bg-gray-50 dark:hover:bg-gray-800 ']")))
                # click_element.click()
                driver.execute_script("arguments[0].click();", click_element)

                time.sleep(10)

                after_url = driver.current_url
                print("URL after click:", after_url)
            except TimeoutException:
                # 超时退出
                print("time out!")
                break
            except NoSuchElementException:
                # 末页退出
                print("No more page!")
                break
            except Exception as e:
                # 其他异常处理
                print(f"An error occured: {e}")
                break
    i += 1

# 关闭浏览器
driver.quit()

print('succeed!')
