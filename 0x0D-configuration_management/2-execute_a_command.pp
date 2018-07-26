# Using puppet, we will create a manifestation that kills that process
# killmenow using pkill and exec
exec { 'killmenow':
  command => '/usr/bin/pkill -f killmenow'

}
