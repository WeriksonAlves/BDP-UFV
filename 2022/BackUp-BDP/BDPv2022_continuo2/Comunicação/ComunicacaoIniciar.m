% Abrir porta de comunicação com robôs
try
    fclose(instrfindall)
end

COM.Porta = serial('COM3','BaudRate',115200);
fopen(COM.Porta);

%edicao hiago
t_debug = tic;
debugTime = 0;

