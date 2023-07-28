import requests_html
import csv

session=requests_html.HTMLSession()

file=open("movies.csv",'w',newline='',encoding='utf-8')

csvwriter=csv.writer(file)
csvwriter.writerow(['电影名','导演','主演','年份','国家','类型'])

pages=0

while pages <250:
    url = f"https://movie.douban.com/top250?start={pages}"

    r = session.get(url)
    for i in range(1,26):
        title=r.html.find(f"#content > div > div.article > ol > li:nth-child({i}) > div > div.info > div.hd > a > span:nth-child(1)",first=True)
        title=title.text  #电影名称
        info=r.html.find(f"#content > div > div.article > ol > li:nth-child({i}) > div > div.info > div.bd > p:nth-child(1)",first=True)
        info=info.text

        info=info.split("\n")
        member=info[0]

        if "主演" in member:
            member=member.split("   ")
            actor=member[1][4::]     #演员
            director = member[0][4::]  # 导演
        else:
            member = member.split("   ")
            actor='略'
            director=member[0][4::]
        year=info[1].split(" / ")[0] #年份
        country=info[1].split(" / ")[1] #国家
        category=info[1].split(" / ")[2] #类型

        csvwriter.writerow([title,director,actor,year,country,category])#写入csv文件


    pages+=25
