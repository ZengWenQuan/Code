# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import numpy
import  requests
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url="https://movie.douban.com/j/chart/top_list"

    parma={
        "type":"24",
        'interval_id':'100:90',
        'action':'',
        'start':20,
        "limit":20
    }
    header={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    resp=requests.get(url,params=parma,headers=header)
    print(resp)

    print(resp.json())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
