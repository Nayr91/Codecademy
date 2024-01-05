medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Add your code here

updated_medical_data = medical_data.replace('#', '$')
num_records = 0

for i in updated_medical_data:
  if i == '$':
    num_records += 1

print(f"There are {num_records} medical records in the data.")

medical_data_split = updated_medical_data.split(";")
medical_records = []

for j in medical_data_split:
  medical_records.append(j.split(","))

medical_records_clean = []
for mrec in medical_records:
  record_clean = []
  for i in mrec:
    record_clean.append(i.strip())
  medical_records_clean.append(record_clean)

names = []
ages = []
bmis = []
insurance_costs = []
for p in medical_records_clean:
  p[0] = p[0].upper()
  names.append(p[0])
  ages.append(p[1])
  bmis.append(p[2])
  insurance_costs.append(p[3])

total_bmi = 0
for total in bmis:
  total_bmi += float(total)
print(f"Average BMI: {total_bmi}")
