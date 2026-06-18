import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

print("Sedang membaca file CSV...")
df_csv = pd.read_csv(r"E:\SEMESTER 2\Basis Data File\Tugas database python\healthcare_dataset.csv")

engine = create_engine("mysql+mysqlconnector://root:@localhost/hospital_db")


print("Sedang mengirim data ke MySQL Workbench... (Tunggu sebentar)")

df_csv.to_sql(name='patient_record', con=engine, if_exists='replace', index=False, chunksize=1000)
print("Berhasil! Data CSV sudah masuk ke Database.")


query_gender = """
SELECT Gender, COUNT(*) as total 
FROM patient_record 
GROUP BY Gender
"""
df_gender = pd.read_sql(query_gender, engine)

query_penyakit = """
SELECT `Medical Condition`, COUNT(*) as total 
FROM patient_record 
GROUP BY `Medical Condition` 
ORDER BY total DESC 
LIMIT 5
"""
df_penyakit = pd.read_sql(query_penyakit, engine)


query_darah = """
SELECT `Blood Type`, COUNT(*) as total 
FROM patient_record 
GROUP BY `Blood Type`
"""
df_darah = pd.read_sql(query_darah, engine)


plt.figure(figsize=(15, 5)) 


plt.subplot(1, 3, 1) 
plt.bar(df_gender["Gender"], df_gender["total"], color=['skyblue', 'lightpink'])
plt.title("Jumlah Pasien Berdasarkan Gender")
plt.xlabel("Gender")
plt.ylabel("Total Pasien")


plt.subplot(1, 3, 2) 
plt.bar(df_penyakit["Medical Condition"], df_penyakit["total"], color=['orange', 'green', 'red', 'purple', 'brown'])
plt.title("Top 5 Penyakit Terbanyak")
plt.xlabel("Jenis Penyakit")
plt.ylabel("Total Pasien")
plt.xticks(rotation=45) 

plt.subplot(1, 3, 3) 

warna_pastel = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666', '#c4e17f']

plt.pie(df_darah["total"], labels=df_darah["Blood Type"], autopct='%1.1f%%', startangle=140, colors=warna_pastel)
plt.title("Persentase Golongan Darah")

plt.tight_layout()
plt.show()