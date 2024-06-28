import requests
from bs4 import BeautifulSoup
class Kitaplık:
    def __init__(self):
        self.base_url = "https://books.toscrape.com/catalogue/category/books_1/index.html"
        self.not_page_url = "https://books.toscrape.com/catalogue/category/books/{}/index.html"
        self.page_url= "https://books.toscrape.com/catalogue/category/books/{}/page-{}.html"
        self.response = requests.get(self.base_url)
        self.soup = BeautifulSoup(self.response.content, "html.parser")
        self.page = 1
        self.list = []
        self.category_list = []
        self.categories_fetched = False
    def categories(self):
        if self.response.status_code == 200:
            html = self.soup.find("div", class_="side_categories")
            side_categories = html.find_all("a")
            for index,side in enumerate(side_categories[1:],start=1):
                category = side.text.strip()
                self.category_list.append(f"{index}-{category}")
            self.categories_fetched = True
            return self.category_list
        else:
            return None
    def put_in(self,category):
        self.page = 1
        self.list = []
        previous_page_title = None # sayfa başlığı birkez gelmesi için none olarak girdim
        while True:
            if self.page == 1:  # sayfa sayısı 1 taneysee kullanıcağım url
                self.response = requests.get(self.not_page_url.format(category))
            else:  # eğer birden fazla sayfa varsa çağıracağım url
                self.response = requests.get(self.page_url.format(category,self.page))
            if self.response.status_code != 200:
                break
            self.soup = BeautifulSoup(self.response.content, "html.parser")
            sayfa_title = self.soup.find("h1").text.strip()
            if sayfa_title != previous_page_title:

                print(f"{sayfa_title}\n") # çağırdığım sayfanın ilk olarak başlığını yazdım
                previous_page_title = sayfa_title
            html = self.soup.find_all("article",class_="product_pod")
            if not html:
                break
            start_index = (self.page - 1)*20+1   # devam eden sayfaların numaralarını ekleme yaparak indexledim
            for index,book in enumerate(html,start=start_index):  # burada verilen kitapları numaraladım
                title = book.h3.a["title"]
                price = book.find("p",class_="price_color").text
                stars_icon = len(book.find_all("i",class_="icon-star"))
                star =  "*"* stars_icon
                image = book.find("img")["src"] # img url lerini buldum
                image_url = "https://books.toscrape.com"+ image.replace("../..","") # img ur fazlalıklarından kurtuldum
                self.list.append(f"{index} -Book Name:{title} - Book price:{price} - {star} - Book img :{image_url}") # istediğim görüntüyü listede görünteledim
            self.page+=1 #sayfa sayısını her defasında varsa artırdık

        return self.list  # listeyi çalıştır
    # aynı fonks defalarca yazmak yerine sadece url ye isim yollayarak return yaptım
    def travel_2(self):
        return self.put_in("travel_2") # bir kez yazdığımız kodları put_in e isim yollayarak istediğimizkütüphane yolunu yaptık
    def mystery_3(self):
        return self.put_in("mystery_3")
    def historical_fiction_4(self):
        return self.put_in("historical-fiction_4")
    def sequential_art_5(self):
        return self.put_in("sequential-art_5")
    def classics_6(self):
        return self.put_in("classics_6")
    def philosophy_7(self):
        return self.put_in("philosophy_7")
    def romance_8(self):
        return self.put_in("romance_8")
    def womens_fiction_9(self):
        return self.put_in("womens-fiction_9")
    def fiction_10(self):
        return self.put_in("fiction_10")
    def childrens_11(self):
        return self.put_in("childrens_11")
    def religion_12(self):
        return self.put_in("religion_12")
    def nonfiction_13(self):
        return self.put_in("nonfiction_13")
    def music_14(self):
        return self.put_in("music_14")
    def default_15(self):
        return self.put_in("default_15")
    def science_fiction_16(self):
        return self.put_in("science-fiction_16")
    def sports_and_games_17(self):
        return self.put_in("sports-and-games_17")
    def add_a_comment_18(self):
        return self.put_in("add-a-comment_18")
    def fantasy_19(self):
        return self.put_in("fantasy_19")
    def new_adult_20(self):
        return self.put_in("new-adult_20")
    def young_adult_21(self):
        return self.put_in("young-adult_21")
    def science_22(self):
        return self.put_in("science_22")
    def poetry_23(self):
        return self.put_in("poetry_23")
    def paranormal_24(self):
        return self.put_in("paranormal_24")
    def art_25(self):
        return self.put_in("art_25")
    def psychology_26(self):
        return self.put_in("psychology_26")
    def autobiography_27(self):
        return self.put_in("autobiography_27")
    def parenting_28(self):
        return self.put_in("parenting_28")
    def adult_fiction_29(self):
        return self.put_in("adult-fiction_29")
    def humor_30(self):
        return self.put_in("humor_30")
    def horror_31(self):
        return self.put_in("horror_31")
    def history_32(self):
        return self.put_in("history_32")
    def food_and_drink_33(self):
        return self.put_in("food-and-drink_33")
    def christian_fiction_34(self):
        return self.put_in("christian-fiction_34")
    def business_35(self):
        return self.put_in("business_35")
    def biography_36(self):
        return self.put_in("biography_36")
    def thriller_37(self):
        return self.put_in("thriller_37")
    def contemporary_38(self):
        return self.put_in("contemporary_38")
    def spirituality_39(self):
        return self.put_in("spirituality_39")
    def academic_40(self):
        return self.put_in("academic_40")
    def self_help_41(self):
        return self.put_in("self-help_41")
    def historical_42(self):
        return self.put_in("historical_42")
    def christian_43(self):
        return self.put_in("christian_43")
    def suspense_44(self):
        return self.put_in("suspense_44")
    def short_stories_45(self):
        return self.put_in("short-stories_45")
    def novels_46(self):
        return self.put_in("novels_46")
    def health_47(self):
        return self.put_in("health_47")
    def politics_48(self):
        return self.put_in("politics_48")
    def cultural_49(self):
        return self.put_in("cultural_49")
    def erotica_50(self):
        return self.put_in("erotica_50")
    def crime_51(self):
        return self.put_in("crime_51")

    def menü(self):  # fonksiyonları dict yapısına göre sıraladım
        category_method = {
            1: self.travel_2,
            2: self.mystery_3,
            3: self.historical_fiction_4,
            4: self.sequential_art_5,
            5: self.classics_6,
            6: self.philosophy_7,
            7: self.romance_8,
            8: self.womens_fiction_9,
            9: self.fiction_10,
            10: self.childrens_11,
            11: self.religion_12,
            12: self.nonfiction_13,
            13: self.music_14,
            14: self.default_15,
            15: self.science_fiction_16,
            16: self.sports_and_games_17,
            17: self.add_a_comment_18,
            18: self.fantasy_19,
            19: self.new_adult_20,
            20: self.young_adult_21,
            21: self.science_22,
            22: self.poetry_23,
            23: self.paranormal_24,
            24: self.art_25,
            25: self.psychology_26,
            26: self.autobiography_27,
            27: self.parenting_28,
            28: self.adult_fiction_29,
            29: self.humor_30,
            30: self.horror_31,
            31: self.history_32,
            32: self.food_and_drink_33,
            33: self.christian_fiction_34,
            34: self.business_35,
            35: self.biography_36,
            36: self.thriller_37,
            37: self.contemporary_38,
            38: self.spirituality_39,
            39: self.academic_40,
            40: self.self_help_41,
            41: self.historical_42,
            42: self.christian_43,
            43: self.suspense_44,
            44: self.short_stories_45,
            45: self.novels_46,
            46: self.health_47,
            47: self.politics_48,
            48: self.cultural_49,
            49: self.erotica_50,
            50: self.crime_51,
        }

        while True:
            seçenekler = input("1-Kategoriler\n2-Çıkış\nSeçiniz: ")
            if seçenekler == "2":
                break
            elif seçenekler == "1":
                if not self.categories_fetched:
                    categories = self.categories()
                    if categories:
                        for category in categories:
                            print(category)            # kategorileri listeledik
                    else:
                        print("Kategoriler alınamadı.")
                        continue
                else:
                    for category in self.category_list:
                        print(category)
                try:
                    choice = int(input("Bir kategori numarası seçiniz: ").strip()) # ekranda yazdırdığımız seçenekleri seçmek için input aldık
                    if choice in category_method: # sözlüğün içinde seçtiğimiz seçeneği çağırttık
                        books = category_method[choice]()
                        for book in books:
                            print(book)
                    else:
                        print("Geçersiz kategori numarası.")
                except ValueError:
                    print("Lütfen geçerli bir numara giriniz.")
            else:
                print("Geçersiz seçenek. Tekrar deneyiniz.")

if __name__ == "__main__":
    kitaplik = Kitaplık()
    kitaplik.menü()
