# Ensure flask package is installed with specific version
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Ensure Werkzeug package is installed with specific version
package { 'werkzeug':
  ensure   => '2.0.2',
  provider => 'pip3',
}
