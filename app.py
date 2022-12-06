from flask import Flask, render_template, request
import pickle

app=Flask(__name__)

with open('assets/lr.pkl', 'rb') as f: 
	lr=pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def home(): 
	# return render_template('index_1.html')
	
	# return render_template('index_2.html', output='hard-coded 17')
	
	# x1=request.form.get('x1')
	# x2=request.form.get('x2')
	# model_output=lr.predict([(x1, x2)])
	# return render_template('index_2.html', output=f'Class {model_output[0]}')

	if request.method=='POST': 
		x1=request.form.get('x1')
		x2=request.form.get('x2')
		model_output=lr.predict([(x1, x2)])
		return render_template('index_2.html', output=f'Class {model_output[0]}')
	else: 
		return render_template('index_2.html')

if __name__=='__main__': 
	app.run()