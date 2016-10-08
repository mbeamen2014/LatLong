#!/usr/bin/perl -w
use Math::Trig qw(great_circle_distance deg2rad);
use Scalar::Util qw(looks_like_number);
use CGI;
my $cgi = new CGI;

$lat1 = $cgi->param("First Latitude");
$long1 = $cgi->param("First Longitude");
$lat2 = $cgi->param("Second Latitude");
$long2 = $cgi->param("Second Longitude");

if (($lat1 eq "") || ($long1 eq "") || ($lat2 eq "") || ($long2 eq "") ){
    print "\nOne or more of your fields is empty. Enter a number in all fields.\n";
    next;
  }

if ((looks_like_number($lat1) == 0) || (($lat1 > 90) || ($lat1 < -90))) {
    print "\nLatitude field out of range.\n";
    next;
  }
if ((looks_like_number($lat2) == 0) || (($lat2 > 90) || ($lat2 < -90))) {
    print "\nLatitude field out of range.\n";
    next;
  }
if ((looks_like_number($long1) == 0) || (($long1 > 180) || ($long1 < -180))) {
    print "\nLongitude field out of range.\n";
    next;
  }
if ((looks_like_number($long2) == 0) || (($long2 > 180) || ($long2 < -180))) {
    print "\nLongitude field out of range.\n";
    next;
  }
 

sub NESW { deg2rad($_[0]), deg2rad(90 - $_[1]) }
my @L = NESW($long1, $lat1);
my @T = NESW($long2, $lat2);
my $km = great_circle_distance(@L, @T, 6378);
my $miles = sprintf("%.2f", $km * 0.62137);	

print $cgi->header(-type=>'text/html'),
      $cgi->start_html('Great Circle Distance');

print $cgi->h1("Great Circle Distance");
print $cgi->p("First Latitude : " . $lat1);
print $cgi->p("First Longitude : " . $long1);
print $cgi->p("Second Latitude : " . $lat2);
print $cgi->p("Second Longitude : " . $long2);


									
print $cgi->p("Great Circle Distance: " . $miles . " miles");




print $cgi->img({src=>"http://maps.googleapis.com/maps/api/staticmap?size=300x185&maptype=roadmap
&frame=1&markers=color:blue|label:A|$lat1,$long1&markers=color:green|label:B|$lat2,$long2&path=color:red|weight:5|
geodesic:true|$lat1,$long1|$lat2,$long2&scale=2&sensor=false"});
 
print $cgi->end_html, "\n";