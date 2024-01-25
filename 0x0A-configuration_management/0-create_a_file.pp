# create file in temp with given requirement
file { '/tmp/school':
    ensure  => 'file',
    mode    => '0744',
    content => 'I love Puppet',
    owner   => 'www-data',
    group   => 'www-data',
}
