import csv
import json
import time


with open('test.json', 'r' ,  encoding='utf-8') as json_file:
    data = json.load(json_file)


with open('education_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    
   
    header_row = ['Full Name', 'Position', 'Location']
    for i in range(1, 6): 
        header_row.extend(['Degree {}'.format(i), 'Start Time {}'.format(i), 'End Time {}'.format(i)])
    csvwriter.writerow(header_row)

 
    for entry in data:
        full_name = entry['full_name']
        position = entry['position']
        location = entry['location']
        education = entry['education']
        
     
        unique_degrees = set()
        degrees_info = []

        for edu in education:
            if edu.get("degree") is None:
                continue
            degree_str = " ".join(edu['degree'])
            start_time = edu.get('start_time', '')  
            end_time = edu.get('end_time', '') 
            if degree_str and degree_str not in unique_degrees:
                degrees_info.append((degree_str, start_time, end_time))
                unique_degrees.add(degree_str)
        
  
        while len(degrees_info) < 5:
            degrees_info.append(('', '', ''))
        
 
        row_data = [full_name, position, location]
        for degree, start_time, end_time in degrees_info:
            row_data.extend([degree, start_time, end_time])
        csvwriter.writerow(row_data)