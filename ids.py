# -*- coding: utf-8 -*-
"""IDS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vJN6OPHdKDsRJ2oyQXiz-kFfYyjEIYNy

# Intrusion Detection System

# Importing the Dependencies
"""

import pandas as pd
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.metrics import accuracy_score

"""# Data Collection and Processing"""

test="/content/drive/MyDrive/Data/UNSW_NB15_testing-set.csv"
data=pd.read_csv(test)
data

# print first 5 rows of the dataset
data.head()

# print last 5 rows of the dataset
data.tail()

# number of rows and columns in the dataset
data.shape

# to check missing value in the dataset
missingvalue=pd.isnull("data")
missingvalue

# to check duplicate value in the dataset
data.duplicated()

data.isnull()

"""# Delete non-numeric Data"""

#drop non-numeric column
data.drop("proto",axis=1,inplace=True)
data

#drop non-numeric column
data.drop("state",axis=1,inplace=True)
data

#drop non-numeric column
data.drop("service",axis=1,inplace=True)
data

#drop non-numeric column
data.drop("attack_cat",axis=1,inplace=True)
data

#Save the Data File
data.to_csv('/content/drive/My Drive/Data/mydata.csv', index=False)

"""# Find the Mean, Mode, Median, Standard Deviation, Variance & Z_Score"""

print("Mean:",round(stats.mean(data.dur),3))
print("Mode:",round(stats.mode(data.dur),3))
print("Median:",round(stats.median(data.dur),3))
print("Standard deviation:",round(stats.stdev(data.dur),3))
print("Variance:",round(stats.variance(data.dur),3))
data['z_score']=(data.dur-data.dur.mean())/data.dur.std()
data

print("Mean:",round(stats.mean(data.spkts),3))
print("Mode:",round(stats.mode(data.spkts),3))
print("Median:",round(stats.median(data.spkts),3))
print("Standard deviation:",round(stats.stdev(data.spkts),3))
print("Variance:",round(stats.variance(data.spkts),3))
data['z_score1']=(data.spkts-data.spkts.mean())/data.spkts.std()
data

print("Mean:",round(stats.mean(data.dpkts),3))
print("Mode:",round(stats.mode(data.dpkts),3))
print("Median:",round(stats.median(data.dpkts),3))
print("Standard deviation:",round(stats.stdev(data.dpkts),3))
print("Variance:",round(stats.variance(data.dpkts),3))
data['z_score2']=(data.dpkts-data.dpkts.mean())/data.dpkts.std()
data

print("Mean:",round(stats.mean(data.sbytes),3))
print("Mode:",round(stats.mode(data.sbytes),3))
print("Median:",round(stats.median(data.sbytes),3))
print("Standard deviation:",round(stats.stdev(data.sbytes),3))
print("Variance:",round(stats.variance(data.sbytes),3))
data['z_score3']=(data.sbytes-data.sbytes.mean())/data.sbytes.std()
data

print("Mean:",round(stats.mean(data.dbytes),3))
print("Mode:",round(stats.mode(data.dbytes),3))
print("Median:",round(stats.median(data.dbytes),3))
print("Standard deviation:",round(stats.stdev(data.dbytes),3))
print("Variance:",round(stats.variance(data.dbytes),3))
data['z_score4']=(data.dbytes-data.dbytes.mean())/data.dbytes.std()
data

print("Mean:",round(stats.mean(data.rate),3))
print("Mode:",round(stats.mode(data.rate),3))
print("Median:",round(stats.median(data.rate),3))
print("Standard deviation:",round(stats.stdev(data.rate),3))
print("Variance:",round(stats.variance(data.rate),3))
data['z_score5']=(data.rate-data.rate.mean())/data.rate.std()
data

print("Mean:",round(stats.mean(data.sttl),3))
print("Mode:",round(stats.mode(data.sttl),3))
print("Median:",round(stats.median(data.sttl),3))
print("Standard deviation:",round(stats.stdev(data.sttl),3))
print("Variance:",round(stats.variance(data.sttl),3))
data['z_score6']=(data.sttl-data.sttl.mean())/data.sttl.std()
data

print("Mean:",round(stats.mean(data.dttl),3))
print("Mode:",round(stats.mode(data.dttl),3))
print("Median:",round(stats.median(data.dttl),3))
print("Standard deviation:",round(stats.stdev(data.dttl),3))
print("Variance:",round(stats.variance(data.dttl),3))
data['z_score7']=(data.dttl-data.dttl.mean())/data.dttl.std()
data

print("Mean:",round(stats.mean(data.sload),3))
print("Mode:",round(stats.mode(data.sload),3))
print("Median:",round(stats.median(data.sload),3))
print("Standard deviation:",round(stats.stdev(data.sload),3))
print("Variance:",round(stats.variance(data.sload),3))
data['z_score8']=(data.sload-data.sload.mean())/data.sload.std()
data

print("Mean:",round(stats.mean(data.dload),3))
print("Mode:",round(stats.mode(data.dload),3))
print("Median:",round(stats.median(data.dload),3))
print("Standard deviation:",round(stats.stdev(data.dload),3))
print("Variance:",round(stats.variance(data.dload),3))
data['z_score9']=(data.dload-data.dload.mean())/data.dload.std()
data

print("Mean:",round(stats.mean(data.sloss),3))
print("Mode:",round(stats.mode(data.sloss),3))
print("Median:",round(stats.median(data.sloss),3))
print("Standard deviation:",round(stats.stdev(data.sloss),3))
print("Variance:",round(stats.variance(data.sloss),3))
data['z_score10']=(data.sloss-data.sloss.mean())/data.sloss.std()
data

print("Mean:",round(stats.mean(data.dloss),3))
print("Mode:",round(stats.mode(data.dloss),3))
print("Median:",round(stats.median(data.dloss),3))
print("Standard deviation:",round(stats.stdev(data.dloss),3))
print("Variance:",round(stats.variance(data.dloss),3))
data['z_score11']=(data.dloss-data.dloss.mean())/data.dloss.std()
data

print("Mean:",round(stats.mean(data.sinpkt),3))
print("Mode:",round(stats.mode(data.sinpkt),3))
print("Median:",round(stats.median(data.sinpkt),3))
print("Standard deviation:",round(stats.stdev(data.sinpkt),3))
print("Variance:",round(stats.variance(data.sinpkt),3))
data['z_score12']=(data.sinpkt-data.sinpkt.mean())/data.sinpkt.std()
data

print("Mean:",round(stats.mean(data.dinpkt),3))
print("Mode:",round(stats.mode(data.dinpkt),3))
print("Median:",round(stats.median(data.dinpkt),3))
print("Standard deviation:",round(stats.stdev(data.dinpkt),3))
print("Variance:",round(stats.variance(data.dinpkt),3))
data['z_score13']=(data.dinpkt-data.dinpkt.mean())/data.dinpkt.std()
data

print("Mean:",round(stats.mean(data.sjit),3))
print("Mode:",round(stats.mode(data.sjit),3))
print("Median:",round(stats.median(data.sjit),3))
print("Standard deviation:",round(stats.stdev(data.sjit),3))
print("Variance:",round(stats.variance(data.sjit),3))
data['z_score14']=(data.sjit-data.sjit.mean())/data.sjit.std()
data

print("Mean:",round(stats.mean(data.djit),3))
print("Mode:",round(stats.mode(data.djit),3))
print("Median:",round(stats.median(data.djit),3))
print("Standard deviation:",round(stats.stdev(data.djit),3))
print("Variance:",round(stats.variance(data.djit),3))
data['z_score15']=(data.djit-data.djit.mean())/data.djit.std()
data

print("Mean:",round(stats.mean(data.swin),3))
print("Mode:",round(stats.mode(data.swin),3))
print("Median:",round(stats.median(data.swin),3))
print("Standard deviation:",round(stats.stdev(data.swin),3))
print("Variance:",round(stats.variance(data.swin),3))
data['z_score16']=(data.swin-data.swin.mean())/data.swin.std()
data

print("Mean:",round(stats.mean(data.stcpb),3))
print("Mode:",round(stats.mode(data.stcpb),3))
print("Median:",round(stats.median(data.stcpb),3))
print("Standard deviation:",round(stats.stdev(data.stcpb),3))
print("Variance:",round(stats.variance(data.stcpb),3))
data['z_score17']=(data.stcpb-data.stcpb.mean())/data.stcpb.std()
data

print("Mean:",round(stats.mean(data.dtcpb),3))
print("Mode:",round(stats.mode(data.dtcpb),3))
print("Median:",round(stats.median(data.dtcpb),3))
print("Standard deviation:",round(stats.stdev(data.dtcpb),3))
print("Variance:",round(stats.variance(data.dtcpb),3))
data['z_score18']=(data.dtcpb-data.dtcpb.mean())/data.dtcpb.std()
data

print("Mean:",round(stats.mean(data.dwin),3))
print("Mode:",round(stats.mode(data.dwin),3))
print("Median:",round(stats.median(data.dwin),3))
print("Standard deviation:",round(stats.stdev(data.dwin),3))
print("Variance:",round(stats.variance(data.dwin),3))
data['z_score19']=(data.dwin-data.dwin.mean())/data.dwin.std()
data

print("Mean:",round(stats.mean(data.tcprtt),3))
print("Mode:",round(stats.mode(data.tcprtt),3))
print("Median:",round(stats.median(data.tcprtt),3))
print("Standard deviation:",round(stats.stdev(data.tcprtt),3))
print("Variance:",round(stats.variance(data.tcprtt),3))
data['z_score20']=(data.tcprtt-data.tcprtt.mean())/data.tcprtt.std()
data

print("Mean:",round(stats.mean(data.synack),3))
print("Mode:",round(stats.mode(data.synack),3))
print("Median:",round(stats.median(data.synack),3))
print("Standard deviation:",round(stats.stdev(data.synack),3))
print("Variance:",round(stats.variance(data.synack),3))
data['z_score21']=(data.synack-data.synack.mean())/data.synack.std()
data

print("Mean:",round(stats.mean(data.ackdat),3))
print("Mode:",round(stats.mode(data.ackdat),3))
print("Median:",round(stats.median(data.ackdat),3))
print("Standard deviation:",round(stats.stdev(data.ackdat),3))
print("Variance:",round(stats.variance(data.ackdat),3))
data['z_score22']=(data.ackdat-data.ackdat.mean())/data.ackdat.std()
data

print("Mean:",round(stats.mean(data.smean),3))
print("Mode:",round(stats.mode(data.smean),3))
print("Median:",round(stats.median(data.smean),3))
print("Standard deviation:",round(stats.stdev(data.smean),3))
print("Variance:",round(stats.variance(data.smean),3))
data['z_score23']=(data.smean-data.smean.mean())/data.smean.std()
data

print("Mean:",round(stats.mean(data.dmean),3))
print("Mode:",round(stats.mode(data.dmean),3))
print("Median:",round(stats.median(data.dmean),3))
print("Standard deviation:",round(stats.stdev(data.dmean),3))
print("Variance:",round(stats.variance(data.dmean),3))
data['z_score24']=(data.dmean-data.dmean.mean())/data.dmean.std()
data

print("Mean:",round(stats.mean(data.trans_depth),3))
print("Mode:",round(stats.mode(data.trans_depth),3))
print("Median:",round(stats.median(data.trans_depth),3))
print("Standard deviation:",round(stats.stdev(data.trans_depth),3))
print("Variance:",round(stats.variance(data.trans_depth),3))
data['z_score25']=(data.trans_depth-data.trans_depth.mean())/data.trans_depth.std()
data

print("Mean:",round(stats.mean(data.response_body_len),3))
print("Mode:",round(stats.mode(data.response_body_len),3))
print("Median:",round(stats.median(data.response_body_len),3))
print("Standard deviation:",round(stats.stdev(data.response_body_len),3))
print("Variance:",round(stats.variance(data.response_body_len),3))
data['z_score26']=(data.response_body_len-data.response_body_len.mean())/data.response_body_len.std()
data

print("Mean:",round(stats.mean(data.ct_srv_src),3))
print("Mode:",round(stats.mode(data.ct_srv_src),3))
print("Median:",round(stats.median(data.ct_srv_src),3))
print("Standard deviation:",round(stats.stdev(data.ct_srv_src),3))
print("Variance:",round(stats.variance(data.ct_srv_src),3))
data['z_score27']=(data.ct_srv_src-data.ct_srv_src.mean())/data.ct_srv_src.std()
data

print("Mean:",round(stats.mean(data.ct_state_ttl),3))
print("Mode:",round(stats.mode(data.ct_state_ttl),3))
print("Median:",round(stats.median(data.ct_state_ttl),3))
print("Standard deviation:",round(stats.stdev(data.ct_state_ttl),3))
print("Variance:",round(stats.variance(data.ct_state_ttl),3))
data['z_score28']=(data.ct_state_ttl-data.ct_state_ttl.mean())/data.ct_state_ttl.std()
data

print("Mean:",round(stats.mean(data.ct_dst_ltm),3))
print("Mode:",round(stats.mode(data.ct_dst_ltm),3))
print("Median:",round(stats.median(data.ct_dst_ltm),3))
print("Standard deviation:",round(stats.stdev(data.ct_dst_ltm),3))
print("Variance:",round(stats.variance(data.ct_dst_ltm),3))
data['z_score29']=(data.ct_dst_ltm-data.ct_dst_ltm.mean())/data.ct_dst_ltm.std()
data

print("Mean:",round(stats.mean(data.ct_src_dport_ltm),3))
print("Mode:",round(stats.mode(data.ct_src_dport_ltm),3))
print("Median:",round(stats.median(data.ct_src_dport_ltm),3))
print("Standard deviation:",round(stats.stdev(data.ct_src_dport_ltm),3))
print("Variance:",round(stats.variance(data.ct_src_dport_ltm),3))
data['z_score30']=(data.ct_src_dport_ltm-data.ct_src_dport_ltm.mean())/data.ct_src_dport_ltm.std()
data

print("Mean:",round(stats.mean(data.ct_dst_sport_ltm),3))
print("Mode:",round(stats.mode(data.ct_dst_sport_ltm),3))
print("Median:",round(stats.median(data.ct_dst_sport_ltm),3))
print("Standard deviation:",round(stats.stdev(data.ct_dst_sport_ltm),3))
print("Variance:",round(stats.variance(data.ct_dst_sport_ltm),3))
data['z_score31']=(data.ct_dst_sport_ltm-data.ct_dst_sport_ltm.mean())/data.ct_dst_sport_ltm.std()
data

print("Mean:",round(stats.mean(data.ct_dst_src_ltm),3))
print("Mode:",round(stats.mode(data.ct_dst_src_ltm),3))
print("Median:",round(stats.median(data.ct_dst_src_ltm),3))
print("Standard deviation:",round(stats.stdev(data.ct_dst_src_ltm),3))
print("Variance:",round(stats.variance(data.ct_dst_src_ltm),3))
data['z_score32']=(data.ct_dst_src_ltm-data.ct_dst_src_ltm.mean())/data.ct_dst_src_ltm.std()
data

print("Mean:",round(stats.mean(data.is_ftp_login),3))
print("Mode:",round(stats.mode(data.is_ftp_login),3))
print("Median:",round(stats.median(data.is_ftp_login),3))
print("Standard deviation:",round(stats.stdev(data.is_ftp_login),3))
print("Variance:",round(stats.variance(data.is_ftp_login),3))
data['z_score33']=(data.is_ftp_login-data.is_ftp_login.mean())/data.is_ftp_login.std()
data

print("Mean:",round(stats.mean(data.ct_ftp_cmd),3))
print("Mode:",round(stats.mode(data.ct_ftp_cmd),3))
print("Median:",round(stats.median(data.ct_ftp_cmd),3))
print("Standard deviation:",round(stats.stdev(data.ct_ftp_cmd),3))
print("Variance:",round(stats.variance(data.ct_ftp_cmd),3))
data['z_score34']=(data.ct_ftp_cmd-data.ct_ftp_cmd.mean())/data.ct_ftp_cmd.std()
data

print("Mean:",round(stats.mean(data.ct_flw_http_mthd),3))
print("Mode:",round(stats.mode(data.ct_flw_http_mthd),3))
print("Median:",round(stats.median(data.ct_flw_http_mthd),3))
print("Standard deviation:",round(stats.stdev(data.ct_flw_http_mthd),3))
print("Variance:",round(stats.variance(data.ct_flw_http_mthd),3))
data['z_score35']=(data.ct_flw_http_mthd-data.ct_flw_http_mthd.mean())/data.ct_flw_http_mthd.std()
data

print("Mean:",round(stats.mean(data.ct_src_ltm),3))
print("Mode:",round(stats.mode(data.ct_src_ltm),3))
print("Median:",round(stats.median(data.ct_src_ltm),3))
print("Standard deviation:",round(stats.stdev(data.ct_src_ltm),3))
print("Variance:",round(stats.variance(data.ct_src_ltm),3))
data['z_score36']=(data.ct_src_ltm-data.ct_src_ltm.mean())/data.ct_src_ltm.std()
data

print("Mean:",round(stats.mean(data.ct_srv_dst),3))
print("Mode:",round(stats.mode(data.ct_srv_dst),3))
print("Median:",round(stats.median(data.ct_srv_dst),3))
print("Standard deviation:",round(stats.stdev(data.ct_srv_dst),3))
print("Variance:",round(stats.variance(data.ct_srv_dst),3))
data['z_score37']=(data.ct_srv_dst-data.ct_srv_dst.mean())/data.ct_srv_dst.std()
data

print("Mean:",round(stats.mean(data.is_sm_ips_ports),3))
print("Mode:",round(stats.mode(data.is_sm_ips_ports),3))
print("Median:",round(stats.median(data.is_sm_ips_ports),3))
print("Standard deviation:",round(stats.stdev(data.is_sm_ips_ports),3))
print("Variance:",round(stats.variance(data.is_sm_ips_ports),3))
data['z_score38']=(data.is_sm_ips_ports-data.is_sm_ips_ports.mean())/data.is_sm_ips_ports.std()
data

"""# Histogram of Mean Data"""

data_dict={'dur':18.666,'dpkts':17.546,'ct_srv_src':9.547}
attribute=list(data_dict.keys())
meanvalue=list(data_dict.values())
plt.bar(attribute,meanvalue)
plt.xlabel("Attribute name")
plt.ylabel("Values")
plt.title("Mean values for some attribute")
plt.show()

data_dict={'sloss':4.754,'dloss':6.309,'ct_dst_ltm':5.745}
attribute=list(data_dict.keys())
meanvalue=list(data_dict.values())
plt.bar(attribute,meanvalue)
plt.xlabel("Attribute name")
plt.ylabel("Values")
plt.title("Mean values for some attribute")
plt.show()

"""
# Histogram of Mode Data
```

```

"""

data_dict={'ct_dst_ltm':1,'ct_dst_sport_ltm':1,'ct_src_dport_ltm':1}
attribute=list(data_dict.keys())
modevalue=list(data_dict.values())
plt.bar(attribute,meanvalue)
plt.xlabel("Attribute name")
plt.ylabel("Values")
plt.title("Mode values for some attribute")
plt.show()

"""# Measures about the data"""

test1="/content/drive/MyDrive/Data/mydata.csv"
data1=pd.read_csv(test1)
data1

data1['label'].value_counts()

"""1 --> Attack Network

0 --> Non-Attack Network

# Splitting the Features and Target
"""

X=data1.drop(columns='label',axis=1)
Y=data1['label']

print(X)

print(Y)

"""# Splitting the Data into Training data & Test Data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)
print(X.shape, X_train.shape, X_test.shape)

"""# Model Training

# Logistic Regression
"""

model = LogisticRegression()

# training the LogisticRegression model with Training data
model.fit(X_train, Y_train)

"""# Model Evaluation

# Accuracy Score
"""

X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Accuracy on Training data : ', training_data_accuracy)

# accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Accuracy on Test data : ', test_data_accuracy)

input_data = (0.121478,6,4,258,172,74.08749,252,254,14158.94238,8906,90,8495.365234,0,0,24.2956,8.375,30.177547,11.830604,255,621772692,2202533631,255,0,0,0,43,43,0,0,1,0,1,1,1,1,0,0,0,1,1,0)
# Add a dummy feature to the input data
input_data = input_data [:-1]

# Convert the input data to a NumPy array
input_data_as_numpy_array = np.asarray(input_data)

# Reshape the input data for prediction
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

# Make the prediction
prediction = model.predict(input_data_reshaped)

# Print the prediction and interpret the result
if prediction[0] == 0:
    print('Network is not under attack')
else:
    print('Network is under attack')

