print("Weiden和Megan好美啊")
f = open("test.txt", "rb")
info = f.read()
potentials = ["big5", "gbk", "gb18030", "gb2312","UTF-8"]
# I see what's wrong: gbk and gb18030 are traditional, not simplified
# Argh this is so confusing
# UTF-8 seems to be king

for x in potentials:
    try:
        print(x + ":", info.decode(x))
    except:
        print("Encoding", x, "failed.")