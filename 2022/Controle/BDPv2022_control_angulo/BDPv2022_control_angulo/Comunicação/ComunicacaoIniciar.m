% Abrir porta de comunicação com robôs
try
    fclose(instrfindall)
end

COM.Porta = serial('COM5','BaudRate',115200);
fopen(COM.Porta);

