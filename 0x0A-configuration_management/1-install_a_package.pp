# Install flask from pip3
package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3'
}

# Install or upgrade Werkzeug to meet Flask 2.1.0 requirements
package { 'werkzeug':
    ensure   => '>=2.1.1',
    provider => 'pip3'
}
