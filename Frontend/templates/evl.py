#program to evaluate the nlp model
import spacy
from spacy import displacy
from fastapi import FastAPI

#object creation
obj=FastAPI()


nlp = spacy.load("C:/Users/siva.kotagiri/OneDrive - Nimble Accounting/Desktop/siva/resume parsermy_desired_filename/resume parsermy_desired_filename/model-best")      #loading the model and storing it in nlp

resume = """
Siva Kumar Kotagiri Email: sivakumarkotagiri15@gmail.com
"""

#result= nlp(resume)    #the nlp is the object we can pass the resume as input to it and see the results

#for ent in result.ents:
#    print( ent.label_,"------->",ent.text)
#displacy.serve(result,style="ent", host="localhost",port=8000)

def predict(text):
    print(text);
    print("ghgnhgnghn");
    result=nlp(text)
    d={}
    for ent in result.ents:
        if ent.label_ in d:
            if ent.text in d.values():
                continue
            else:
                d[ent.label_]=ent.text + "-" + d[ent.label_]
        else:
            d[ent.label_]=ent.text
    print("done")
    return d



@obj.get("/")
def root():
    return ("welcome to the resume parsing")
@obj.get("/resume-parser")
def res(text:str):
    return(predict(text))
    

