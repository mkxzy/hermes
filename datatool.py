from urllib import request, parse

class Boktour:
    def __init__(self, baseurl, username, password):
        self.baseurl = baseurl
        self.username = username
        self.password = password

    def getlinetype(self):
        url = self.baseurl + "?" + "USERNAME="+self.username+"&"+"USERPWD="+self.password+"&"+"action=getlinetype"
        u = request.urlopen(url)
        return u;

    def getlongline(self, line_type):
        params = {
            'USERNAME': self.username,
            'USERPWD' : self.password,
            'ACTION' : 'interface1',
            'LINETYPE_ID': line_type
        }
        querystring = parse.urlencode(params);
        url = self.baseurl + '?' + querystring
        u = request.urlopen(url)
        return u
