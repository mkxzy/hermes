#!/usr/bin/python3
from datatool import Boktour
from xml.etree.ElementTree import parse
from repository import Repository

if __name__ == "__main__":
    baseurl = "http://www.boktour.com/Service/LineService.aspx";
    username = "zouzoushijie"
    password = 'zouzou2017!'
    b = Boktour(baseurl, username, password)
    data = b.getlinetype()
    product_type = parse(data)
    connection = 'mongodb://xiezhiyan:yilvxzy@120.26.246.185:27017/';
    repo = Repository(connection);
    for item in product_type.findall('item/linetype'):
        print(item.tag, item.attrib)
        # repo.save('product_type', item.attrib)
        product = parse(b.getlongline(item.attrib['id']))
        for item in product.iterfind('channel/item'):
            print('\t'+item.find('title').text)
            item_dic = {
                'title': item.find('title').text
            }
            repo.save('longline', item_dic)