# using Puppet to make changes to our configuration file
file { '/root/.ssh/config':
  ensure  => file,
  content => "
	HOST ubuntu
	  HostName 100.25.204.148
 	  IdentityFile ~/.ssh/school
	  PreferredAuthentications publickey
	  PasswordAuthentication no
  ",
  owner  => amir,
  group  => amir,
  mode   => '0600',
}

