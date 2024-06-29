# %%
import opencc
import re

t2s = opencc.OpenCC("t2s")

paths_of_docs = [
    "/index.md",
    "/install.md",
    "/docs/index.md",
    "/docs/updates.md",
    "/docs/technical.md",
    "/docs/discussion.md",
    "/docs/background.md",
    "/docs/statistics.md",
    "/docs/coding.md",
    "/docs/guji.md",
    "/docs/yuniversus.md",
    "/docs/joy.md",
    "/docs/tianma.md",
    "/docs/yima.md",
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
    "/learn/frequent.md",
    "/learn/frequent_tc.md",
    "/practice/root.md",
    "/practice/char.md",
    "/practice/root_light.md",
    "/practice/char_light.md",
    "/practice/root_joy.md",
    "/practice/char_joy.md",
    "/practice/char_joy_zhu.md",
    "/practice/root_wafel.md",
    "/chaifen/index.md",
    "/chaifen/light.md",
    "/chaifen/joy.md",
]

for path_of_doc in paths_of_docs:
    with open("../src/zht" + path_of_doc, mode="r", encoding="utf8") as temp:
        doc = temp.read()
    if not doc.startswith("<!-- do not translate -->"):
        pat = re.compile(
            r"((?:<!-- do not translate -->[\S\s]+?<!-- do not translate -->)|(?:`.+?`)|(?:<.+?>)|(?:[^`<>]+)|(?:[\r\n]+)|(?:[<>]))+?"
        )
        res = re.findall(pat, doc)
        res_zht = []
        for i in res:
            if i.startswith("`") or i.startswith("<"):
                res_zht.append(i)
            else:
                res_zht.append(t2s.convert(i))
        output = "".join(res_zht)
        print(path_of_doc, "translated.")
    else:
        output = doc
        print(path_of_doc, "not translated.")
    output = output.replace("/zht/", "/")
    with open("../src" + path_of_doc, mode="w", encoding="utf8") as temp:
        temp.write(output)

# %%
