def format_name(f_name, l_name):
  if f_name == '' or l_name == '':
    return 'You didnt provide valid inputs'
  form_f_name = f_name.title()
  form_l_name = l_name.title()
  return f'{form_f_name} {form_l_name}'

print(format_name('angela', 'YU'))
