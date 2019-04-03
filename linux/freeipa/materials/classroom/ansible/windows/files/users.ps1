$pwd = convertto-securestring "RedHat123^" -asplaintext -force
New-ADUser -Name "Ad User01" -GivenName Ad -Surname User01 -SamAccountName aduser01 -UserPrincipalName aduser01@example.net -AccountPassword $pwd -PassThru | Enable-ADAccount
New-ADUser -Name "Ad User02" -GivenName Ad -Surname User02 -SamAccountName aduser02 -UserPrincipalName aduser02@example.net -AccountPassword $pwd -PassThru | Enable-ADAccount
New-ADUser -Name "Ad User03" -GivenName Ad -Surname User03 -SamAccountName aduser03 -UserPrincipalName aduser03@example.net -AccountPassword $pwd -PassThru | Enable-ADAccount
New-ADUser -Name "Ad User04" -GivenName Ad -Surname User04 -SamAccountName aduser04 -UserPrincipalName aduser04@example.net -AccountPassword $pwd -PassThru | Enable-ADAccount
New-ADUser -Name "Ad User05" -GivenName Ad -Surname User05 -SamAccountName aduser05 -UserPrincipalName aduser05@example.net -AccountPassword $pwd -PassThru | Enable-ADAccount
New-ADUser -Name "Ad Demo" -GivenName Ad -Surname Demo -SamAccountName demoaduser01 -UserPrincipalName demoaduser01@example.net -AccountPassword $pwd -PassThru | Enable-ADAccount
