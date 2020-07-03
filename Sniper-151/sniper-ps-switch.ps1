$p = "36mEAhz/B8xQ~2VM"
$pass = $p | ConvertTo-SecureString -AsPlainText -Force
$user = "Sniper\Chris"
$cred = New-Object System.Management.Automation.PSCredential -ArgumentList $user,$pass
$sess = New-PSSession -Credential $cred | Enter-PSSession
