# Configures a web server for deployment of web_static.
$nginx_conf = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 https:https://aissugar.tech;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"

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
