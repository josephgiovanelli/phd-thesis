import re
import argparse

parser = argparse.ArgumentParser(description='Cleaning bibliography.')
parser.add_argument('--dropunused', help='Drop unused bib', type=bool)
parser.add_argument('--input', help='Input bib file', type=str, default="../global/refs.bib")
parser.add_argument('--logfile', help='Log file', type=str, default="../thesis.log")
args = parser.parse_args()

reg_bib = r"(@[a-zA-Z]*\{[a-zA-Z\:\/0-9,\n\s\=\{\}\-\t\.\(\)\\`\+'\"&’\*]*\}\n)"
reg_unused = r"Unused bibitem `([a-zA-Z0-9\:\/]*)'"
reg_biburl = r"[\t\s]*\b(biburl|bibsource|timestamp|doi)\b[\t\s]*\=[\s\t]*\{[a-zA-Z0-9\:\/\.\,\s\+]*\},?"
reg_title = r"\s+title\s*=\s*\{([a-zA-Z0-9\s:\-,\._!\"]*)\}"

unused_res = []
if args.dropunused:
    with open(args.logfile, "r") as f:
        logs = f.read()
        pattern = re.compile(reg_unused)
        
        for x in re.findall(pattern, logs):
            unused_res.append(x)
    unused_res = sorted(unused_res)
    print("Initial unused bibs: " + str(len(unused_res)))

refs = ""
names = {}
with open(args.input, "r", encoding="utf-8") as f:

    refs = f.read()
    
    # write the original file
    with open(args.input + ".old", "w", encoding="utf-8") as w:
        w.write(refs)

    refs = re.sub("è", "\`e", refs)
    refs = re.sub("é", "\'e", refs)
    refs = re.sub("à", "\`a", refs)
    refs = re.sub("ò", "\`o", refs)
    refs = re.sub("ù", "\`u", refs)
    refs = re.sub("ì", "\`i", refs)
    refs = re.sub(reg_biburl, "", refs)
    refs = re.sub('\n+', '\n', refs)
    pattern = re.compile(reg_bib)
    pattern_name = re.compile(reg_title)
    for x in re.findall(pattern, refs):
        for orig_name in re.findall(pattern_name, x):
            name = re.sub("\n", "", re.sub("\s", "", orig_name)).lower()
            if name in names:
                names[name].append(orig_name)
            else:
                names[name] = [orig_name]

        for y in unused_res:
            if y in x:
                unused_res.remove(y)
                refs = refs.replace(x, "")    


print("Remaining unused bibs: " + str(len(unused_res)))
print("Still to remove: " + str(unused_res))
print("Redundant papers:")
for k, v in names.items():
    if len(v) > 1:
        print(v)
