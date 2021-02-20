# 加密: md5  sha1  sha256  sha512 ...
import hashlib

# md5是不可逆
msg = 'hello word'
# 进行加密，以utf-8的编码格式
md5 = hashlib.md5(msg.encode('utf-8'))
# 将加密内容转捍卫16进制
md5_16 = md5.hexdigest()
print('md5: ', md5_16)  # 32位

# sha1加密
sha1 = hashlib.sha1(msg.encode('utf-8')).hexdigest()
print('sha1: ', sha1)  # 40位

# sha256加密
sha256 = hashlib.sha256(msg.encode('utf-8')).hexdigest()
print('sha256: ', sha256)  # 64位

# sha512加密
sha512 = hashlib.sha512(msg.encode('utf-8')).hexdigest()
print('sha512: ', sha512)
