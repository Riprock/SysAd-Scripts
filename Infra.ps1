$pfsensevmx = "C:\Virtual Machines\pfSense244VM\pfSense 2.4.4 x64.vmx"
$gatewayvmx ="P:\Gateway\gateway.vmx"
$win10vmx = "C:\Virtual Machines\VL_WIN10_64\Windows 10 x64.vmx"
$winclivmx = "P:\Wincli\wincli.vmx"
$win2k16vmx = "C:\Virtual Machines\VL_WINSERV2016_64\Windows Server 2016 x64.vmx"
$winsrvvmx = "P:\Winsrv\winsrv.vmx"
$centosvmx ="C:\Virtual Machines\STU_CentOS7.0_64\CentOS 64-bit.vmx"
$tuxclivmx = "P:\Tuxcli\Tuxcli\Tu.vmx"
Function SetupInfra{
cd '..\..\..\Program Files (x86)\VMware\VMware Workstation'
Write-Output("Setting Up Infrastructure")
VMclone
}

Function VMclone{
Write-Output("Cloning VMs")
.\vmrun.exe -T ws clone $pfsensevmx $gatewayvmx linked 
.\vmrun.exe -T ws clone $win10vmx $winclivmx linked 
.\vmrun.exe -T ws clone $win2k16vmx $winsrvvmx linked 
.\vmrun.exe -T ws clone $centosvmx $tuxclivmx linked
Write-Output("Starting VMs")
.\vmrun.exe -T ws start $gatewayvmx gui
.\vmrun.exe -T ws start $winclivmx gui
.\vmrun.exe -T ws start $winsrvvmx gui
.\vmrun.exe -T ws start $tuxclivmx gui
}

Function SetupSrv{
Write-Output("Setting Up AD")
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools
ADForest


#My COnfig from installation earlier
}

Function ADForest{
Import-Module ADDSDeployment
Install-ADDSForest `
-CreateDnsDelegation:$false `
-DatabasePath "C:\Windows\NTDS" `
-DomainMode "WinThreshold" `
-DomainName "domain" `
-DomainNetbiosName "netbios" `
-ForestMode "WinThreshold" `
-InstallDns:$true `
-LogPath "C:\Windows\NTDS" `
-NoRebootOnCompletion:$false `
-SysvolPath "C:\Windows\SYSVOL" `
-Force:$true
}


Function SetupPF{
$Keystrokes = @("1","n","em0","em1","y","2","2","192.168.73.254","24"," "," ","n","n"," ")
	foreach ($key in $Keystrokes){
		.\vmrun.exe -T ws typeKeystrokesInGuest $gatewayvmx $key
		}
#Might write a while loop here to do the setup of PFsense. While through a list of keystroke strings for configuration. Might Make work easier. WIll need to test
}
Function SetupWinCLI{

}

Function SetupTuxCLI{

}

SetupInfra