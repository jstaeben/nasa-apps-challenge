clear; clc;
location = input('Enter reigon of first case: 1 for city, 2 for suburbs, and 3 for beach: ');
if location == 1
    locRisk = 3;
    spread = 3;
elseif location == 2
    locRisk = 1.5;
    spread = 2;
else
    locRisk = 1.5;
    spread = 1;
end
int = input('Enter light intensity from 0-10. 0 for well below average, 10 for well above: ');
intRisk = int/3;
mob = input('Enter reigon to reigon mobility from 0-10. 0 for well below average, 10 for well above: ');
mobEx = mob/3;
disp('Enter social distancing protocols.');
soc = input('1 for no SD, 2 for disobeyed SD, 3 for obeyed SD: ');
if soc == 1
    socRisk = 3;
elseif soc == 2
    socRisk = 2;
else
    socRisk = 1;
end
Risk = locRisk+intRisk+socRisk
Expand = mobEx+spread
if Risk <= 3.1111
    disp('There is low overall risk of an outbreak.');
elseif Risk <= 6.2222    
    disp('There is medium overall risk of an outbreak.');
else
    disp('There is high overall risk of an outbreak.');
end
if  Expand <= 2.1111
    disp('If an outbreak occurs, it is likely to stay concentrated in its reigon of origin.');
elseif Expand <= 4.2222
    disp('If an outbreak occurs, it may spread to other reigons from its reigon of origin.');
else
    disp('If an outbreak occurs, it will likely spread to other reigons from its reigon of origin.');
end