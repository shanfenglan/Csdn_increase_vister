import re,requests,threading,time,os
position = os.getcwd()
pwd = position + "/1.txt"
list = []
name = []
with open(pwd, 'r') as temporary_file:
    for i in temporary_file:
        i = i.strip("\n")
        list.append(i.split(":",1)[1])
        name.append(i.split(":",1)[0])

class I_V():
    def __init__(self,blog_list,name_list):
        self.out = []
        self.flag = 0
        self.url_list = blog_list
        self.name_list = name_list
        self.head = \
            {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
                'Accept-Encoding': 'gzip, deflate',
                "cookie":""
            }

        self.head_list = []
        # self.head_list.append(self.head)
        self.head_list.append(self.head)
        self.lock = threading.Lock()
        self.thread_list = []

    def run(self,list,head,name):
        self.pattern2 = "编辑"
        self.pattern = '<span class="read-count">(.*?)</span>'
        response = requests.get(list, headers=head).text
        print(response)
        if len(head) == 5:
            if re.search(self.pattern2,response) is None:
                print('失败')
        liulanliang = re.findall(self.pattern, response)
        print(liulanliang)


    def generate_thread(self):
        for i in range(len(self.url_list)):
            for y in self.head_list:
                thread = threading.Thread(target=self.run,kwargs={"list":self.url_list[i],"head":y,"name":self.name_list[i]})
                self.thread_list.append(thread)

    def start_thread(self):
        for i in self.thread_list:
            i.start()

        for i in self.thread_list:
            i.join()
    def save(self):
        with open("/Users/shukasakai/Desktop/2.txt", 'w') as temporary_file2:
            for i in self.out:
                i = i + '\n'
                temporary_file2.writelines(i)

    def auto(self):
        self.generate_thread()
        self.start_thread()

if __name__ == '__main__':
    A = I_V(list,name)
    A.auto()