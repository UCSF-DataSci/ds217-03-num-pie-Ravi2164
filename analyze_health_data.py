#!/usr/bin/env python3
import numpy as np


def load_data(filename):
    """Load CSV data using NumPy"""

    dtype = [
          ('patient_id', 'U10'), 
          ('timestamp', 'U20'),
          ('heart_rate', 'i4'),
          ('blood_pressure_systolic', 'i4'),
          ('blood_pressure_diastolic', 'i4'), 
          ('temperature', 'f4'),
          ('glucose_level', 'i4'), 
          ('sensor_id', 'U10')
    ]

    data = np.genfromtxt(filename, delimiter=',', dtype=dtype, skip_header=1)
    return data

#**Function 2: `calculate_statistics(data)`**

def calculate_average(data):
    """Calculate average statistics"""
    print( "====Health Averages statistics====")

    average_temperature = np.mean(data['temperature'])
    average_heart_rate = np.mean(data['heart_rate'])
    average_glucose_level = np.mean(data['glucose_level'])
    average_systolic_bp = np.mean(data['blood_pressure_systolic'])
    average_diastolic_bp = np.mean(data['blood_pressure_diastolic'])

    print(f"Average Temperature:   {average_temperature:.2f} °F")
    print(f"Average Heart Rate:   {average_heart_rate:.2f} bpm")
    print(f"Average Glucose Level:   {average_glucose_level:.2f} mg/dL")
    print(f"Average Systolic BP:   {average_systolic_bp:.2f} mmHg")
    print(f"Average Diastolic BP:   {average_diastolic_bp:.2f} mmHg")
    print ()

    return {
        'average_temperature': average_temperature,
        'average_heart_rate': average_heart_rate,
        'average_glucose_level': average_glucose_level,
        'average_systolic_bp': average_systolic_bp,
        'average_diastolic_bp': average_diastolic_bp
    }

#**Function 3: `find_abnormal_readings(data)`**
def find_abnormal_readings(data):
    print ("====Abnormal Readings====")
    # Boolean conditions for abnormal readings

    high_heart_rate_condition = data['heart_rate'] > 90
    high_systolic_bp_condition = data['blood_pressure_systolic'] > 130
    high_glucose_condition = data['glucose_level'] > 110

    #count hhow manny records match the conditons
    high_heart_rate_count = np.count_nonzero(high_heart_rate_condition)
    high_systolic_bp_count = np.count_nonzero(high_systolic_bp_condition)
    high_glucose_count = np.count_nonzero(high_glucose_condition)
    
    # print the results
    print(f"High heart rate readings (>90 bpm): {high_heart_rate_count}")
    print(f"High systolic blood pressure readings (>130 mmHg): {high_systolic_bp_count}")
    print(f"High glucose level readings (>110 mg/dL): {high_glucose_count}")
    print()

    # return the counts 
    return {
        'high_heart_rate_count': high_heart_rate_count,
        'high_systolic_bp_count': high_systolic_bp_count,
        'high_glucose_count': high_glucose_count
    }

    
    #**Function 4: `generate_report(stats, abnormal, total_readings)`**
def generate_report(stats, abnormal, total_readings):
    """Generate a summary report"""
  
    report  = (
         "====Health Data Analysis Report====\n"
            f"Total Readings: {total_readings}\n\n"
            ">>Averages:\n"
            f"Average Temperature: {stats['average_temperature']:.1f} °F\n"
            f"Average Heart Rate: {stats['average_heart_rate']:.1f} bpm\n"
            f"Average Glucose Level: {stats['average_glucose_level']:.1f} mg/dL\n"
            f"Average Systolic BP: {stats['average_systolic_bp']:.1f} mmHg\n"
            f"Average Diastolic BP: {stats['average_diastolic_bp']:.1f} mmHg\n"
            f"High heart rate readings (>90 bpm): {abnormal['high_heart_rate_count']}\n"
            f"High systolic blood pressure readings (>130 mmHg): {abnormal['high_systolic_bp_count']}\n"
            f"High glucose level readings (>110 mg/dL): {abnormal['high_glucose_count']}\n"
    )

    return report 

def save_report(filename, report):
    """Save the report to a text file"""
    with open(filename, 'w') as f:
        f.write(report)
    print(f"Report saved to {filename}")


    #**Function 6: `main()`** (0.5 points)

def main():
    data = load_data('health_data.csv')
    stats = calculate_average(data)
    abnormal = find_abnormal_readings(data)
    total_readings = len(data)
    report = generate_report(stats, abnormal, total_readings)
    print(report)
    save_report('health_report.txt', report)

if __name__ == "__main__":
    main()