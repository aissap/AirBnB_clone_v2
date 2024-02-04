# Configures a web server for deployment of web_static.

package { 'nginx':
  ensure => 'installed',
}

file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']:
  ensure => 'directory',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => "<html>\n<head>\n</head>\n<body>\nHolberton School\n</body>\n</html>",
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
}

exec { 'chown_data_directory':
  command => 'chown -R ubuntu:ubuntu /data',
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => template('path/to/nginx_config_template.erb'),
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
