from meetup_five.File import CustomFile
import csv
class CustomFileProcessor(object):
    """processes input files and outputs the result into a csv file"""
    files = []
    def __init__(self,filepath='data/output.csv'):
        self.filePath = filepath
    
    def add_file(self, file):
        self.files.append(file)

    def print_stats(self):
        for file in self.files:
            print(file.filePath)
            print(file.get_row_count())
            print(file.get_unique_word_count())
            print(file.get_word_count())
            print(file.get_word_statistics())

    def save_to_csv(self):
        with open(self.filePath, 'w') as csvfile:
            fileNameHeader = 'file_name'
            wordCountHeader = 'word_count'
            rowCountHeader = 'row_count'
            fieldnames = [fileNameHeader, wordCountHeader,rowCountHeader]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for file in self.files:
                writer.writerow({fileNameHeader: file.filePath, wordCountHeader: file.get_word_count(),rowCountHeader:file.get_row_count()})

        print('Output saved to {0}'.format(self.filePath))
            


