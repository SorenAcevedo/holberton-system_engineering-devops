# Change file configuration
include stdlib

file_line { 'Use file config '
  path => '~/.ssh/holberton',
  line =>  'IdentityFile ~/.ssh/holberton'
}

file_line { 'Set Passw Auth'
  path => '~/.ssh/holberton',
  line =>  'PasswordAuthentication no'
}