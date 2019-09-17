#cd '..\..\Program Files (x86)\VMware\VMware Workstation'
Write-Output("Setting Up Infrastructure")


Function VMclone{
Write-Output("Cloning VMs")
.\vmrun.exe -T ws clone $vmx1 $dest1 linked 
.\vmrun.exe -T ws clone $vmx2 $dest2 linked 
.\vmrun.exe -T ws clone $vmx3 $dest3 linked 
.\vmrun.exe -T ws clone $vmx4 $dest4 linked
.\vmrun.exe -T ws start $vmx1 gui
.\vmrun.exe -T ws start $vmx2 gui
.\vmrun.exe -T ws start $vmx3 gui
.\vmrun.exe -T ws start $vmx4 gui
}

Function SetupSrv{
Write-Output("Setting Up AD")
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools

#My COnfig from installation earlier

}

Function SetupPF{
}
Function SetupWinCLI{
}

Function SetupTuxCLI{
}