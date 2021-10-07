'''
Name: Akhilesh Dhama
Date: 25th Sept 2021
Title: Solution to Virus
'''
from flask import Flask,render_template,request
app=Flask(__name__)
import pickle

#open a file,where you wanna stored the pickled data
file=open('model.pkl','rb')  
clf=pickle.load(file)
file.close()


@app.route('/',methods=["GET","POST"])
def hello_world():
    if request.method=='POST':
        myDict=request.form
        fever=int(myDict['fever'])
        age=int(myDict['age'])
        bodyPain=int(myDict['bodyPain'])
        runnyNose=int(myDict['runnyNose'])
        diffBreadth=int(myDict['diffBreadth'])
        #code for inference
        inputFeatures=[fever,bodyPain,age,diffBreadth,runnyNose]
        infProb=clf.predict_proba([inputFeatures])[0][1]
        print(infProb)
        return render_template('show.html',inf=round(infProb*100))
    return render_template('index.html')
        


if __name__=='__main__':
    app.run(debug=True)
