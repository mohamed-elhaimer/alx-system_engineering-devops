# install flask from pip3 within requirement
file { 'flask'
    ensure      => '2.1.0',
    provider    => 'pip3',
}
