def hello_name(name):
  return "Hello " + name + "!"
print hello_name("Meme God")


def make_abba(a, b):
  return a + b + b + a
print make_abba(" Dank ", " Meme ")


def make_tags(tag, word):
  return '<' +tag+ '>' +word+ '</' +tag+ '>'
print make_tags("i", "meme")

def make_out_word(dank, meme):
  return out[:2] + word + out[2:]
print make_out_word()


def extra_end(str):
  return str[-2:] * 3
print extra_end(MEME)

def first_two(str):
  if len(str) <= 2:
    return str
  return str[:2]
print first_two(dank meme)


def first_half(str):
  return str[:len(str)/2]
print first_half(meme god)


def without_end(str):
  return str[1:-1]
print without_end(ayy lmao)


def combo_string(a, b):
  if len(a) > len(b):
    return b + a + b
  return a + b + a
print combo_string(meme, dank)


def non_start(a, b):
  return a[1:] + b[1:]
print non_start(6, 9)


def left2(str):
  return str[2:] + str[:2]
print left2(meme)
