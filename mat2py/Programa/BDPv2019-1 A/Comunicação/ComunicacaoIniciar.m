% Abrir porta de comunica��o com rob�s
try
    fclose(instrfindall)
end

COM.Porta = serial('COM11','BaudRate',115200);
fopen(COM.Porta);
