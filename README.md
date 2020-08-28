# csdn_increase_vister
提升csdn博客的访问量
---
## Usage：
直接运行python文件即可，修改1.txt中的url，格式为文章名:url。
可以通过添加http头中的cookie字段来达到非匿名访问的效果，添加一个cookie头，这样子相当于多了一个已经登陆的用户来访问目标网页。
类似于下面这样：
> 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0',
>
>'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
>
>'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
>
>'Accept-Encoding': 'gzip, deflate, br',
>
>"Cookie" : "一个合法的cookie" 

 >
 
 可以开两种多线程，一种有http有cookie，一种没有，这样子就可以将速度翻倍，因为这就相当于有两个人一个是登陆用户，一个是匿名用户，两个人在不停的访问你的博客。
