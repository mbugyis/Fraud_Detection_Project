from flask import Flask, render_template, request
import sqlalchemy as sql
import pickle

app=Flask(__name__)
# dump our model
with open('assets/lr.pkl', 'rb') as f: 
	#define variable for pickle.load
	lr=pickle.load(f)
#when running replace password
#engine=sql.create_engine('postgresql://postgres:*******@creditfrauddb.cfc5jupuejq5.us-east-2.rds.amazonaws.com:5432/creditfrauddb')

#def query_balance(account_id): 
	result=engine.execute(f'select * from ____ where id = {account_id}').tolist()
	return result[0]

@app.route('/', methods=['GET', 'POST'])
def home(): 
	# return render_template('index_1.html')
	
	# return render_template('index_2.html', output='hard-coded 17')
	
	# x1=request.form.get('x1')
	# x2=request.form.get('x2')
	# model_output=lr.predict([(x1, x2)])
	# return render_template('index_2.html', output=f'Class {model_output[0]}')

	if request.method=='POST': 
		amount=request.form.get('amount')
		oldbalanceOrg=request.form.get('oldbalanceOrg')
		oldbalanceDest=request.form.get('oldbalanceDest')
		#origin_balance=query_balance(request.form.get('orgin_id'))
		#errBal=old+amount-olddes
		model_output=lr.predict([(amount, oldbalanceOrg, oldbalanceDest)])
		return render_template('index_1.html', output=f'Class {model_output[0]}')
	else: 
		return render_template('index_1.html')

if __name__=='__main__': 
	app.run()