#this manifast installs kills a process named killmenow
exec { 'kill_killmenow_process':
  command => '/usr/bin/pkill -f killmenow',
  unless  => 'pgrep -f killmenow | wc -l == 0',
}
