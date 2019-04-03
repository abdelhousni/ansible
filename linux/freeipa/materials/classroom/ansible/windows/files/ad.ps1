# Create New Forest, add Domain Controller
$my_secure_password = convertto-securestring "password123!" -asplaintext -force
Import-Module ADDSDeployment
Install-ADDSForest `
-SkipPreChecks:$true `
-CreateDnsDelegation:$false `
-DatabasePath "C:\Windows\NTDS" `
-DomainMode "WinThreshold" `
-DomainName "example.net" `
-DomainNetbiosName "EXAMPLE" `
-ForestMode "WinThreshold" `
-InstallDns:$true `
-LogPath "C:\Windows\NTDS" `
-NoRebootOnCompletion:$false `
-SysvolPath "C:\Windows\SYSVOL" `
-SafeModeAdministratorPassword $my_secure_password `
-Force:$true
