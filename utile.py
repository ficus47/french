import os
import tkinter as tk

from googlesearch import search


def valid(a,b,c,d,e,f):
  if c.winfo_ismapped():
    import textwrap
    d = int(d.get()) if d.get().isdigit() else 7


    text = ""
    text2 = ""
    for i in search(a.get(),lang="fr", num_results=d, advanced=True, sleep_interval=1 if d > 10 else 0):
      if b.get() not in i.description or b.get() == "" or b.get() == " ":
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
    e.insert(tk.END, je)
    c.pack_forget()
    f.pack()
    e.pack()
    os.system("clear")

