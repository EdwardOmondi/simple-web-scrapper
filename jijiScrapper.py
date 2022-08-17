import requests
from bs4 import BeautifulSoup

endPage = 50


def scrapper(endPage):
    count = 1
    page = 1

    while (count <= endPage):
        print("Started new page: "+str(count))
        print("-    -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -")
        URL = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=car+parts&_sacat=33707&LH_TitleDesc=0&_pgn=" + \
            str(count)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        imgs = soup.find_all("img")
        # imgs = imgs[13:]
        if (len(imgs) == 0):
            break
        for img in imgs:
            try:
                img_title = img.attrs.get("alt").replace(" ", "")
                # print("image title: ", img_title)
                img_link = img.attrs.get("src")
                # print("image link: ", img_link)
                image = requests.get(img_link).content
                filename = img_title+".png"
                with open(filename, "wb") as file:
                    file.write(image)
            except:
                print("not possible")
        count += 1
        print("-    -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -")


print('\a')


scrapper(endPage)

print('\a')
