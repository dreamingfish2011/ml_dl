import re
import csv


class CleanCarData:
    def __init__(self, area):
        self.area = area

    def getBrandAndSeries(self, title):
        pattern = r'(.*?)[0-9]{4}款(.*?)$'
        repattern = re.search(pattern, title)
        brand = ''
        brand_series = ''
        if repattern:
            brandstr = repattern.group(1)
            brandstr = brandstr.split()
            brand = brandstr[0]
            if len(brandstr) > 1:
                brand_series = brandstr[1]
        return brand, brand_series

    def getDisaplacement(self, title):
        pattern = r'(.*?)([1-9]{1}[\.][0-9]{1}[T|L]|[0-9]{1,3}TSI)(.*?)$'
        disaplacement = ''
        version = ''
        repattern = re.search(pattern, title)
        if repattern:
            grouparray = repattern.groups()
            if len(grouparray) >= 2:
                disaplacement = grouparray[1]
            if len(grouparray) >= 3:
                version = str(grouparray[2]).strip()
        return disaplacement, version

    def clear_car_detail(self):
        with open("guazi_car_detail.txt", "r", encoding="utf-8-sig") as rf:
            # newline为了解决每次写入多空行问题
            with open("guazi_car_detail.csv", "w", newline='') as wf:
                csv_write = csv.writer(wf)
                csv_head = ["title", "brand", "brand_version", "is_strict", "year", "month",
                            "distance", "disaplacement", "city", "transmission", "price", "guiding_price"]
                csv_write.writerow(csv_head)
                line = rf.readline().strip()
                while line.strip():
                    content = line.strip().split("|")
                    if len(content) == 11:
                        title = content[1]
                        brand, brand_version = self.getBrandAndVersion(title)
                        is_strict = content[2]
                        year = str(content[3].strip())[0:4]
                        month = str(content[3].strip())[5:7]
                        distance = str(content[4].strip()).replace('万公里', '')
                        disaplacement = str(content[5].strip())
                        city = str(content[6].strip())
                        transmission = str(content[7].strip())
                        price = str(content[8].strip()).replace('¥', '').replace('万', '').replace('补贴后', '')
                        guiding_price = str(content[9].strip()).replace('新车指导价', '').replace('万', '') \
                            .replace('原价', '').replace('(含税)', '')
                        csv_data = [title, brand, brand_version, is_strict, year, month,
                                    distance, disaplacement, city, transmission, price, guiding_price]
                        csv_write.writerow(csv_data)
                    line = rf.readline().strip()

    def clear_car_list(self):
        filename = "guazi_car_" + self.area + ".txt"
        outputname = "guazi_car_" + self.area + ".csv"
        # newline为了解决每次写入多空行问题
        with open(outputname, "w", newline='', encoding="utf-8-sig") as wf:
            with open(filename, "r", encoding="utf-8-sig") as rf:
                csv_write = csv.writer(wf)
                csv_head = ["city", "title", "brand", "brand_series", "version", "year", "distance",
                            "disaplacement","tl_number", "price", "guiding_price", "service", "is_strict"]
                csv_write.writerow(csv_head)
                line = rf.readline().strip()
                while line.strip():
                    content = line.strip().split("|")
                    if len(content) >= 7:
                        city = self.area
                        title = content[0]
                        brand, brand_series = self.getBrandAndSeries(title)
                        disaplacement, version = self.getDisaplacement(title)
                        tl_number = disaplacement.replace('TSI','').replace('T','').replace('L','')
                        year = str(content[1].strip())[0:4]
                        distance = str(content[2].strip()).replace('万公里', '')
                        if "公里" in distance:
                            distance = float(int(distance.replace('公里', '')) / 10000)

                        service = content[3]
                        price = str(content[4].strip()).replace('¥', '').replace('万', '').replace('补贴后', '')
                        is_strict = content[5]
                        guiding_price = str(content[6].strip()).replace('新车指导价', '').replace('万', '') \
                            .replace('原价', '').replace('(含税)', '')
                        csv_data = [city, title, brand, brand_series, version, year, distance,
                                    disaplacement, tl_number,price, guiding_price, service, is_strict]
                        csv_write.writerow(csv_data)
                    if len(content) == 6:
                        print(len(content))
                        city = self.area
                        title = content[0]
                        brand, brand_series = self.getBrandAndSeries(title)
                        disaplacement, version = self.getDisaplacement(title)
                        tl_number = disaplacement.replace('TSI','').replace('T','').replace('L','')
                        year = str(content[1].strip())[0:4]
                        distance = str(content[2].strip()).replace('万公里', '')
                        if "公里" in distance:
                            distance = float(int(distance.replace('公里', '')) / 10000)
                        service = ''
                        price = str(content[3].strip()).replace('¥', '').replace('万', '').replace('补贴后', '')
                        is_strict = content[4]
                        guiding_price = str(content[5].strip()).replace('新车指导价', '').replace('万', '') \
                            .replace('原价', '').replace('(含税)', '')
                        csv_data = [city, title, brand, brand_series, version, year, distance,
                                    disaplacement,tl_number, price, guiding_price, service, is_strict]
                        csv_write.writerow(csv_data)

                        print(",".join(content))
                    line = rf.readline().strip()


if __name__ == "__main__":
    # bj12,sh13,sz17,gz16,cd
    t = CleanCarData("bj")
    t.clear_car_list()
