### 用Python进行自然语言处理学习笔记（1）
##### 1.安装anacoda以及Pycharm
`from nltk.book import*`
```
text1
<Text: Moby Dick by Herman Melville>
```
##### 单词层面基础操作

###### 检索单词上下文

`text1.concordance("monstrous") `

###### 检索上下文类似的单词

`text1.similiar("monstrous")`

###### 检索两个或两个以上单词共同上下文

`text2.common_contexts(["monstrous","very"])`

###### 绘制单词位于文本中的位置离散图

`text4.dispersion_plot(["citizens","freedom","duties","America"])`

###### 随机文本

`text3.generate()`

##### 计数词汇

###### 计算文本大小

`len(text)`

###### 文本元素表

`set(text3)`

###### 文本元素排序表

`sorted(set(text3))`

###### 文本元素排序表大小

`len(sorted(text3))`

###### 文本词汇丰富度[文本大小/文本元素排序表大小]

```
from __future__ import division
len(text3) / len(sorted(text3))
```

###### 特定词在文本中出现次数

`text3.count("smote")`

###### 特定词在文本中占据的百分比
`100 * text4.count('a')  /  len(text4)`

###### e.g. text5中lol出现次数以及占文本全部词数百分比

``` text5.count("lol")
704
100 * text5.count('lol') / len(text5)
1
```

###### 定义函数
```def lexical_diversity(text):
...    return len(text) / len(set(text))
...
def percentage(count, total):
...    return 100 * count / total

```
