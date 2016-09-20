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
