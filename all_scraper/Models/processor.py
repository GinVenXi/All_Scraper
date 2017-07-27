#coding: utf-8
'''
创建人：Javen
创建时间：
'''
import sys
import datetime

class Model_Processor():
    def __init__(self):
        pass

    def formatNumber(self, number, region):
        if (region == "com"):
            self.number = number.split("-")[0].strip().replace(".", "").replace("$", "").replace("#", "").replace(",", "").replace(" Free", "").replace("Paid", "").replace("%", "").strip()
        elif (region == "co.uk"):
            self.number = number.split("-")[0].strip().replace(".", "").replace("£", "").replace("#", "").replace(",", "").replace(" Free", "").replace("Paid", "").replace("from", "").replace("%", "").strip()
        elif (region == "de"):
            self.number = number.split("-")[0].strip().replace(".", "").replace("Nr", "").replace("EUR", "").replace("#", "").replace(",", "").replace(" Free", "").replace("Paid", "").replace("ab", "").replace("%", "").strip()
        elif (region == "co.jp"):
            self.number = number.split("-")[0].strip().replace(".", "").replace("￥", "").replace("#", "").replace(",", "").replace(" Free", "").replace("Paid", "").replace("より", "").replace("%", "").strip()
        elif (region == "fr" or region == "es" or region == "it"):
            self.number = number.split("-")[0].strip().replace(".", "").replace("à partir de", "").replace("Nr", "").replace("EUR", "").replace("#", "").replace(",", "").replace(" Free", "").replace("Paid", "").replace("%", "").replace("n°", "").replace("nº", "").replace(" ", "").strip()
        elif (region == "ca"):
            self.number = number.split("-")[0].strip().replace(".", "").replace("from CDN$", "").replace("CDN$", "").replace("#", "").replace(",", "").replace(" Free", "").replace("Paid", "").replace("%", "").strip()
        else:
            pass

        return self.number

    def formatRating(self, rating, region):
        if (region == "com" or region == "co.uk" or region == "ca"):
            self.rating = rating.replace(" out of 5 stars", "").replace(" out of 5 stars", "").replace(" stars over the past 12 months", "").replace(" stars", "")
        elif (region == "de"):
            self.rating = rating.replace(" von 5 Sternen", "").replace(",", ".").replace(" stars", "")
        elif (region == "co.jp"):
            self.rating = rating.replace("（星5つ中）", "").replace("5つ星のうち ", "").replace("星5つ中の星", "").replace("5つ星のうち", "").replace("つ", "").replace(" stars", "")
        elif (region == "fr"):
            self.rating = rating.replace(" étoiles sur 5", "").replace(" sur 5 étoiles", "").replace(",", ".").replace(" stars", "")
        elif (region == "es"):
            self.rating = rating.replace(" de un máximo de 5 estrellas", "").replace(" estrellas de 5", "").replace(" sur 5 étoiles", "").replace(" de 5 estrellas", "").replace(",", ".").replace(" stars", "")
        elif (region == "it"):
            self.rating = rating.replace(" su 5 stelle", "").replace(",", ".").replace(" sur 5 étoiles", "").replace(" stars", "")
        return self.rating

    def formatSellerRatingCount(self, ratingcount, region):
        if(region == "com" or region == "co.uk" or region == "ca"):
            self.ratingcount = ratingcount.replace("(", "").replace(" total ratings)", "").replace(",", "").strip()
        elif (region == "de"):
            self.ratingcount = ratingcount.replace("Bewertungen insgesamt", "").replace(".", "").strip()
        elif (region == "co.jp"):
            self.ratingcount = ratingcount.replace("件の評価", "").replace(",", "").strip()
        elif (region == "fr"):
            self.ratingcount = ratingcount.replace("évaluations totales", "").replace(" ", "").replace(".", "").strip()
        elif (region == "es"):
            self.ratingcount = ratingcount.replace("valoraciones totales", "").replace(" ", "").replace(".", "").strip()
        elif (region == "it"):
            self.ratingcount = ratingcount.replace("valutazioni totali", "").replace(" ", "").replace(".", "").strip()
        else:
            pass

        return self.ratingcount

    def formatCondition(self, condition, region):
        if (region == "com"):
            self.condition = condition.replace("Certified Refurbished", "Refurbished")
        elif (region == "de"):
            self.condition = condition.replace("Neu", "New").replace("Gebraucht-Wieneu", "UsedLikeNew").replace("Gebraucht-Sehrgut", "UsedVeryGood").replace("Gebraucht-Gut", "UsedGood").replace("Gebraucht-Akzeptabel", "UsedAcceptable")
        elif (region == "co.jp"):
            self.condition = condition.replace("中古品-ほぼ新品", "UsedLikeNew").replace("中古品-非常に良い", "UsedVeryGood").replace("中古品-良い", "UsedGood").replace("中古品-可", "UsedAcceptable").replace("新品", "New")
        elif (region == "fr"):
            self.condition = condition.replace("Neuf", "New").replace("D'occasion-Commeneuf", "UsedLikeNew").replace("D'occasion-Trèsbon", "UsedVeryGood").replace("D'occasion-Bon", "UsedGood").replace("D'occasion-Acceptable", "UsedAcceptable").replace("Decollection-Acceptable", "CollectibleAcceptable").replace(" ", "")
        elif (region == "es"):
            self.condition = condition.replace("Nuevo", "New").replace("De2ªmano-Comonuevo", "UsedLikeNew").replace("De2ªmano-Muybueno", "UsedVeryGood").replace("De2ªmano-Bueno", "UsedGood").replace("De2ªmano-Aceptable", "UsedAcceptable")
        elif (region == "it"):
            self.condition = condition.replace("Nuovo", "New").replace("Usato-Comenuovo", "UsedLikeNew").replace("Usato-Ottimecondizioni", "UsedVeryGood").replace("Usato-Buonecondizioni", "UsedGood").replace("Usato-Condizioniaccettabili", "UsedAcceptable").replace("Ricondizionato-Rimessoanuovo", "CollectibleLikeNew")
        elif (region == "ca"):
            self.condition = condition.replace("OpenBox-LikeNew", "UsedLikeNew").replace("OpenBox-VeryGood", "UsedVeryGood").replace("OpenBox-Good", "UsedGood").replace("OpenBox-Acceptable", "UsedAcceptable").replace("-", "").replace(" ", "")
        return self.condition

    def formatPositive(self, positive, region):
        if (region == "com" or region == "co.uk" or region == "ca"):
            self.sellerpositive = positive.replace("positive", "").replace("%", "").strip()
        elif (region == "de"):
            self.sellerpositive = positive.replace("positiv", "").replace("%", "").strip()
        elif (region == "co.jp"):
            self.sellerpositive = positive.replace("%の高い評価", "").strip()
        elif (region == "fr"):
            self.sellerpositive = positive.replace("positif", "").replace("%", "").strip()
        elif (region == "es"):
            self.sellerpositive = positive.replace("positivas", "").replace("%", "").strip()
        elif (region == "it"):
            self.sellerpositive = positive.replace("positivo", "").replace("%", "").strip()
        return self.sellerpositive

    def formatReviewCount(self, reviewcount, region):
        if (region == "com" or region == "co.uk" or region == "ca"):
            self.reviewcount = reviewcount.replace(" customer reviews", "").replace(" customer review", "").replace(" reviews from the U.S.", "").replace(",", "")
        elif(region == "de"):
            self.reviewcount = reviewcount.replace("Rezension aus den USA.", "").replace(" Kundenrezensionen", "").replace("Kundenrezension", "").replace(",", "").strip()
        elif (region == "co.jp"):
            self.reviewcount = reviewcount.replace("件のカスタマーレビュー", "").replace(",", "")
        elif (region == "fr"):
            self.reviewcount = reviewcount.replace(" commentaire client", "").replace(" commentaires client", "").replace(",", "")
        elif (region == "es"):
            self.reviewcount = reviewcount.replace(" opiniones de EE. UU.", "").replace(" opiniones de clientes", "").replace(",", "")
        elif (region == "it"):
            self.reviewcount = reviewcount.replace(" recensioni clienti", "").replace(",", "")
        else:
            pass

        return self.reviewcount

    def replace_date(self, region, date):
        if (region == "co.uk"):
            date = date.replace("March", "Mar").replace("April", "Apr").replace("Sept", "Sep").replace("December", "Dec").replace("July", "Jul")
        elif (region == "de"):
            date = date.replace("Januar", "Jan").replace("Februar", "Feb").replace("März", "Mar").replace("April", "Apr").replace("Mai", "May").replace("Juni", "Jun").replace("Juli", "Jul").replace("August", "Aug").replace("September", "Sep").replace("Oktober", "Oct").replace("November", "Nov").replace("Dezember", "Dec")
        elif (region == "fr"):
            date = date.replace("janvier", "Jan").replace("février", "Feb").replace("mars", "Mar").replace("avril", "Apr").replace("mai", "May").replace("juin", "Jun").replace("juillet", "Jul").replace("août", "Aug").replace("septembre", "Sep").replace("octobre", "Oct").replace("novembre", "Nov").replace("décembre", "Dec")
        elif (region == "es"):
            date = date.replace("de enero de", "Jan").replace("de febrero de", "Feb").replace("de marzo de", "Mar").replace("de abril de", "Apr").replace("de mayo de", "May").replace("de junio de", "Jun").replace("de julio de", "Jul").replace("de agosto de", "Aug").replace("de septiembre de", "Sep").replace("de octubre de", "Oct").replace("de noviembre de", "Nov").replace("de diciembre de", "Dec")
        elif (region == "it"):
            date = date.replace("gennaio", "Jan").replace("febbraio", "Feb").replace("marzo", "Mar").replace("aprile", "Apr").replace("maggio", "May").replace("giugno", "Jun").replace("luglio", "Jul").replace("agosto", "Aug").replace("settembre", "Sep").replace("ottobre", "Oct").replace("novembre", "Nov").replace("dicembre", "Dec")
        elif (region == "ca"):
            date = date.replace("January", "Jan").replace("February", "Feb").replace("March", "Mar").replace("April", "Apr").replace("June", "Jun").replace("July", "Jul").replace("Sept", "Sep")
        return date

    def formatDate(self, date, region):
        if (region == "com"):
            # self.date = datetime.datetime.strptime("/".join(date.replace(",", '').split(' ')), "%B/%d/%Y")
            self.date = str(datetime.datetime.strptime("/".join(date.replace("on ", "").replace(",", '').replace("(", "").replace(")", "").split(' ')), "%B/%d/%Y")).split(" ")[0].replace("-", "/")
        elif (region == "co.uk"):
            en = ['Jan', 'Feb', 'Mar', 'April', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
            us = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            self.date = str(datetime.datetime.strptime("/".join(self.replace_date(region, date.replace("on ", "").replace(".", "")).split(' ')), "%d/%b/%Y")).split(" ")[0].replace("-", "/")
        elif (region == "de"):
            de = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember']
            us = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            self.date = str(datetime.datetime.strptime("/".join(self.replace_date(region, date.replace(".", "").replace("(", "").replace(")", "")).split(' ')), "%d/%b/%Y")).split(" ")[0].replace("-", "/")
        elif (region == "co.jp"):
            self.date = str(datetime.datetime.strptime("/".join(self.replace_date(region, date.replace(".", "").replace("(", "").replace(")", "")).split(' ')), "%d/%b/%Y")).split(" ")[0].replace("-", "/")
        elif (region == "fr"):
            fr = ['janvier','février','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','décembre']
            us = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            self.date = str(datetime.datetime.strptime("/".join(self.replace_date(region, date.replace(".", "").replace("(", "").replace(")", "")).split(' ')), "%d/%b/%Y")).split(" ")[0].replace("-", "/")
        elif (region == "es"):
            es = ['de enero de', 'de febrero de', 'de marzo de', 'de abril de', 'de mayo de', 'de junio de', 'de julio de', 'de agosto de', 'de septiembre de', 'de octubre de', 'de noviembre de', 'de diciembre de']
            us = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            self.date = str(datetime.datetime.strptime("/".join(self.replace_date(region, date.replace(".", "").replace("(", "").replace(")", "")).split(' ')), "%d/%b/%Y")).split(" ")[0].replace("-", "/")
        elif (region == "it"):
            it = ['gennaio', 'febbraio', 'marzo', 'aprile', 'maggio', 'giugno', 'luglio', 'agosto', 'settembre', 'ottobre', 'novembre', 'dicembre']
            us = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            self.date = str(datetime.datetime.strptime("/".join(self.replace_date(region, date.replace(".", "").replace("(", "").replace(")", "")).split(' ')), "%d/%b/%Y")).split(" ")[0].replace("-", "/")
        elif (region == "ca"):
            self.date = str(datetime.datetime.strptime("/".join(self.replace_date(region, date.replace(".", "").replace(",", '').replace("(", "").replace(")", "")).split(' ')), "%b/%d/%Y")).split(" ")[0].replace("-", "/")
        return self.date

    def formatReviewDate(self, date, region):
        if (region == "com"):
            # self.date = datetime.datetime.strptime("/".join(date.replace(",", '').split(' ')), "%B/%d/%Y")
            self.date = str(datetime.datetime.strptime("/".join(date.replace("on ", "").replace(",", '').replace("(", "").replace(")", "").split(' ')), "%B/%d/%Y")).split(" ")[0].replace("-", "/")
        elif (region == "co.uk"):
            en = ['Jan', 'Feb', 'Mar', 'April', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
            us = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            self.date = str(datetime.datetime.strptime("/".join(date.replace("on ", "").replace(".", "").split(' ')), "%d/%B/%Y")).split(" ")[0].replace("-", "/")
        elif (region == "de"):
            de = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember']
            us = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            self.date = str(datetime.datetime.strptime("/".join(self.replace_date(region, date.replace("am ", "").replace(".", "").replace("(", "").replace(")", "")).split(' ')), "%d/%b/%Y")).split(" ")[0].replace("-", "/")
        elif (region == "co.jp"):
            self.date = str("/".join(date.replace("年", " ").replace("月", " ").replace("日", "").split(' ')))
        elif (region == "fr"):
            fr = ['janvier','février','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','décembre']
            us = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            self.date = str(datetime.datetime.strptime("/".join(self.replace_date(region, date.replace("le ", "").replace(".", "").replace("(", "").replace(")", "")).split(' ')), "%d/%b/%Y")).split(" ")[0].replace("-", "/")
        elif (region == "es"):
            es = ['de enero de', 'de febrero de', 'de marzo de', 'de abril de', 'de mayo de', 'de junio de', 'de julio de', 'de agosto de', 'de septiembre de', 'de octubre de', 'de noviembre de', 'de diciembre de']
            us = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            self.date = str(datetime.datetime.strptime("/".join(self.replace_date(region, date.replace("el ", "").replace(".", "").replace("(", "").replace(")", "")).split(' ')), "%d/%b/%Y")).split(" ")[0].replace("-", "/")
        elif (region == "it"):
            it = ['gennaio', 'febbraio', 'marzo', 'aprile', 'maggio', 'giugno', 'luglio', 'agosto', 'settembre', 'ottobre', 'novembre', 'dicembre']
            us = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            self.date = str(datetime.datetime.strptime("/".join(self.replace_date(region, date.replace("il ", "").replace(".", "").replace("(", "").replace(")", "")).split(' ')), "%d/%b/%Y")).split(" ")[0].replace("-", "/")
        elif (region == "ca"):
            self.date = str(datetime.datetime.strptime("/".join(date.replace("on ", "").replace(".", "").replace(",", '').replace("(", "").replace(")", "").split(' ')), "%B/%d/%Y")).split(" ")[0].replace("-", "/")
        return self.date

    def formatImage(self , image):
        images = []
        items = image.split("//")
        images.append(items[0])
        images1 =[]
        images1.append(items[1].split("/")[0])
        images1.append(items[1].split("/")[1])
        images1.append(items[1].split("/")[2])
        item = []
        item1 = items[1].split("/")[3].split(".")[0]
        item.append(item1)
        item2 = items[1].split("/")[3].split(".")[2]
        item.append(item2)
        img1 = '.'.join(item)
        images1.append(img1)
        img2 = '/'.join(images1)
        images.append(img2)
        return '//'.join(images)

    def formatType(self, type):
        if (type == "Positive" or type == "Positiv" or type == "肯定的" or type == "Positive" or type == "Positivo" or type == "Positivo"):
            return "Positive"
        if (type == "Neutral" or type == "Neutral" or type == "普通" or type == "Neutre" or type == "Neutral" or type == "Neutro"):
            return "Neutral"
        if (type == "Negative" or type == "Negativ" or type == "否定的" or type == "Négative" or type == "Negativo" or type == "Negativo"):
            return "Negative"
        if (type == "Count" or type == "Anzahl" or type == "数" or type == "Décompte" or type == "Recuento" or type == "Conteggio"):
            return "Count"

    def formatUrl(self, url, website):
        if (website == "sina"):
            if ("?" in url):
                url = url.split("?")[0]
        elif (website == "tencent"):
            if ("?" in url):
                url = url.split("?")[0]
        return url

    def formatSinaKeywords(self, keywords, website):
        if (website == "sina"):
            return keywords.replace(u"新浪游戏", "").replace(u"高清图片", "").replace(",", " ").strip().replace(" ", ",")

    def formatTime(self, time, website):
        if (website == "sina"):
            return time.split("+")[0].replace("T", " ").strip()