## 2.1 获取文本语料库
### 古腾堡语料库
```
>>> import nltk
>>> nltk.corpus.gutenberg.fileids()
[u'austen-emma.txt', u'austen-persuasion.txt', u'austen-sense.txt', u'bible-kjv.txt', u'blake-poems.txt', u'bryant-stories.txt', u'burgess-busterbrown.txt', u'carroll-alice.txt', u'chesterton-ball.txt', u'chesterton-brown.txt', u'chesterton-thursday.txt', u'edgeworth-parents.txt', u'melville-moby_dick.txt', u'milton-paradise.txt', u'shakespeare-caesar.txt', u'shakespeare-hamlet.txt', u'shakespeare-macbeth.txt', u'whitman-leaves.txt']
>>> emma=nltk.corpus.gutenberg.words('austen-emma.txt')
>>> print (len(emma))
192427
>>>
```

```
>>>emma=nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
>>>emma.concordance("surprize")
Displaying 25 of 37 matches:
er father , was sometimes taken by surprize at his being still able to pity ` 
hem do the other any good ." " You surprize me ! Emma must do Harriet good : a
Knightley actually looked red with surprize and displeasure , as he stood up ,
r . Elton , and found to his great surprize , that Mr . Elton was actually on 
d aid ." Emma saw Mrs . Weston ' s surprize , and felt that it must be great ,
father was quite taken up with the surprize of so sudden a journey , and his f
y , in all the favouring warmth of surprize and conjecture . She was , moreove
he appeared , to have her share of surprize , introduction , and pleasure . Th
ir plans ; and it was an agreeable surprize to her , therefore , to perceive t
talking aunt had taken me quite by surprize , it must have been the death of m
f all the dialogue which ensued of surprize , and inquiry , and congratulation
 the present . They might chuse to surprize her ." Mrs . Cole had many to agre
the mode of it , the mystery , the surprize , is more like a young woman ' s s
 to her song took her agreeably by surprize -- a second , slightly but correct
" " Oh ! no -- there is nothing to surprize one at all .-- A pretty fortune ; 
t to be considered . Emma ' s only surprize was that Jane Fairfax should accep
of your admiration may take you by surprize some day or other ." Mr . Knightle
ation for her will ever take me by surprize .-- I never had a thought of her i
 expected by the best judges , for surprize -- but there was great joy . Mr . 
 sound of at first , without great surprize . " So unreasonably early !" she w
d Frank Churchill , with a look of surprize and displeasure .-- " That is easy
; and Emma could imagine with what surprize and mortification she must be retu
tled that Jane should go . Quite a surprize to me ! I had not the least idea !
 . It is impossible to express our surprize . He came to speak to his father o
g engaged !" Emma even jumped with surprize ;-- and , horror - struck , exclai
```
另一种版本的import

```
>>> from nltk.corpus import gutenberg
>>> gutenberg.fileids()
[u'austen-emma.txt', u'austen-persuasion.txt', u'austen-sense.txt', u'bible-kjv.txt', u'blake-poems.txt', u'bryant-stories.txt', u'burgess-busterbrown.txt', u'carroll-alice.txt', u'chesterton-ball.txt', u'chesterton-brown.txt', u'chesterton-thursday.txt', u'edgeworth-parents.txt', u'melville-moby_dick.txt', u'milton-paradise.txt', u'shakespeare-caesar.txt', u'shakespeare-hamlet.txt', u'shakespeare-macbeth.txt', u'whitman-leaves.txt']
>>> emma=gutenberg.words('austen-emma.txt')
```

写一个简短的程序，通过循环遍历前面列出的gutenberg文件标识符链表相应的fileid，然后计算统计每个文本。用int()函数来确保数字都是整数。
```
>>>for fileid in gutenberg.fileids():
      num_chars=len(gutenberg.raw(fileid))
      num_words=len(gutenberg.words(fileid))
      num_sents=len(gutenberg.sents(fileid))
      num_vocab=len(set([w.lower() for w in gutenberg.words(fileid)]))
     print int(num_chars/num_words),int(num_words/num_sents),int(num_words/num_vocab),fileid
4 24 26 austen-emma.txt
4 26 16 austen-persuasion.txt
4 28 22 austen-sense.txt
4 33 79 bible-kjv.txt
4 19 5 blake-poems.txt
4 19 14 bryant-stories.txt
4 17 12 burgess-busterbrown.txt
4 20 12 carroll-alice.txt
4 20 11 chesterton-ball.txt
4 22 11 chesterton-brown.txt
4 18 10 chesterton-thursday.txt
4 20 24 edgeworth-parents.txt
4 25 15 melville-moby_dick.txt
4 52 10 milton-paradise.txt
4 11 8 shakespeare-caesar.txt
4 12 7 shakespeare-hamlet.txt
4 12 6 shakespeare-macbeth.txt
4 36 12 whitman-leaves.txt
```
num_chars/num_words 平均词长
num_words/num_sents 平均句长
num_words/num_vocab 每个词出现的平均次数

使用raw()函数得到没有进行过任何语言学处理的文件的内容
`len(gutenberg.raw('blake-poems.txt')`文本中出现的词汇个数，包括空格
sents()函数将文本划分为句子，一个句子是一个词链表
```
>>> macbeth_sentences=gutenberg.sents('shakespeare-macbeth.txt')
>>> macbeth_sentences
[[u'[', u'The', u'Tragedie', u'of', u'Macbeth', u'by', u'William', u'Shakespeare', u'1603', u']'], [u'Actus', u'Primus', u'.'], ...]
>>>>>> macbeth_sentences[1037]
[u'Good', u'night', u',', u'and', u'better', u'health', u'Attend', u'his', u'Maiesty']
>>> longest_len=max([len(s) for s in macbeth_sentences])
>>> [s for s in macbeth_sentences if len(s) == longest_len]
[[u'Doubtfull', u'it', u'stood', u',', u'As', u'two', u'spent', u'Swimmers', u',', u'that', u'doe', u'cling', u'together', u',', u'And', u'choake', u'their', u'Art', u':', u'The', u'mercilesse', u'Macdonwald', u'(', u'Worthie', u'to', u'be', u'a', u'Rebell', u',', u'for', u'to', u'that', u'The', u'multiplying', u'Villanies', u'of', u'Nature', u'Doe', u'swarme', u'vpon', u'him', u')', u'from', u'the', u'Westerne', u'Isles', u'Of', u'Kernes', u'and', u'Gallowgrosses', u'is', u'supply', u"'", u'd', u',', u'And', u'Fortune', u'on', u'his', u'damned', u'Quarry', u'smiling', u',', u'Shew', u"'", u'd', u'like', u'a', u'Rebells', u'Whore', u':', u'but', u'all', u"'", u's', u'too', u'weake', u':', u'For', u'braue', u'Macbeth', u'(', u'well', u'hee', u'deserues', u'that', u'Name', u')', u'Disdayning', u'Fortune', u',', u'with', u'his', u'brandisht', u'Steele', u',', u'Which', u'smoak', u"'", u'd', u'with', u'bloody', u'execution', u'(', u'Like', u'Valours', u'Minion', u')', u'caru', u"'", u'd', u'out', u'his', u'passage', u',', u'Till', u'hee', u'fac', u"'", u'd', u'the', u'Slaue', u':', u'Which', u'neu', u"'", u'r', u'shooke', u'hands', u',', u'nor', u'bad', u'farwell', u'to', u'him', u',', u'Till', u'he', u'vnseam', u"'", u'd', u'him', u'from', u'the', u'Naue', u'toth', u"'", u'Chops', u',', u'And', u'fix', u"'", u'd', u'his', u'Head', u'vpon', u'our', u'Battlements']]
>>>
```

### 网络和聊天文本
```
from nltk.corpus import webtext
for fileid in webtext.fileids():
    print fileid, webtext.raw(fileid)[:65],'...'
firefox.txt Cookie Manager: "Don't allow sites that set removed cookies to se ...
grail.txt SCENE 1: [wind] [clop clop clop] 
KING ARTHUR: Whoa there!  [clop ...
overheard.txt White guy: So, do you have any plans for this evening?
Asian girl ...
pirates.txt PIRATES OF THE CARRIBEAN: DEAD MAN'S CHEST, by Ted Elliott & Terr ...
singles.txt 25 SEXY MALE, seeks attrac older single lady, for discreet encoun ...
wine.txt Lovely delicate, fragrant Rhone wine. Polished leather and strawb ...
```
即时消息会话语料库
```
from nltk.corpus import nps_chat
chatroom=nps_chat.posts('10-19-20s_706posts.xml')
print (chatroom[123])
[u'i', u'do', u"n't", u'want', u'hot', u'pics', u'of', u'a', u'female', u',', u'I', u'can', u'look', u'in', u'a', u'mirror', u'.']
```
### 布朗语料库
```
from nltk.corpus import brown
print (brown.categories())
[u'adventure', u'belles_lettres', u'editorial', u'fiction', u'government', u'hobbies', u'humor', u'learned', u'lore', u'mystery', u'news', u'religion', u'reviews', u'romance', u'science_fiction']
print (brown.words(categories='news'))
[u'The', u'Fulton', u'County', u'Grand', u'Jury', ...]
print (brown.sents(fileid=['cg22']))
[[u'Does', u'our', u'society', u'have', u'a', u'runaway', u',', u'uncontrollable', u'growth', u'of', u'technology', u'which', u'may', u'end', u'our', u'civilization', u',', u'or', u'a', u'normal', u',', u'healthy', u'growth', u'?', u'?'], [u'Here', u'there', u'may', u'be', u'an', u'analogy', u'with', u'cancer', u':', u'we', u'can', u'detect', u'cancers', u'by', u'their', u'rapidly', u'accelerating', u'growth', u',', u'determinable', u'only', u'when', u'related', u'to', u'the', u'more', u'normal', u'rate', u'of', u'healthy', u'growth', u'.'], ...]
print (brown.sents(categories=['news','editorial','reviews']))
[[u'The', u'Fulton', u'County', u'Grand', u'Jury', u'said', u'Friday', u'an', u'investigation', u'of', u"Atlanta's", u'recent', u'primary', u'election', u'produced', u'``', u'no', u'evidence', u"''", u'that', u'any', u'irregularities', u'took', u'place', u'.'], [u'The', u'jury', u'further', u'said', u'in', u'term-end', u'presentments', u'that', u'the', u'City', u'Executive', u'Committee', u',', u'which', u'had', u'over-all', u'charge', u'of', u'the', u'election', u',', u'``', u'deserves', u'the', u'praise', u'and', u'thanks', u'of', u'the', u'City', u'of', u'Atlanta', u"''", u'for', u'the', u'manner', u'in', u'which', u'the', u'election', u'was', u'conducted', u'.'], ...]
```
布朗语料库方便用来研究文体之间的系统性差异——文体学研究
##### 比较不同文体中情态动词的用法
```
import nltk
from nltk.corpus import brown
news_text=brown.words(categories='news')
fdist= nltk.FreqDist([w.lower() for w in news_text])
modals=['can','could','may',',might','must','will']
for m in modals:
    print m + ':',fdist[m],
can: 94 could: 87 may: 93 ,might: 0 must: 53 will: 389
```

```
cfd=nltk.ConditionalFreqDist(
    (genre,word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))
genre=['news','religion','hobbies','science_fiction','romance','humor']
modals=['can','could','may','might','must','will']
print (cfd.tabulate(conditions=genre,samples=modals))
                   can could   may might  must  will 
           news    93    86    66    38    50   389 
       religion    82    59    78    12    54    71 
        hobbies   268    58   131    22    83   264 
science_fiction    16    49     4    12     8    16 
        romance    74   193    11    51    45    43 
          humor    16    30     8     8     9    13 
```
### 路透社语料库
```
from nltk.corpus import reuters
print (reuters.fileids())
['test/14826', 'test/14828', 'test/14829', 'test/14832',...]
print (reuters.categories())
[u'acq', u'alum', u'barley', u'bop', u'carcass', u'castor-oil', u'cocoa', u'coconut', u'coconut-oil', u'coffee', u'copper', u'copra-cake', u'corn', u'cotton', u'cotton-oil', u'cpi', u'cpu', u'crude', u'dfl', u'dlr', u'dmk',...]
reuters.categories('training/9865')
[u'barley', u'corn', u'grain', u'wheat']
reuters.categories(['training/9865','training/9880'])
[u'barley', u'corn', u'grain', u'money-fx', u'wheat']
reuters.fileids('barley')
[u'test/15618', u'test/15649', u'test/15676', u'test/15728', u'test/15871', u'test/15875', u'test/15952', u'test/17767', u'test/17769', u'test/18024', u'test/18263', u'test/18908', u'test/19275', u'test/19668', u'training/10175', u'training/1067', u'training/11208', u'training/11316', u'training/11885', u'training/12428', u'training/13099', u'training/13744', u'training/13795', u'training/13852', u'training/13856', u'training/1652', u'training/1970', u'training/2044', u'training/2171',...]
>>> reuters.fileids(['barley','corn'])
[u'test/14832', u'test/14858', u'test/15033', u'test/15043', u'test/15106', u'test/15287', u'test/15341', u'test/15618', u'test/15648', ...]
```
以文档或类别为单位查找词句
```
>>> reuters.words('training/9865')[:14]
[u'FRENCH', u'FREE', u'MARKET', u'CEREAL', u'EXPORT', u'BIDS', u'DETAILED', u'French', u'operators', u'have', u'requested', u'licences', u'to', u'export']
>>> reuters.words(['training/9865','training/9880'])
[u'FRENCH', u'FREE', u'MARKET', u'CEREAL', u'EXPORT', ...]
>>> reuters.words(categories='barley')
[u'FRENCH', u'FREE', u'MARKET', u'CEREAL', u'EXPORT', ...]
>>> reuters.words(categories=['barley','corn'])
[u'THAI', u'TRADE', u'DEFICIT', u'WIDENS', u'IN', ...]
>>>
```
