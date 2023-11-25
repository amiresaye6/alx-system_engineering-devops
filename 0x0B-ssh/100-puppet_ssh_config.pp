# using Puppet to make changes to our configuration file

include stdlib

file_line { 'Refuse to authenticate using a password':
  ensure => present,
  path   => '/root/.ssh/config',
  line   => 'PasswordAuthentication no',
}

file_line { 'Use private key':
  ensure => present,
  path   => '/root/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school'
}
