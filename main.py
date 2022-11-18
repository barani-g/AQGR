import aqgFunction
# Main Function
def main():
    # Create AQG object
    aqg = aqgFunction.AutomaticQuestionGenerator()
    inputTextPath = "D:/FALL 22/NLP/Project/AQG/ip2.txt"
    readFile = open(inputTextPath, 'r+', encoding="utf8")
    inputText = readFile.read()
    questionList = aqg.aqgParse(inputText)
    aqg.display(questionList)
    #aqg.DisNormal(questionList)
    return 0
# Call Main Function
if __name__ == "__main__":
    main()