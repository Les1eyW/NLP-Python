## 1.2 近观Python：将文本当做词链表
### 链表

#### 定义sent1

```
>>>sent1=['Call','me','Ishmael','.'] 方括号中即为链表（list），也是Python中存储文本的方式。
>>>sent1
['Call','me','Ishmael','.'] 
>>>len(sent1)
4
```

#### 链表相加

```
>>>sent2=['or','Ish','.'] 
>>>['Call','me','Ishmael','.'] +['or','Ish','.'] 
['Call','me','Ishmael','.''or','Ish','.']
```

or
```
>>>sent1+sent2
['Call','me','Ishmael','.','or','Ish','.']
```

#### 链表追加

```
>>>sent1.append('Happy')
['Call','me','Ishmael','.','Happy']
```

#### 索引列表

Python中的文本即为词汇链表，用括号和引号的组合来表示。
表示单词[元素]在文本中出现次序的数字叫做索引，在文本名称后的方括号中写下索引，Pyhton即可表示出索引处的元素

```
>>>text4[173]
'awaken'
```

反之

```
>>>text4.index('awaken')
173
```

#### 切片：从文本中抽取片段

`>>>text5[16715:16735]`

注意：索引从0开始， sent[0]实际为word1.

```>>>sent[5:8]
['word6','word7','word8']
>>>sent[5]
'word6'
>>>sent[6]
'word7'
>>>sent[7]
'word8'
>>>sent[:3] 
```

到第三个元素为止

`>>>sent[141525:] 从第141525个元素开始`

#### 变量

`>>>sent1=['Call','me','Ishmael','.'] `

变量=表达式 Python计算右边的表达式把结果保存在变量中，这个过程叫赋值。
变量的名字按照个人偏好，必须以字母开头，可以包含数字和下划线。
```
>>>my_sent=['I','am','so','excited']
>>>feeling=my_sent[3]
>>>feeling
['excited']
```

用变量保存中间计算的步骤，使代码易懂
```
len(set(text1)
>>>vocab=set(text1)
>>>vocab_size=len(vocab)
>>>>vocab_size
19317
```

#### 字符串
`>>>name='Monty'` 【将字符串指定给变量】
`>>>name[0]` 【索引字符串】
`'M'`
```
>>>name[:4]
'Mont'
```
#### 对字符串执行乘法和加法
```
>>>name*2
'MontyMonty'
>>>name+'!'
'Monty!' 
```

#### 组合字符串

```>>>''.join(['Monty','Python'])
'Monty Pyhton'
```

#### 分割字符串
```
>>>'Monty Python'.split()
['Monty','Pyhton']
```

## 1.3 计算语言：简单的统计
```
>>> saying=['After','all','is','said','and','done','more','is','said','than','done']
>>> tokens=set(saying)
>>> tokens
set(['and', 'all', 'said', 'is', 'After', 'done', 'than', 'more']) 【句子词表】
>>> tokens=sorted(tokens)
>>> tokens
['After', 'all', 'and', 'done', 'is', 'more', 'said', 'than']【句子词表按照符号、大写单词、小写单词字母顺序排列】
>>> tokens[-2:]【排序词表倒数两个单词】
['said', 'than']
>>>
```

### 频率分布
#### 文本中每一个词项的频率
```
>>>fidst1=FreqDist(text1)【将文本中的元素按频率排序（包括标点）】
>>>fidist1
<FreqDist with 26819 outcomes>
FreqDist({u',': 18713, u'the': 13721, u'.': 6862, u'of': 6536, u'and': 6024, u'a': 4569, u'to': 4542, u';': 4072, u'in': 3916, u'that': 2982, ...})
>>>vocabulary1=fdist1.keys()【表达式keys()为我们提供了文本中所有不同类型的链表】
>>>vocabulary1[:50]
[u'funereal', u'unscientific', u'divinely', u'foul', u'four', u'gag', u'prefix', u'woods', u'clotted', u'Duck', u'hanging', u'plaudits', u'woody', u'Until', u'marching', u'disobeying', u'canes', u'granting', u'advantage', u'Westers', u'insertion', u'DRYDEN', u'formless', u'Untried', u'superficially', u'vesper', u'Western', u'portentous', u'meadows', u'sinking', u'Ding', u'Spurn', u'treasuries', u'churned', u'oceans', u'powders', u'tinkerings', u'tantalizing', u'yellow', u'bolting', u'uncertain', u'stabbed', u'bringing', u'elevations', u'ferreting', u'wooded', u'songster', u'uttering', u'scholar', u'Less']
>>>fdist1['whale']
906
```

`>>>fdist1.plot(50,cumulative=True)【前五十个词累计频率图】`

![]
(http://imglf4.nosdn.127.net/img/N3Z1WlRXTDM5VXpCZExMS1dDVUY2MURTTEhmVFQwVFplQTlZcUNuUVB5cS91QXZVNVNoZW1nPT0.png)

`>>>fdist1.hapaxes()【只出现一次的词】`

### 细粒度的选择词
#### 查找文中长词
```
>>> len(set(text1))
19317
>>> len(sorted(text1))
260819
>>> V=set(text1)
>>> long_words=[w for w in V if len(w)>15]
>>> sorted(long_words)
[u'CIRCUMNAVIGATION', u'Physiognomically', u'apprehensiveness', u'cannibalistically', u'characteristically', u'circumnavigating', u'circumnavigation', u'circumnavigations', u'comprehensiveness', u'hermaphroditical', u'indiscriminately', u'indispensableness', u'irresistibleness', u'physiognomically', u'preternaturalness', u'responsibilities', u'simultaneousness', u'subterraneousness', u'supernaturalness', u'superstitiousness', u'uncomfortableness', u'uncompromisedness', u'undiscriminating', u'uninterpenetratingly']
>>>
```

#### 查找文中出现频率高的长词
```
>>> sorted([w for w in set(text5) if len(w)>7 and fdist5[w]>7])
[u'#14-19teens', u'#talkcity_adults', u'((((((((((', u'........', u'Question', u'actually', u'anything', u'computer', u'cute.-ass', u'everyone', u'football', u'innocent', u'listening', u'remember', u'seriously', u'something', u'together', u'tomorrow', u'watching']
>>>
```
#### 词的搭配和双连词

```
>>> text4.collocations()
United States; fellow citizens; four years; years ago; Federal
Government; General Government; American people; Vice President; Old
World; Almighty God; Fellow citizens; Chief Magistrate; Chief Justice;
God bless; every citizen; Indian tribes; public debt; one another;
foreign nations; political parties
>>> text8.collocations()
would like; medium build; social drinker; quiet nights; non smoker;
long term; age open; Would like; easy going; financially secure; fun
times; similar interests; Age open; weekends away; poss rship; well
presented; never married; single mum; permanent relationship; slim
build
>>>
```
### 计数和其他东西
#### 查看文中词长分布
```
>>> [len(w) for w in text1]【查看文中所有词的长度】
[1, 4, 4, 2, 6, 8, 4, 1, 9, 1, 1, 8, 2, 1, 4, 11, 5, 2, 1, 7, 6, 1, 3, 4, 5, 2, 10, 2, 4, 1, 5, 1, 4, 1, 3, 5, 1, 1, 3, 3, 3, 1, 2, 3, 4, 7, 3 ...]
>>> fdist=FreqDist([len(w) for w in text1])【查看文中词长度出现的频率】
>>> fdist
FreqDist({3: 50223, 1: 47933, 4: 42345, 2: 38513, 5: 26597, 6: 17111, 7: 14399, 8: 9966, 9: 6428, 10: 3528, ...})
>>> fdist.keys()
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20]
>>>
```
#### 不同长度的词出现频率
```
>>> fdist.items()
[(1, 47933), (2, 38513), (3, 50223), (4, 42345), (5, 26597), (6, 17111), (7, 14399), (8, 9966), (9, 6428), (10, 3528), (11, 1873), (12, 1053), (13, 567), (14, 177), (15, 70), (16, 22), (17, 12), (18, 1), (20, 1)]
>>> fdist.max()
3
>>> fdist[3]
50223
>>> fdist.freq(3)【长度为3的词占书中所有词汇的比率】
0.19255882431878046
```
#### 频率相关函数
```
fdist=FreqDist(samples) 创建包含给定样本的频率分布
fdist.inc(sample) 增加样本
fdist['monstrous'] 计算给定样本出现的次数
fdist.N()样本总数
fdist.keys()以频率递减顺序排序的样本链表
for sample in fdist  以频率递减的顺序遍历样本
fdist.max() 数值最大的样本
fdist.tabulate 绘制频率分布表
fdist.plot 绘制频率分布图
fdist.plot(cumulative=True) 绘制累计频率分布图
fdist1<fdist2 测试样本在fdist1中出现的频率是否小于fdist2
```
