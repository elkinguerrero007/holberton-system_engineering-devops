# Setup NGINX with Puppet manifest
package { 'nginx':
  ensure => installed,
}
exec { 'exec_2':
  command => 'echo "Holberton School" > /var/www/html/index.html',
  path    => ['/usr/bin', '/bin'],
}
exec { 'exec_3':
  require     => Exec['exec_2'],
  environment => ['GG=https://www.youtube.com/watch?v=QH2-TGUlwu4'],
  command     => 'sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me $GG;/" /etc/nginx/sites-enabled/default',
  path        => ['/usr/bin', '/bin'],
}

exec { 'exec_4':
  require     => Exec['exec_3'],
  command     => 'sed -i "48i \\\t\tadd_header X-Served-By $HOSTNAME always; /etc/nginx/sites-enabled/default',
  path        => ['/usr/bin', '/bin'],
}

service { 'nginx':
  ensure => running,
  require => Package['nginx'],
}
