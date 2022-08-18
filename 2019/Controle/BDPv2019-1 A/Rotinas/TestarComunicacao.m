% Abrir porta de comunicação com robôs
try
    fclose(instrfindall)
end

COM.Porta = serial('COM7','BaudRate',115200);
fopen(COM.Porta);

pause(1) 

% PARA TESTAR O ROBÔ FORA DA PARTIDA
% Máximo para frente
COM.msg = ['B' 'D' 230*[1 1 1 1 1 1] 'P' 10];

% Máximo para trás
% COM.msg = ['B' 'D' 50*[1 1 1 1 1 1] 'P' 10]; 
    
% Giro máximo anti-horário
% COM.msg = ['B' 'D' 50 230 50 230 50 230 'P' 10];

% Giro máximo horário
% COM.msg = ['B' 'D' 230 50 230 50 230 50 'P' 10];

% COM.msg = ['B' 'D' 190 110 190 110 190 110 'P' 10];

disp('Testando comunicação......')

t = tic;
while toc(t) < 0.1
    fwrite(COM.Porta,COM.msg,'char');
    tc = tic;
    while toc(tc) < 0.05
    end
end

fclose(COM.Porta);