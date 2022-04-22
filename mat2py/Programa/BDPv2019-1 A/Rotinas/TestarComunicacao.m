% Abrir porta de comunica��o com rob�s
try
    fclose(instrfindall)
end

COM.Porta = serial('COM7','BaudRate',115200);
fopen(COM.Porta);

pause(1) 

% PARA TESTAR O ROB� FORA DA PARTIDA
% M�ximo para frente
COM.msg = ['B' 'D' 230*[1 1 1 1 1 1] 'P' 10];

% M�ximo para tr�s
% COM.msg = ['B' 'D' 50*[1 1 1 1 1 1] 'P' 10]; 
    
% Giro m�ximo anti-hor�rio
% COM.msg = ['B' 'D' 50 230 50 230 50 230 'P' 10];

% Giro m�ximo hor�rio
% COM.msg = ['B' 'D' 230 50 230 50 230 50 'P' 10];

% COM.msg = ['B' 'D' 190 110 190 110 190 110 'P' 10];

disp('Testando comunica��o......')

t = tic;
while toc(t) < 0.1
    fwrite(COM.Porta,COM.msg,'char');
    tc = tic;
    while toc(tc) < 0.05
    end
end

fclose(COM.Porta);