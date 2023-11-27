# This script allows for authentication without password

file_line {'Disable Password Authentication':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no'
}

file_line {'Set Identity File':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school'
}
