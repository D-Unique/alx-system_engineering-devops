#this puppet file make the config not accept passweordauth and make it look for the private key
file { '/etc/ssh/ssh_config':
  ensure => present,
  content => '# SSH configuration for dev server
    Host dev
        HostName 54.237.23.230
        User ubuntu
        PasswordAuthentication no
        ChallengeResponseAuthentication no
        IdentityFile ~/.ssh/school
        UsePAM no'
}
