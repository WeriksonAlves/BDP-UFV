A = str2num(Comunic.Potencia(1).String)
B = str2num(Comunic.Potencia(2).String)

C = str2num(Comunic.Potencia(3).String)
D = str2num(Comunic.Potencia(4).String)

E = str2num(Comunic.Potencia(5).String)
F = str2num(Comunic.Potencia(6).String)

COM.msg = ['B' 'D' A B C D E F 'P' 10]; % Valor real é -150
    for i = 1:500
    
    %fprintf(COM.Porta,COM.msg);

    fwrite(COM.Porta,COM.msg,'char');

    end
    
    set(BDP.status(1),'string','')
    set(BDP.status(2),'string','')