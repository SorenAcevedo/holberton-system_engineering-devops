# Change file configuration
include stdlib

file_line { 'Use file config '
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton'
}

file_line { 'Set Passw Auth'
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no'
}