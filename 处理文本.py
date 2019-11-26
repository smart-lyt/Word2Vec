#处理文件使其符合word2vec输入格式
查阅BrownCorpus,Text8Corpus或lineSentence

#first example：
class MySentences(object):
...     def __init__(self, dirname):
...         self.dirname = dirname
... 
...     def __iter__(self):
...         for fname in os.listdir(self.dirname):
...             for line in open(os.path.join(self.dirname, fname)):
...                 yield line.split()
>>>
>>> sentences = MySentences('/some/directory') # a memory-friendly iterator
>>> model = gensim.models.Word2Vec(sentences)

#second example:
import nltk
raw_text = ''
# os.listdir()方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
for file in os.listdir('./input/'):     
  if file.endswith(".txt"):        
    raw_text += open("./input/" + file, errors='ignore').read() + '\n\n'
raw_text = raw_text.lower()
#加载punkt句子分割器
sentensor = nltk.data.load('tokenizers/punkt/english.pickle')  
# <nltk.tokenize.punkt.PunktSentenceTokenizer at 0x16cc42020f0> 
# 对句子进行分割：将文章分割为句子列表
sents = sentensor.tokenize(raw_text)   
#句子列表['句子1.'，'句子2.'...]
corpus = [] 
# 分词word tokenize：将句子分割为单词列表
for sen in sents:    
  corpus.append(nltk.word_tokenize(sen))   
# 单词列表[['sexes', 'similar', '.'],['family', 'hirundinidae', '.'],...] 
# 构建词向量：W2V
w2v_model = Word2Vec(corpus, size=128, window=5, min_count=3, workers=4)   # 128维的词向量

#third example:中文文本，分词后处理
with open('./in_the_name_of_people.txt') as f:
  document = f.read()
  document_cut = jieba.cut(document)
  result = ' '.join(document_cut)
  result = result.encode('utf-8')
  with open('./in_the_name_of_people_segment.txt', 'w') as f2:
    f2.write(result)
  sentences = word2vec.LineSentence('./in_the_name_of_people_segment.txt') 
  model = word2vec.Word2Vec(sentences, hs=1,min_count=1,window=3,size=100)
  
 

    
