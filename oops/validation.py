import re
# a="hello world hello"
# print(re.sub('hello','HELLO',a,2))
# print(re.findall('hello',a))
# print(re.search('hello',a))
# print(re.search('z',a))


# a='sadf122224ASSSSDF'
# print(re.search('sadf',a))
# print(re.search('[a-z]',a))
# print(re.search('[A-Z]',a))
# print(re.search('[A-z]',a))
# print(re.search('[abc]',a))
# print(re.search('a..',a))
# print(re.search('f.*',a))
# print(re.search('f.+',a))
# print(re.search('d.*',a))
# print(re.search('d.+',a))
# print(re.search('s.?',a))
# print(re.search('f.*',a))

# print(re.search('[a-z].*[A-Z]',a))
# print(re.search('[a-z].*[0-9].[A-Z].*',a))
# print(re.search('[a-m].*[0-9].[A-Z].*',a))
# print(re.search('[a-m0-9A-z].*[0-9].[A-Z].*',a))


# a=input('enter your email : ')
# if re.search('[a-z].{}.*@gmail.com$',a):
#     print('valid')
# else:
#     print ('invalid')     



a=input('enter your password : ')
if len(a)>=8 and re.search('[a-zA-Z].[0-9].*',a):
    print('valid')
else:
    print ('invalid')     

