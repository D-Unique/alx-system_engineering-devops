#this manifast installs flask of version 2.1.0 using pip3
package { 'python3-pip':
  ensure => present,
}

exec { 'install_flask':
  command => 'pip3 install flask==2.1.0',
  onlyif  => 'test -z "$(pip3 show flask | grep "Version: 2.1.0")"',
}
