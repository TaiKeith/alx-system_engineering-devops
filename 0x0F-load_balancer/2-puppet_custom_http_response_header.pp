exec { 'update':
  command => '/usr/bin/apt-get update',
  refreshonly => true
}

package { 'nginx':
  ensure  => 'present',
  require => Exec['update']
}

file_line { 'http_header':
  path   => '/etc/nginx/nginx.conf',
  match  => 'http {',
  line   => "    add_header X-Served-By \"\${hostname}\";",
  notify => Exec['nginx_restart'],
}

exec { 'nginx_restart':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
  subscribe   => File_line['http_header'],
}
