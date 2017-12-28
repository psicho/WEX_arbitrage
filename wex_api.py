import sys
import time
import requests
import re
import urllib.request
import json
import time


# Аутентификация ВКонтакте
# session = vk.AuthSession(app_id=MyvkData.app_id,user_login=MyvkData.login, user_password=MyvkData.get_password(), scope='market, photos, group, groups, wall')
# vkapi = vk.API(session)
##########################

# Данные по группе

#################################

url_base = []

ticker = 'https://wex.nz/api/3/ticker/'
depth = 'https://wex.nz/api/3/depth/'

curriences = ['btc_usd','btc_rur', 'btc_eur', 'ltc_usd', 'ltc_rur', 'ltc_eur', 'dsh_btc', 'dsh_usd', 'dsh_rur', 'dsh_eur', 'dsh_ltc', 'dsh_eth', 'eth_btc', 'eth_usd', 'eth_eur', 'eth_ltc', 'eth_rur', 'bch_usd', 'bch_btc', 'bch_rur', 'bch_eur', 'bch_ltc', 'bch_eth', 'bch_dsh', 'zec_btc', 'zec_usd']
print(len(curriences))

# response = requests.get(linkapi + curriences[0])
# json_data = json.loads(response.text)
# print(json_data['btc_usd']['buy'], json_data['btc_usd']['sell'])

linkapi = ticker
# linkapi = depth

# Выгрузка валютных пар по одной
'''
for i in curriences:
     response = requests.get(linkapi + i)
     json_data = json.loads(response.text)
     j = json.dumps(json_data)
     print(json_data[i])
'''

# Общая выгрузка
def current(cur, linkapi = 'https://wex.nz/api/3/depth/'):
     n = 1
     for i in curriences:
          if n < len(curriences):
               linkapi += i + '-'
          else:
               linkapi += i + '?ignore_invalid=1'
          n += 1

     response = requests.get(linkapi)
     json_data = json.loads(response.text)
     j = json.dumps(json_data)
     # print(len(json_data))
     # print(json_data[cur]['asks'][0], json_data[cur]['bids'][0])
     return json_data[cur]['asks'][0][0], json_data[cur]['bids'][0][0]

# Выбор пар для арбитража

def select(eqvIn, curIn, eqvOut, curOut, curriences = curriences):
     valite = ['rur', 'usd', 'eur']
     curIn = curIn.split("_")
     for i in curriences:
          if i
     pass


n = 6 # количество арбитражируемых пар
cur = 'btc_usd' # текущая пара для арбитража
nal = 100 # текущая сумма инвестиций

nal1 = current(cur)
nal1 = nal/nal1[0]
print(nal1)

for i in range(n):
     bit = current(cur)
     print(bit)
     # curriences[i]


# page = html.fromstring(response.text)

# for i in range(1, 4):
#      link = 'http://rings.su/catalog?goods_search_field_id=7&per_page=100&page=' + str(i)
#      print(link)
#      response = requests.get(link)
#      page = html.fromstring(response.text)
#
#      linker = '//tr/td/div/h6/a/@href'
#      linker = '//tr/td/div/h6/a/@href'
#      link1 = page.xpath(linker)
#      url_base.extend(link1)
#
#
# base = []
# base_item = []
#
# for link in url_base:
#      response = requests.get(link)
#      page = html.fromstring(response.text)
#
#      base_item.append(link)
#
#      title = '//tr/td[1]/div/div[1]/h1/text()'
#      title1 = page.xpath(title)
#      base_item.append(title1[0])
#
#      photo = '//tr/td[1]/div[3]/div/a/@href'
#      photo = page.xpath(photo)
#      base_item.append(photo)
#
#      price = '//tr[1]/td[1]/span[1]/span/span/span[1]/text()'
#      price = page.xpath(price)
#      base_item.append(price[0])
#
#      sklad = '//tr[1]/td[1]/div/div[1]/h5/text()'
#      sklad = page.xpath(sklad)
#      base_item.append(sklad[0])
#
#      description = '//tr/td[1]/div/div[2]/div[2]/div[2]/text()'
#      description = page.xpath(description)
#      base_item.append(description[0].strip())
#
#      base.append(base_item.copy())
#      base_item.clear()
#
#      print(len(base))
#      json.dump(base, open("base.json", "w"))
#
# f = open('log.txt', 'w')
# f.close()
#
# while True:
#     try:
#         # Аутентификация ВКонтакте
#         session = vk.AuthSession(app_id=MyvkData.app_id,user_login=MyvkData.login, user_password=MyvkData.get_password(), scope='market, photos, group, groups, wall')
#         vkapi = vk.API(session)
#         ##########################
#
#         with open ("base.json", "r") as f:
#             reader = json.load(f)
#             # print(len(reader))
#             # print(reader[0])
#             # break
#
#             for i in range(start, len(reader)):   #maximum
#                 tags = str()
#
#                 #print ('id', reader[i]["id"])
#                 #print()
#                 reader[i][1] = str(reader[i][1]).replace('\n', '').strip()
#                 # print ("title", reader[i][1])
#                 #print()
#                 # print (reader[i]["url"])
#                 reader[i][5] = str(reader[i][5]).strip().replace('<br />', '\n').replace('<b>', '').replace('</b>', '')
#                 try:
#                     result = re.search(r'(\(<a href="http://35photo.ru/.+" class="ot-anchor">35photo.ru/.+</a>\).+)', reader[i][5])
#                     reader[i][5] = (str(reader[i][5]).replace(result.group(1), '').strip())
#                 except:
#                     pass
#                 try:
#                     result = re.search(r'(Photo source:.+)', reader[i][5])
#                     reader[i][5] = (str(reader[i][5]).replace(result.group(1), '').strip())
#                 except:
#                     pass
#                 try:
#                     result = re.search(r'(Source photo:.+)', reader[i][5])
#                     reader[i][5] = (str(reader[i][5]).replace(result.group(1), '').strip())
#                 except:
#                     pass
#
#                 image_list = list()
#
#                 image_list = list(reader[i][2])
#
#                 tagsis = str(reader[i][1]).split(' ')
#                 for t in tagsis:
#                     if len(t) > 3:
#                         tags = tags + '#' + t +' '
#                         tags = tags.replace('-','_').replace('"', '').replace("'", '').replace(".", '')
#
#                 #print('tags', tags)
#
#                 # Размещение фотографии в альбоме
#
#                 attach_photo = '' # Список для заполнения фотографиями размещаемого туристического места.
#                 p = 0
#                 for image in image_list:
#                     # print('image', image)
#
#                     # Меняем размер изображения (при необходимости)
#                     try:
#                         try:
#                             # print('image',image)
#                             image_size.size(image)
#                         except:
#                             image = str(image).replace('https', 'http')
#                             # print('image', image)
#                             image_size.size(image)
#                     except:
#                         print(i, 'Ошибка изменения размера')
#                         continue
#
#                     product_photo = vkapi.photos.getUploadServer(group_id=group_number, album_id=albom_id)
#                     # print('product_photo', product_photo)
#                     upload_url = product_photo['upload_url']
#
#                     img = {'photo': ('img.jpg', open(r'img/img.jpg', 'rb'))}
#
#                     response = requests.post(upload_url, files=img)
#                     result = json.loads(response.text)
#                     server = result['server']
#                     photos_list = result['photos_list']
#                     hash = result['hash']
#                     aid = result['aid']
#                     # print('result', result)
#
#                     photo_save = vkapi.photos.save(album_id=albom_id, group_id=group_number, photos_list=photos_list,
#                                                    server=server, hash=hash, aid=aid,
#                                                    caption=reader[i][1] + '\n' + reader[i][0] + '\n\nЦена: ' + reader[i][3] + ' руб.' + '\n\n' + reader[i][5] + ' ' + reader[i][0] + '\n\n Большой выбор украшений на сайте http://rings.su' + '\n' + tags)
#                     # print(photo_save)
#
#                     if p < 1:
#                         attach_photo = attach_photo + 'photo' + str(photo_save[0]['owner_id']) + '_' + str(photo_save[0]['pid'])
#                     else:
#                         attach_photo = attach_photo + ',' + 'photo' + str(photo_save[0]['owner_id']) + '_' + str(photo_save[0]['pid'])
#                     p = p + 1
#
#                 vkapi.wall.post(owner_id=-1*int(group_number), from_group=1, message=reader[i][1] + '\n' + reader[i][0] + '\n\nЦена: ' + reader[i][3] + ' руб.' + '\n\n' + reader[i][5]
#                                 + ' ' + reader[i][0] + '\n\n Большой выбор украшений на сайте http://rings.su' + '\n' + tags,
#                                 attachments=attach_photo, signed=0, lat='', long='', mark_as_ads=0, scope='wall, groups, photos')
#
#                 localtime = time.asctime(time.localtime(time.time()))
#                 print(i, 'Украшение размещено - осталось:' + str(len(reader)-1-i), localtime)
#                 print('Ждем 30 минут')
#                 print()
#                 with open('log.txt', 'a') as f:
#                     f.write(str(i) + ' - ' + str(reader[i][1]) + ' статус: Размещён ' + str(localtime) + '\n')
#                 if i == len(reader)-1:
#                     i = 0
#                     start = 0
#                     time.sleep(1800)
#                     break
#                 time.sleep(1800)
#     except:
#         print()
#         print('<< Перезапуск >>, Ждем 30 минут')
#         print()
#         if i == len(reader)-1:
#             i = 0
#         start = i + 1
#         time.sleep(1800)
#         continue
#
# print('Все позиции сайта были размещены')
