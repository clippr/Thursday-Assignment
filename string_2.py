def double_char(str):
  end = ''
  for char in str:
    end += char * 2
  return end
print double_char('maymay')


def count_hi(str):
  count = 0
  for i in range(len(str)-1):
    if str[i:i+2] == 'hi':
      count += 1
  return count
print count_hi("meme, hi, meme, hi, hi, meme")


def cat_dog(str):
  count_cat = 0
  count_dog = 0
  for i in range(len(str)-2):
    if str[i:i+3] == 'dog':
      count_dog += 1
    if str[i:i+3] == 'cat':
      count_cat += 1
  return count_cat == count_dog
print cat_dog("catdog")


def count_code(str):
  num = 0
  for i in range(0, len(str)-3):
    if str[i:i+2] == 'co' and str[i+3] == 'e':
      num += 1
  return num
print count_code("may may code meme code code")


def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return a[-(len(b)):] == b or a == b[-(len(a)):]
print end_other("meme", "meme")


def xyz_there(str):
  for i in range(len(str)):
    if str[i] != '.' and str[i+1:i+4] == 'xyz':
      return True
  if str[0:3] == 'xyz':
    return True
  return False
