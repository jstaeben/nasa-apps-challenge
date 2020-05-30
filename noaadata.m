clear; clc;
Jan = imread('Jan30noaa.png');
May = imread('may26noaa.png');
Jan1 = rgb2gray(Jan);
May1 = rgb2gray(May);
[Janmag,Jandir] = imgradient(Jan1);
Janavg = mean(Janmag,'all')
[Maymag,Maydir] = imgradient(May1);
Mayavg = mean(Maymag,'all')