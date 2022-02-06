# Import Libraries
import sys


class BmiCalculator:
    """ Calculate the BMI (Body Mass Index) """
    def __init__(self):
        self.bmi_val = 0.0

    def bmi_formula(self, height, weight):
        """ BMI (Body Mass Index) formula """
        try:
            self.bmi_val = round(weight / (height/100) ** 2, 2)
            print("Your BMI Score : {} kg/m2".format(self.bmi_val))
        except Exception as err1:
            print("Error in BMI Formula Method : ", err1)
            print("Please Enter valid inputs....")

    def bmi_condition_range(self):
        """ BMI (Body Mass Index) Category and Health Risk """
        try:
            if 0.0 < self.bmi_val <= 18.4:
                category = "Underweight"
                risk = "Malnutrition Risk"
            elif 18.5 <= self.bmi_val <= 24.9:
                category = "Normal weight"
                risk = "Low Risk"
            elif 25.0 <= self.bmi_val <= 29.9:
                category = "Overweight"
                risk = "Enhanced Risk"
            elif 30.0 <= self.bmi_val <= 34.9:
                category = "Moderately Obese"
                risk = "Medium Risk"
            elif 35.0 <= self.bmi_val <= 39.9:
                category = "Severely Obese"
                risk = "High Risk"
            elif self.bmi_val >= 40.0:
                category = "Very Severely Obese"
                risk = "Very High Risk"
            else:
                category = None
                risk = None
            print("Your BMI Category : {} \nYour Health Status : {}".format(category, risk))
        except Exception as err2:
            print("Error in BMI Condition Range Method : ", err2)


def bmi_data_process(data):
    """ Calculate BMI (Body Mass Index) for list of dictionaries"""
    try:
        print("*********** >> Welcome To BMI Calculator << ***********")
        bmi_obj = BmiCalculator()
        for i in data:
            print("Input Data : ", i)
            bmi_obj.bmi_formula(i["HeightCm"], i["WeightKg"])
            bmi_obj.bmi_condition_range()
            print("*"*50)
    except Exception as err3:
        print('Error in BMI Data Process Function : ', err3)
        sys.exit(0)


def user_inputs():
    """ Checking User Inputs for BMI Calculator"""
    user_height_cm, user_weight_kg, user_gender = 0, 0, ''
    status = True
    while status:
        try:
            if user_height_cm == 0:
                user_height_cm = float(input("Enter Your Height in Centimeters (cm) : "))
            if user_weight_kg == 0:
                user_weight_kg = float(input("Enter Your Weight in Kilograms (kg) : "))
            user_gender = input("Enter Your Gender (Male or Female) : ")
            if user_gender in ["Male", "Female"]:
                status = False
        except ValueError:
            print("Please Enter Valid Input. Try Again.....")

    return user_height_cm, user_weight_kg, user_gender


def main():
    """ Main function for BMI Calculator"""
    try:
        print("*********** >> Welcome To BMI Calculator << ***********")
        height_cm, weight_kg, gender = user_inputs()
        print("     ::: BMI Status :::     ")
        bmi_obj = BmiCalculator()
        bmi_obj.bmi_formula(height_cm, weight_kg)
        bmi_obj.bmi_condition_range()
        print("*******************************************************\n")
        print("Please type 'quit' to Exit. \nPress Enter To Continue...")
        if input() == 'quit':
            sys.exit(0)
        else:
            main()
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == '__main__':
    ''' Enter the values one by one '''
    main()

    # ''' Pass the data (list of dictionaries) '''
    # data_list = [{"Gender": "Male", "HeightCm": 0, "WeightKg": 96 },
    #             { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
    #             { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
    #             { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
    #             {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
    #             {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
    # bmi_data_process(data_list)
