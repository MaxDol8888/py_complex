import sys
from meetup_five.File import CustomFile
from meetup_five.FileProcessor import CustomFileProcessor

if __name__ == "__main__":
  
    processor = CustomFileProcessor()
    if not len(sys.argv) > 1 :
        text1 = CustomFile('data/text1.txt')
        text2 = CustomFile('data/text2.txt')
        processor.add_file(text1)
        processor.add_file(text2)
    else:
        for fileArgument in sys.argv[1:]:
            textFile = CustomFile(fileArgument)
            processor.add_file(textFile)

    processor.print_stats()
    processor.save_to_csv()
