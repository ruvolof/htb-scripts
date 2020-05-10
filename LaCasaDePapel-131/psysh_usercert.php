/*<?php
/*
/* Copy paste the following php code into psysh shell.
/* Spawn a psysh shell on port 6200 using the vsftpd 2.3.4 backdoor
*/

// Data for CSR
$me = array(
    "countryName" => "IT",
    "stateOrProvinceName" => "Marche",
    "localityName" => "Pescara",
    "organizationName" => "Fishing Creds",
    "organizationalUnitName" => "Stupid PHP Abuse",
    "commonName" => "Wat Dafak",
    "emailAddress" => "wat@dafak.com"
);

// Private key to sign CSR
$kconfig = array(
    "digest_alg" => "sha512",
    "private_key_bits" => 4096,
    "private_key_type" => OPENSSL_KEYTYPE_RSA,
);
$pkey = openssl_pkey_new($kconfig);

// Creating certificate request
$csr = openssl_csr_new($me, $pkey, array('digest_alg' => 'sha256'));

// Loading private key and signing request
$cert = openssl_csr_sign($csr, null, $key, $days=365, array('digest_alg' => 'sha256'));

openssl_x509_export($cert, $certout) and var_dump($certout);
