% Abrir porta de comunica��o com rob�s
try
    fclose(instrfindall)
end

COM.Porta = serial('COM11','BaudRate',115200);
fopen(COM.Porta);

set(BDP.status(1),'string',' Comunica��o Iniciada')
set(BDP.status(2),'string','Ecolha a op��o desejada ')