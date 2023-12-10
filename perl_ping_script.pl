# ping.pl 
# Stephen Sparks - IFT 475 - Program pings IP addresses to search for active hosts


use diagnostics; #enhanced error messages and warning module
use Net::Ping; # ping module for network ping operations 

$p = Net::Ping->new(); #creates new ping object with default settings 
$my_IP = "192.168.0"; #assign start of IP to variable update to reflect current topology that will be scanned

for ($z=1; $z<255; $z++){ # For statment with variable iterating from 1 to 255 
	$wkstation = "$my_IP.$z"; #string concatenation creating the full IP to ping
	print "Looking for live systems to enumerate. Trying $wkstation \n"; #print that we are trying the IP address
	system("echo ***$wkstation is ready to enumerate***") if $p->ping($wkstation); #echo and conditional to print if ping is successful? 
}





