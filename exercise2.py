ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

email = ramit['email']
print(email)

first_interest = ramit['interests'][0]
print(first_interest)

email_Jasmine = ramit['friends'][0]['email']
print(email_Jasmine)

second_interest_Jan = ramit['friends'][1]['interests'][1]
print(second_interest_Jan)
