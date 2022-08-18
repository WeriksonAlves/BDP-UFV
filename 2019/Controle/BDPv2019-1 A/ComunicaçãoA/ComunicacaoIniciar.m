% Abrir porta de comunicação com robôs
try
    fclose(instrfindall)
end

COM.Porta = serial('COM11','BaudRate',115200);
fopen(COM.Porta);

set(BDP.status(1),'string',' Comunicação Iniciada')
set(BDP.status(2),'string','Ecolha a opção desejada ')