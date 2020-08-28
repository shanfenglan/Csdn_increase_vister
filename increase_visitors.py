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
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        "cookie": ""
        }
        self.head2 = \
        {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        }
        self.head3 = \
            {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
                'Accept-Encoding': 'gzip, deflate, br',
            }

        self.head4 = \
            {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0',
                     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                      'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
                      'Accept-Encoding': 'gzip, deflate, br',
            }

        self.head_list = []
        self.head_list.append(self.head)
        self.head_list.append(self.head2)
        self.head_list.append(self.head2)
        self.head_list.append(self.head2)

        self.lock = threading.Lock()
        self.thread_list = []

    def run(self,list,head,name):
        self.pattern2 = "编辑"
        self.pattern = '<span class="read-count">(.*?)</span>'
        while(1):
            response = requests.get(list, headers=head).text
            if len(head) == 5:
                # print(re.search(self.pattern2,response))
                if re.search(self.pattern2,response) is None:
                    # print('失败')
                    pass
            liulanliang = re.findall(self.pattern, response)
            # temporary = name+":"+liulanliang[0]
            # self.lock.acquire()
            # self.out.append(temporary)
            print(liulanliang)
            # self.lock.release()
            time.sleep(63)



    def generate_thread(self):
        for i in range(len(self.url_list)):
            for y in self.head_list:
                thread = threading.Thread(target=self.run,kwargs={"list":self.url_list[i],"head":y,"name":self.name_list[i]})
                self.thread_list.append(thread)

    def start_thread(self):
        for i in self.thread_list:
            time.sleep(0.1)
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
