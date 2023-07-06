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

def AskQuestions(question):
  my_survey = Anonymoussurvey(question)
  print('Answer the questions below')
  print('If you want to exit, enter q')
  my_survey.show_question()  
  While True:
    response = input("Your answer: ")
    if response = 'q':
      break
    my_survey.add_response(response)
  print(f'Your answer {my_survey.show_results()}')
  
AskQuestions("What's your name")