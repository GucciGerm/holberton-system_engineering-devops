# By applying this puppet script will increase the use of sys resources

exec { 'increase sys resources to 15000':
    path    => '/bin',
    command => 'sed -i '\s/15/15000/g'\ /etc/default/nginx',
}
exec { 'restart your nginx':
    path    => '/usr/bin',
    command => 'sudo service nginx restart',
}

