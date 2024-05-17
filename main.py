from twilio.rest import Client
import keys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

df = pd.read_csv("train.csv")
df = df.drop(['No.','Time'],axis=1)
df = df[df['Protocol'] == 'HTTP']

df1 = pd.read_csv("test.csv")
df1 = df1.drop(['No.','Time'],axis=1)
df1 = df1[df1['Protocol'] == 'HTTP']

def assign_numbers(ip_addresses):
 prev_ip = None
 prev_num = 0
 output = []
 for ip in ip_addresses:
     if prev_ip is None:
         prev_ip = ip
         output.append(prev_num)
     elif prev_ip != ip:
         prev_ip = ip
         if prev_num == 0:
             prev_num = 1
         else:
            prev_num = 0
         output.append(prev_num)
     else:
         output.append(prev_num)
 return output


list_a = df['Source'].tolist()
list_b = df['Destination'].tolist()
list_c = df['Length'].tolist()
info1 = df['Info'].tolist()
df['SLabel'] = assign_numbers(list_a)
df['DLabel'] = assign_numbers(list_b)
df['LLabel'] = assign_numbers(list_c)
df['Infoo'] = assign_numbers(info1)
df = df.drop(['Source', 'Destination','Protocol','Info','Length'],axis=1)

list_a1 = df1['Source'].tolist()
list_b1 = df1['Destination'].tolist()
list_c1 = df1['Length'].tolist()
info11 = df1['Info'].tolist()
df1['SLabel'] = assign_numbers(list_a1)
df1['DLabel'] = assign_numbers(list_b1)
df1['LLabel'] = assign_numbers(list_c1)
df1['Infoo'] = assign_numbers(info11)
df1 = df1.drop(['Source', 'Destination','Protocol','Info','Length'],axis=1)

model = IsolationForest(n_estimators=100, contamination=float(0.2), random_state=42)
model.fit(df)
pred = model.predict(df1)


def check_negatives(lst):
    count = 0
    for num in lst:
        if num == -1:
            count += 1
            if count > 20:
                print("Alert")
                alert()
                return
        else:
            count = 0
    print("Nothing found")
    
def alert():
    client = Client(keys.account_sid,keys.auth_token)
    message = client.messages.create(
    from_=keys.twilio_number,
    body='alert ur being hacked',
    to=keys.target_number
    )
    print(message.body)

check_negatives(pred)