## 1.4 回到Python：决策与控制

### 条件

#### Python关系运算符
运算符             关系
<                   小于
<=                 小于等于
==                 等于【两个等号】   
!=                   不等于
>                    大于
>=                  大于等于
```
>>>from nltk.book import *
print (sent7)['Pierre', 'Vinken', ',', '61', 'years', 'old', ',', 'will', 'join', 'the', 'board', 'as', 'a', 'nonexecutive', 'director', 'Nov.', '29', '.']
print ([w for w in sent7 if len(w)<4]
[',', '61', 'old', ',', 'the', 'as', 'a', '29', '.']
print ([w for w in sent7 if len(w)<=4])[',', '61', 'old', ',', 'will', 'join', 'the', 'as', 'a', 'Nov.', '29', '.']
print ([w for w in sent7 if len(w)==4])
['will', 'join', 'Nov.']
print ([w for w in sent7 if len(w)!=4])
['Pierre', 'Vinken', ',', '61', 'years', 'old', ',', 'the', 'board', 'as', 'a', 'nonexecutive', 'director', '29', '.']
```

#### 一些词比较运算符
|函数 |含义|
|-------------------|-----------------------------------|
|s.startswith(t)|测试s是否以t开头|
|s.endswith(t)|测试s是否以t结尾|
|t in s|测试s是否包含t|
|s.islower()|测试s中所有字符是否都是小写字母|
|s.isupper()|测试s中所有字符是否都是大写字母|
|s.isalpha()|测试s中所有字符是否都是字母|
|s.isalnum()|测试s中所有字符是否都是字母或数字|
|s.isdigit()|测试s 中所有字母是否都是数字|
|s.istitle()|测试s是否首字母大写（s中所有的词都首字母大写）|
```
>>>print (sorted([w for w in set(text1)if w.endswith('ableness')]))
[u'comfortableness', u'honourableness', u'immutableness', u'indispensableness', u'indomitableness', u'intolerableness', u'palpableness', u'reasonableness', u'uncomfortableness']
print (sorted([term for term in set(text4) if 'gnt'in term]))
[u'Sovereignty', u'sovereignties', u'sovereignty']
print (sorted([item for item in set(text6)if item.istitle()]))
[u'A', u'Aaaaaaaaah', u'Aaaaaaaah', u'Aaaaaah', u'Aaaah', u'Aaaaugh', u'Aaagh', u'Aaah', u'Aaauggh', u'Aaaugh', u'Aaauugh', u'Aagh', u'Aah', u'Aauuggghhh',]
print (sorted([item for item in set(sent7)if item.isdigit()]))
['29', '61']
```

#### 练习
```
print (sorted([w for w in set(text7)if '-'in w and 'index'in w]))【text7中有‘-’以及‘index’的单词】
[u'Stock-index', u'index-arbitrage', u'index-fund', u'index-options', u'index-related', u'stock-index']
print (sorted([wd for wd in set(text3)if wd.istitle()and len(wd)>10]))【text3中首字母大写且长度大于10的单词】
[u'Abelmizraim', u'Allonbachuth', u'Beerlahairoi', u'Canaanitish', u'Chedorlaomer', u'Girgashites', u'Hazarmaveth', u'Hazezontamar', u'Ishmeelites', u'Jegarsahadutha', u'Jehovahjireh', u'Kirjatharba', u'Melchizedek', u'Mesopotamia', u'Peradventure', u'Philistines', u'Zaphnathpaaneah']
print(sorted([w for w in set(sent7)if not w.islower()]))【sent7中所有非小写的单词】
[',', '.', '29', '61', 'Nov.', 'Pierre', 'Vinken']
print (sorted([t for t in set(text2)if 'cie'in t or 'cei'in t]))【text2中包含cie或是cei的单词】
[u'ancient', u'ceiling', u'conceit', u'conceited', u'conceive', u'conscience', u'conscientious', u'conscientiously', u'deceitful', u'deceive', u'deceived', u'deceiving', u'deficiencies', u'deficiency', u'deficient', u'delicacies', u'excellencies', u'fancied', ]
```
#### 对每个元素进行操作

[f(w) for....] 例子 [len(w) for w in text1]
[w.f() for...] 例子 [w.upper() for w in text1]
```
>>> len(text1)
260819
>>> len(set(text1))
19317
>>> len(set([word.lower() for word in text1]))
17231
>>> len(set([word.lower() for word in text1 if word.isalpha()]))
16948
>>>
```
#### 嵌套代码块
```
>>> word='cat'
>>> if len(word)<5:
...     print 'word length is less than 5'
...
word length is less than 5
>>>
```
if语句为控制结构，其控制缩进块中的代码是否运行
另一控制结构为for循环。
```
>>>for word in ['Call','me','Ishmael','.']:
    print word
Call
me
Ishmael
.
```
#### 条件循环
结合if语句与for语句
```
>>>sent1=['Call','me','Ishmael','.']
for xyzzy in sent1:
    if xyzzy.endswith('l'):
        print xyzzy
Call
Ishmael
```
添加elif（else if）语句与else语句
```
>>>sent1=['Call','me','Ishmael','.']
for token in sent1:
    if token.islower():【四个空格】
        print token, 'is a lowercase word'【逗号意为在同一行输出】【八个空格】
    elif token.istitle():
        print token,'is a titilecase word'
    else:
        print token,'is a punctuation'
Call is a titilecase word
me is a lowercase word
Ishmael is a titilecase word
. is a punctuation
>>>
```
```
tricky=sorted([w for w in set(text2) if 'cie'in w or 'cei' in w])
for word in tricky:
    print  word,
ancient ceiling conceit conceited conceive conscience conscientious conscientiously deceitful deceive deceived deceiving deficiencies deficiency deficient delicacies excellencies fancied insufficiency insufficient legacies perceive perceived perceiving prescience prophecies receipt receive received receiving society species sufficient sufficiently undeceive undeceiving
>>>
```
