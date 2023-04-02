<?php 

$command = escapeshellcmd('Htmlthings/beastgen.py');
$output = shell_exec($command);
echo $output;

?>