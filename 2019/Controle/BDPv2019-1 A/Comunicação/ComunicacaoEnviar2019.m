COM.msg = ['B' 'D' 200 200 200 200 180 120 'P' 10]; % Valor real é -150
    for i = 1:100
    
    %fprintf(COM.Porta,COM.msg);

    fwrite(COM.Porta,COM.msg,'char');

end