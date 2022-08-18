A = str2num(Comunic.Potencia(7).String)
B = str2num(Comunic.Potencia(8).String)

COM.msg = ['B' 'D' A B A B A B 'P' 10]; % Valor real é -150
    for i = 1:500
    
    %fprintf(COM.Porta,COM.msg);

    fwrite(COM.Porta,COM.msg,'char');

    end
  
    
  