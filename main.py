from testinput import greet_user, Anonymoussurvey

# def welcome_user():
#     '''Take inputs from the user and welcome him/her'''
#     print('Plesae enter your first and last name: \n')
#     while True:
#         first_name = input('please enter first name: \n')
#         if first_name == 'q':
#             break
#         second_name = input('please enter second name: \n')
#         if first_name == 'q':
#             break
#         formatted_name = greet_user(first_name, second_name)
#         print(f'Hellow {formatted_name}')

# welcome_user()

survey_one = Anonymoussurvey('what\'s my name?')
survey_one.show_question()
survey_one.add_responses('john doe')
print(vars(survey_one))


