clc, clear all, close all;
COM.Porta = serial('COM5', 'BaudRate', 115200);
fopen(COM.Porta);
t = tic;
debugTime = 0;
while toc(t) < 22

    if toc(t) < 10
        COM.msg = ['B', 'D', 180, 120, 180, 120, 180, 120, 'P', 10];
    elseif toc(t) >= 10
        COM.msg = ['B', 'D', 120, 180, 120, 180, 120, 180, 'P', 10];
    end

    fwrite(COM.Porta, COM.msg, 'char');

    t1 = tic;
    while toc(t1) < .01
    end

    if toc(t) - debugTime > 10 % A cada 10s verifica a perda de pacote
        Loss = char2array(fscanf(COM.Porta, '%c'));
        disp(Loss)
        debugTime = toc(t);
    end

    end
    fclose(COM.Porta);