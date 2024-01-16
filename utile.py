from streamlit import write
import googlesearch

try:
  from googlesearch import Search
  
except Exception:
  write(dir(googlesearch))
  
write(Search.args)
def valid(a,b,d):
  try:
    import textwrap



    text = ""
    text2 = ""
    for i in Search(a, num_results=d, advanced=True, sleep_interval=1 if d > 10 else 0):
      if b not in i.description or b == "" or b == " ":
        text += i.description if i.description != "" or i.description != " " else "aucune description trouvée ;("
        text += "  :  "
        text2 += "~"
        text2 += i.url
        text2 += "\n\n" 



    je = ""
    for i, o in zip(textwrap.wrap(text=text,width=500,break_long_words=False), text2.split("~")):
      je += i[:60 if len(i) > 60 else len(i)] + "..."if len(i) > 60 else " "
      je += "  :  "
      je += o
      je += "\n\n"


    print(je)
    return je

  except Exception:
    return "error"
