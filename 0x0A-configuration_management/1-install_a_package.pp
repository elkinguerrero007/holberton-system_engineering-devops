# install package with puppet
# Install a package
package { 'flask' :
     ensure        => 'present',
     pkgname       => 'requests',
     pip_provider  => 'pip3',
     virtualenv    => '/var/www/project1',
     owner         => 'root',
     timeout       => 1800
   }
