clear; clc;
location = input('Enter reigon: 1 for city, 2 for suburbs, and 3 for beach: ');
if location == 1
    locRisk = 3;
else
    locRisk =1.5;
end
int = input('Enter light intensity from 0-10. 0 for well below average, 10 for well above: ');
intRisk = int/3;
mob = input('Enter mobility from 0-10. 0 for well below average, 10 for well above: ');
mobRisk = int/3;
disp('Enter social distancing protocols.');
soc = input('1 for no SD, 2 for disobeyed SD, 3 for obeyed SD: ');
if soc == 1
    socRisk = 3;
elseif soc == 2
    socRisk = 2;
else
    socRisk = 1;
end
Risk = locRisk+intRisk+mobRisk+socRisk
if Risk <= 4.2222
    disp('This reigon under these conditions has low risk of an outbreak');
elseif Risk <= 8.4444
    disp('This reigon under these conditions has medium risk of an outbreak');
else
    disp('This reigon under these conditions has high risk of an outbreak');
end
    
