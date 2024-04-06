# %%
import opencc

s2tw = opencc.OpenCC("s2tw")

# %%
# %%

paths_of_docs = [
    # "/index.md",
    "/install.md",
    "/docs/index.md",
    "/docs/updates.md",
    "/docs/statistics.md",
    "/learn/index.md",
    "/learn/division.md",
    "/learn/roots.md",
    "/learn/chars.md",
    "/learn/quick.md",
    "/learn/words.md",
    "/learn/advanced.md",
    "/learn/machine.md",
    "/learn/star.md",
    "/learn/light.md",
    "/learn/examples.md",
]

for path_of_doc in paths_of_docs:
    with open("../src" + path_of_doc, mode="r", encoding="utf8") as temp:
        doc = temp.read()
    # print(doc[:10])
    if not doc.startswith("<!-- ts -->"):
        translated_doc = []
        status = 1
        for para in doc.split("`"):
            if status:
                translated_doc.append(s2tw.convert(para))
                status = 0
            else:
                print(translated_doc)
                translated_doc.append(para)
                status = 1
        print(path_of_doc, "translated.")
    else:
        translated_doc = doc.split("`")
        print(path_of_doc, "not translated.")
    with open("../src/tw" + path_of_doc, mode="w", encoding="utf8") as temp:
        temp.write("`".join(translated_doc))


# %%
