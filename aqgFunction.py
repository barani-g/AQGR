import re
import spacy
import clause
import random
import nonClause
import identification
import questionValidation
from nlpNER import nerTagger

class AutomaticQuestionGenerator():
    # AQG Parsing & Generate a question
    def aqgParse(self, sentence):
        #nlp = spacy.load("en")
        nlp = spacy.load('en_core_web_md')
        singleSentences = sentence.split(".")
        questionsList = []
        if len(singleSentences) != 0:
            for i in range(len(singleSentences)):
                segmentSets = singleSentences[i].split(",")

                ner = nerTagger(nlp, singleSentences[i])

                if (len(segmentSets)) != 0:
                    for j in range(len(segmentSets)):
                        try:
                            questionsList += clause.howmuch_2(segmentSets, j, ner)
                        except Exception:
                            pass

                        if identification.clause_identify(segmentSets[j]) == 1:
                            try:
                                questionsList += clause.whom_1(segmentSets, j, ner)
                            except Exception:
                                pass
                            try:
                                questionsList += clause.whom_2(segmentSets, j, ner)
                            except Exception:
                                pass
                            try:
                                questionsList += clause.whom_3(segmentSets, j, ner)
                            except Exception:
                                pass
                            try:
                                questionsList += clause.whose(segmentSets, j, ner)
                            except Exception:
                                pass
                            try:
                                questionsList += clause.what_to_do(segmentSets, j, ner)
                            except Exception:
                                pass
                            try:
                                questionsList += clause.who(segmentSets, j, ner)
                            except Exception:
                                pass
                            try:
                                questionsList += clause.howmuch_1(segmentSets, j, ner)
                            except Exception:
                                pass
                            try:
                                questionsList += clause.howmuch_3(segmentSets, j, ner)
                            except Exception:
                                pass


                            else:
                                try:
                                    s = identification.subjectphrase_search(segmentSets, j)
                                except Exception:
                                    pass

                                if len(s) != 0:
                                    segmentSets[j] = s + segmentSets[j]
                                    try:
                                        questionsList += clause.whom_1(segmentSets, j, ner)
                                    except Exception:
                                        pass
                                    try:
                                        questionsList += clause.whom_2(segmentSets, j, ner)
                                    except Exception:
                                        pass
                                    try:
                                        questionsList += clause.whom_3(segmentSets, j, ner)
                                    except Exception:
                                        pass
                                    try:
                                        questionsList += clause.whose(segmentSets, j, ner)
                                    except Exception:
                                        pass
                                    try:
                                        questionsList += clause.what_to_do(segmentSets, j, ner)
                                    except Exception:
                                        pass
                                    try:
                                        questionsList += clause.who(segmentSets, j, ner)
                                    except Exception:
                                        pass

                                    else:
                                        try:
                                            questionsList += nonClause.what_whom1(segmentSets, j, ner)
                                        except Exception:
                                            pass
                                        try:
                                            questionsList += nonClause.what_whom2(segmentSets, j, ner)
                                        except Exception:
                                            pass
                                        try:
                                            questionsList += nonClause.whose(segmentSets, j, ner)
                                        except Exception:
                                            pass
                                        try:
                                            questionsList += nonClause.howmany(segmentSets, j, ner)
                                        except Exception:
                                            pass
                                        try:
                                            questionsList += nonClause.howmuch_1(segmentSets, j, ner)
                                        except Exception:
                                            pass

                questionsList.append('\n')
        return questionsList



    def DisNormal(self, string):
        print("\n")
        print("----SUCCESSFULLY QUESTIONS GENERATED----")
        print("Questions:\n")

        count = 0
        out = ""

        for i in range(len(string)):
            count = count + 1
            print("Question-0%d: %s" % (count, string[i]))

        print("")
        print("End of Questions")
        print("-----------\n\n")


    # AQG Display the Generated Question
    def display(self, string):
        print("\n")
        print("----SUCCESSFULLY QUESTIONS GENERATED----")
        print("Questions:\n")

        count = 0
        out = ""
        for i in range(len(string)):
            if (len(string[i]) >= 3):
                if (questionValidation.hNvalidation(string[i]) == 1):
                    if ((string[i][0] == 'W' and string[i][1] == 'h') or (string[i][0] == 'H' and string[i][1] == 'o') or (
                            string[i][0] == 'H' and string[i][1] == 'a')):
                        WH = string[i].split(',')
                        if (len(WH) == 1):
                            string[i] = string[i][:-1]
                            string[i] = string[i][:-1]
                            string[i] = string[i][:-1]
                            string[i] = string[i] + "?"
                            count = count + 1

                            if (count < 10):
                                print("Question-0%d: %s" % (count, string[i]))
                                out += "Question-0" + count.__str__() + ": " + string[i] + "\n"

                            else:
                                print("Question-%d: %s" % (count, string[i]))
                                out += "Question-" + count.__str__() + ": " + string[i] + "\n"

        print("")
        print("End of Questions")
        print("------------\n\n")

        output = "D:/FALL 22/NLP/Project/AQG/output.txt"
        w = open(output, 'w+', encoding="utf8")
        w.write(out)
        w.close()
        readFile = open("output.txt",'r')
        questionPaperList = list(readFile)
        print("Provide the Number of Set's:")
        qSet = int(input())
        print("Provide the Number of Question's per Set:")
        tQuestion = int(input())
        for i in range(1,qSet+1):
            writeFile = open("Set - "+str(i)+".txt","w+")
            for j in range(1,tQuestion+1):
                questionNumber = random.randint(0,len(questionPaperList)-1)
                writeQuestion = re.sub(r"Question-\d*:","Question-"+str(j)+":", questionPaperList[questionNumber])
                writeFile.write(writeQuestion)
        return 0
