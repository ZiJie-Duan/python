# -- coding:utf-8--

word = {}

word["\n"] = "print()语法中换行"
word["\t"] = "print()语法中制表（空格键）"
word["title()"] = "title() 将字串符全部转换为首字母大写"
word["upper()"] = "upper() 将字串符全部转换为大写"
word["lower()"] = "lower() 将字串符全部转换为小写"


print(word["title()"])
