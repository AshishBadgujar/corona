from flask import Flask,render_template,request
import pickle

app=Flask(__name__)

@app.route('/',methods=["POST",'GET'])
def home():
    if request.method=='POST':
        cough=int(request.form['cough'])
        fever=int(request.form['fever'])
        diffbr=int(request.form['diffbr'])
        loss_sm=int(request.form['loss_sm'])
        with open('my_model','rb') as f:
            model=pickle.load(f)
        result=model.predict([[cough,fever,diffbr,loss_sm]])
        if result[0]=='YES':
            return render_template('home.html',data=["Sorry!, you have symptomps of COVID-19,Please consult your doctor !",'red'])
        else:
            return render_template('home.html',data=["Congratulation! you don't have any symptoms of COVID-19,Take care!",'green'])
        return render_template('home.html')
    else:
        return render_template('home.html')
       

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run()