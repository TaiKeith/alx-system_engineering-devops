# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx server
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => '
server {
    listen 80;
    server_name _;

    location / {
        return 200 "Hello World!";
    }

    location /redirect_me {
        return 301 https://youtu.be/D1v0FNR3-Xc;
    }
}'
  ,
  notify  => Service['nginx'],
}

# Create a symbolic link to enable the site
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
}

# Remove the default nginx configuration
file { '/etc/nginx/sites-enabled/default':
  ensure => absent,
}

# Ensure nginx service is running
service { 'nginx':
  ensure => running,
  enable => true,
}
