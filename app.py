from flask import Flask, render_template, request
import sqlalchemy as sql
import pickle
import numpy as np

app=Flask(__name__)

# load our model
output_map={0: 'Not Fraud', 1: 'Fraud'}
with open('assets/XGB.pkl', 'rb') as f: 
	# define variable for pickle.load
	XGB=pickle.load(f)

#when running replace password
#engine=sql.create_engine('postgresql://postgres:*******@creditfrauddb.cfc5jupuejq5.us-east-2.rds.amazonaws.com:5432/creditfrauddb')

#def query_balance(account_id): 
	# result=engine.execute(f'select * from ____ where id = {account_id}').tolist()
	# return result[0]

def convert_to_float(input): 
	if input: 
		return float(input)
	else: 
		return float(0)

@app.route('/', methods=['GET', 'POST'])
def home(): 
	# return render_template('index_1.html')
	
	# return render_template('index_2.html', output='hard-coded 17')
	
	# x1=request.form.get('x1')
	# x2=request.form.get('x2')
	# model_output=lr.predict([(x1, x2)])
	# return render_template('index_2.html', output=f'Class {model_output[0]}')

	if request.method=='POST': 
		user_input={'step': convert_to_float(request.form.get('step')), 
		            'type': convert_to_float(request.form.get('type')), 
		            'amount': convert_to_float(request.form.get('amount')), 
		            'oldBalanceOrig': convert_to_float(request.form.get('oldBalanceOrig')), 
		            'newBalanceOrig': convert_to_float(request.form.get('newBalanceOrig')),
		            'oldBalanceDest': convert_to_float(request.form.get('oldBalanceDest')), 
		            'newBalanceDest': convert_to_float(request.form.get('newBalanceDest'))}
		user_input['errorBalanceOrig']=user_input['newBalanceOrig']+user_input['amount']-user_input['oldBalanceOrig']
		user_input['errorBalanceDest']=user_input['oldBalanceDest']+user_input['amount']-user_input['newBalanceDest']
		user_input=user_input.values()
		user_input_array=np.array([*user_input])
		user_input_array=user_input_array.reshape(-1, 9)
		model_output=XGB.predict(user_input_array)
		return render_template('index_1.html', output=f'{output_map[model_output[0]]}')
	else: 
		return render_template('index_1.html')

if __name__=='__main__': 
	app.run()