# Puppet that manuscript to replace line in the file on the server

$file_to_edit = '/var/www/html/wp-settings.php'

#To find and replace line containing "phpp" with "php"

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin','/usr/bin']
}
