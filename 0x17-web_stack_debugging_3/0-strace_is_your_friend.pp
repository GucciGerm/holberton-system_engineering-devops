# This puppet script will use operators s to swap the values phpp with
# php, using option g will apply all changes to all matches
exec {'/var/www/html/wp-setting.php':
  path    => ['/bin'],
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",}
