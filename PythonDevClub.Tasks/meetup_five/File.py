class CustomFile(object):
    """Represents the file as a File, that was read by the FileProcessor"""
    
    filePath = ""
    fileContents = dict()
    isFileLoaded = False
    def __init__(self, filePath=""):
        self.filePath = filePath
        self.isFileLoaded = self.load_file()
        if not self.isFileLoaded:
            raise IOError('File was not loaded')

    def get_word_count(self):
        word_count = 0
        if self.isFileLoaded:
            for x in self.fileContents:
                temp = str(x).split()
                word_count += len(temp)
        return word_count
    
    def get_word_statistics(self):
        result_dict = dict()
        if self.isFileLoaded:
            for row in self.fileContents:
                words_in_row = str(row).split()
                for word in words_in_row:
                    word_count = 1
                    if word in result_dict:
                        old_count = result_dict[word]
                        result_dict[word] = old_count + word_count
                    else:
                        result_dict[word] = word_count
        return result_dict
    
    def get_row_count(self):
        rowCount = 0
        if self.isFileLoaded:
            for x in self.fileContents:
                rowCount += 1
        return rowCount
                    
    def get_unique_word_count(self):
        list_of_words = []
        if self.isFileLoaded:
            for x in self.fileContents:
                list_of_words.extend(str(x).split())
            
        unique_words = set(list_of_words)
        return len(unique_words)   
    
    def get_count_per_word(self):
        word_counts = {}
        if self.isFileLoaded:
            for line in self.fileContents:
                list_of_words = str(line).split()
                for x in list_of_words:
                    
                    word_count = 0
                    word_counts[x] = word_count     
    
    def load_file(self):
        try:
            with open(self.filePath,'r') as f:
                self.fileContents = f.readlines()
            return True
        except IOError as e:
            print(e)
            return False
        return False
        




