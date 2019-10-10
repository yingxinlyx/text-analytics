class TextCleaningUtils:
    
    
    def __init__(self, text):
        self.text = text

        
    def tokenizer(self):
        """this is to tokenize string text"""
    
        from nltk.tokenize import sent_tokenize
        sentences = sent_tokenize(self.text)
    
        return sentences
    
    
    def remove_stop(self, sentence):
        """this is to remove stop words"""

        from nltk.corpus import stopwords 
        stop = set(stopwords.words('english'))
        stop_free = " ".join([i for i in sentence.split() if i not in stop])

        return stop_free
    
    
    def stemming(self, sentence):
        """this is to stem words in a sentence"""

        from nltk.stem import PorterStemmer 
        porter = PorterStemmer()
        normalized = " ".join(porter.stem(word) for word in sentence.split())

        return normalized
    
    
    def lemmatizer(self, sentence):
        from nltk.stem.wordnet import WordNetLemmatizer
        lemma = WordNetLemmatizer()
        normalized = " ".join(lemma.lemmatize(word) for word in sentence.split())
        
        return normalized
    
    
    def text_clean(self, stop=1, stem=0, lemma=0):
        """this is to remove non-alpha characters, stop words and lemmatize the doc"""

        import re   
        ctext = re.sub("[^a-zA-Z]", " ", self.text.lower())
        if stop == 1:
            ctext = self.remove_stop(ctext)
        if stem == 1:
            ctext = self.stemming(ctext)
        if lemma == 1:
            ctext = self.lemmatizer(ctext)

        return ctext