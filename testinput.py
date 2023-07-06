def greet_user(first, last, middle = ''):
  '''Takes the first and last name and returns a fill name'''
  if middle:
    full_name = f'{first} {middle} {last}'
  else:  
    full_name = f'{first} {last}'
  return full_name

print(greet_user('John', 'Doe', 'Henry'))

class Anonymoussurvey:
  '''collect anonymous survey reuslts'''

  def __init__(self, question):
    '''Store question and store resposnes'''
    self.question = question
    self.responses = []
  
  def show_question(self):
    '''show the question'''
    print(self.question)

  def add_responses(self, new_response):
    '''Adds resposnes'''
    self.responses.append(new_response)

  def show_results(self):
    '''show the results'''
    print('The responses are')
    for item in self.responses:
      print(f'{item}')  


