clear all
% filename1 = 'Y1.xlsx';
% Y1 = xlsread(filename1);
% Y_sub1 = Y1(2:end,2);
% writematrix(Y_sub1,strcat('Y1.txt'));
% 
% filename2 = 'Y2.xlsx';
% Y2 = xlsread(filename2);
% Y_sub2 = Y2(2:end,2);
% writematrix(Y_sub2,strcat('Y2.txt'));
% 
% filename3 = 'Y3.xlsx';
% Y3 = xlsread(filename3);
% Y_sub3 = Y3(2:end,2);
% writematrix(Y_sub3,strcat('Y3.txt'));

filename = 'Exp_Data.xlsx';
YT = xlsread(filename);
YTa(:,1) = YT(:,3) + 24.8 + 273.15; %dw
% YTa(:,1) = YT(:,2)+ 24.8 + 273.15; %25
% YTa(:,1) = YT(:,1)+ 24.8 + 273.15; %50

writematrix(YTa,strcat('Exp_Data_Kel_DW.txt'));




