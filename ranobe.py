import requests
from bs4 import BeautifulSoup

# План:
# 1. делаем список из всех урлов  https://ранобэ.рф/revolyutsiya-maga-vosmogo-klassa
# 2. заходим в каждый и собираем данные
# 3. сохраняем в тхт файл

def get_html():
    url = 'https://ranobelib.me/8-keullaeseu-mabeobsaui-hoegwi'#'https://ranobehub.org/ranobe/367-revolution-of-the-8th-class-mage#tab-contents'#'https://ранобэ.рф/revolyutsiya-maga-vosmogo-klassa'
    r = requests.get(url)
    return r.text


def get_chapter_links(html: str):
    soup = BeautifulSoup(html,'lxml')
    chapters = soup.find('div', {'class': 'chapters-list'}).find_all('a', {"class": "link-default"})
    chapters_link = []
    for link in chapters:
        chapters_link.append(link.get('href'))
    return chapters_link


def write_content_in_txt(content: list, name: str):
    f = open(name + '.txt', 'a',  encoding='UTF-8')
    for i in content:
        f.write(i + '\n')
    f.close()


def get_chapter_content(links: list):
    content_chapter = []
    count = 0
    for url in links:
        if count == 5 and content_chapter is not None:
            write_content_in_txt(content_chapter, "Революция мага восьмого класса")
            count = 0
            content_chapter =[]
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        content = soup.find('div', {'class': 'reader-container container container_center'})
        name_chapter = soup.find('a', {'class': 'menu__item text-truncate menu__item_active'})
        content_chapter.append("\n\n\t\t\t" + name_chapter.text + "\n\n"+content.text)
        count += 1
    return content_chapter


def main():
    html = get_html()
    links = get_chapter_links(html)
    content = get_chapter_content(links)



if __name__ == '__main__':
    main()
