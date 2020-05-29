import re

with open("C:/Users/kakos/Downloads/stefanidakis2002.txt", "r", encoding="utf-8") as fd0:
    text = fd0.read()

    #eksagogi kai print titlou
    repx = re.compile(r"<title>(.+?)</title>")
    m=repx.search(text)
    print(m.group(1))

    #apalifi apo sxolia
    repx2= re.compile(r"<!.+?>")
    new_text = repx2.sub("", text)

    #apalifi <script><style>
    repx3 = re.compile(r"(<script.+?</script>)|(<style.+?</style>)"re.DOTALL)
    new_text2 = repx3.sub("",new_text)

    #eksagogi kai print <a>
    repx4= re.compile(r"<a(.+?)</a>")
    for m in repx4.finditer(new_text2):
      print(m.group(1))

    #apalifi olon ton tags
    repx5 = re.compile(r"<.+?>")
    new_text3 = repx5.sub("", new_text2)

    #Lexicon gia antikatastasi
    HTMLentities = {"&amp;": "&", "&gt;": ">", "&lt;": "<", "&nbsp;": " "}

    #callback function
    def rep1(m):
        if m.group(1) == "&amp;":
            return HTMLentities[m.group(1)]
        elif m.group(1) == "&gt;":
            return HTMLentities[m.group(1)]
        elif m.group(1) == "&lt;":
            return HTMLentities[m.group(1)]
        elif m.group(1) == "&nbsp;":
            return HTMLentities[m.group(1)]


    repx6= re.compile(r"(&amp;|&gt;|&lt;|&nbsp;)")
    new_text4 = repx6.sub(rep1,new_text3)

    #metatropi whitespace se 1 keno
    repx7= re.compile(r"\s+")
    new_text5 = repx7.sub(" ",new_text4)
    print(new_text5)
    
with open("output.txt","w",encoding="utf-8") as fd1:
    fd1.write(new_text5)
    
