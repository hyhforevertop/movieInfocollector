import requests_html
import csv

session=requests_html.HTMLSession()

url="https://movie.douban.com/top250?start=0"

r=session.get(url)
pages=0
file=open("movies.csv","w",newline="",encoding='utf-8')
csvwriter=csv.writer(file)
csvwriter.writerow(['电影名','导演','演员','年份','国家','类型'])
while pages <250:
    for i in range(1,26):
        title=r.html.find(f"#content > div > div.article > ol > li:nth-child({i}) > div > div.info > div.hd > a > span:nth-child(1)",first=True)
        title=title.text  #电影名称
        info=r.html.find(f"#content > div > div.article > ol > li:nth-child({i}) > div > div.info > div.bd > p:nth-child(1)",first=True)
        info=info.text

        info=info.split("\n")
        member=info[0]
        member=member.split("   ")
        director=member[0][4::]  #导演
        actor=member[1][4::]     #演员
        year=info[1].split(" / ")[0] #年份
        country=info[1].split(" / ")[1] #国家
        category=info[1].split(" / ")[2] #类型

        csvwriter.writerow([title,director,actor,year,country,category])

    pages+=25

file.close()