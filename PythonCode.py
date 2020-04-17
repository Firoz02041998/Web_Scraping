from bs4 import BeautifulSoup
import requests
import csv

##with open('testhtml.html') as html_file:
##soup = BeautifulSoup(html_file,'lxml')
##print(soup.prettify())
##match = soup.title.text
##print(match)

web = requests.get('').text
csv_file = open('data.csv','w')
data_write = csv.writer(csv_file)
data_write.writerow(['Heading','Summary','Video_Link'])
code = BeautifulSoup(web,'lxml')
for article in code.find_all('article'):

    ##print(article.prettify())


    header = article.h2.a.text
    print(header)


    details = article.find('div',class_='entry-content').p.text
    print(details)


    try:
        link = article.find('iframe',class_='youtube-player')['src']
        ##print(link)
        id = link.split('/')[4]
        computed_id = id.split('?')[0]
        ##print(computed_id)
        new_link = f'https://youtube.com/watch?v={computed_id}'
    except Exception as e:
        new_link = None
    print(new_link)    
    print()

    data_write.writerow([header,details,new_link])

csv_file.close()