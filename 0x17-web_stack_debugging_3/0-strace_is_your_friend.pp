# Change phpp by php, fix 500 error
exec { 'fixbug'
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  provider => '/usr/bin:/usr/sbin:/bin',
}
