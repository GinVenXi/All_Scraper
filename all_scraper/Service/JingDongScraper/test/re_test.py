# #-*-coding:utf-8*-
# import re
#
# def main():
#     bwx="a-bike自行车"
#     # J=re.sub(r'\W*','',bwx)
#     # J=re.sub(r' [\u4e00-\u9fa5]*','',bwx)
#     # J=re.match(r'[\u4e00-\u9fa5]\W*',bwx)
#     # J=re.compile('[\u4e00-\u9fa5]\W*')
#     # print J.groups()
#     J=re.sub(r'\w*','','a-bike自行车')
#     # J=re.sub(r' [\u4e00-\u9fa5] ','','a-bike自行车')
#     print J
#
#
#
# if __name__ == '__main__':
#   main()

# -*- coding: utf-8 -*-
import re
s = "a/bike自行车/"
r = re.sub("[A-Za-z0-9\[\`\~\!\@\-\.\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\！\@\#\\\&\*\%]", "", s)
print r