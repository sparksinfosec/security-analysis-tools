# Win32.pl 

# Stephen Sparks - IFT 475 - Perl Script that shows system information using the Win32 API

use win32;
$login = Win32::LoginName(); # Returns the username of the person running Perl 
$NetBIOS = Win32::NodeName(); #Returns NetBIO computer name 
$Filesystem = Win32::FsType(); #Returns name of the file system
$Directory = Win32::GetCwd(); #Returns the curren active drive 
$os_name = Win32::GetOSName(); # Returns OS name 
$time_since_start = Win32::GetTickCount(); # returns time elaspsed since th system first started
$admin_user = Win32::IsAdminUser(); # returns if non zero if account is part of built in admin 0 if not

# If statment to show if the current user is an admin or not
if ($admin_user == 0){
	$admin_is_root = "This user is not an admin:"
}
else {
	$admin_is_root = "This user maybe an admin:"
}
 
print "Username: $login\n"; #Print the username
print "Computer Name: $NetBIOS\n"; #Print Computer name
print "Filesystem Type: $Filesystem\n"; #Print the current filesytem type
print "Current DIR: '$Directory'\n"; #Print current directory/pwd
print "OS Name: $os_name\n"; #Print OS name
print "Time Since System Start: $time_since_start ms\n"; #Print tick count time since System was started (milliseconds)
print "$admin_is_root $admin_user\n"; #print the results of IF statment and if user is an admin


